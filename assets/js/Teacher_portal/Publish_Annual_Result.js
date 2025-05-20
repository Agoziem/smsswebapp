// ------------------------------------------------------
// Imports
// ------------------------------------------------------
import AnnualClassResultHandler from "./utils/AnnualClassResulthandler.js";
import AnnualClassResultDataTable from "./datatable/AnnualClassResultDatatable.js";
import { getannualclassresult, publishstudentresult } from "./utils/serveractions.js";

// ------------------------------------------------------
// DOM References (cached once)
// ------------------------------------------------------
const DOM = {
  classInput:      document.querySelector(".classinput"),
  subjectListInput:document.querySelector(".subjectlist"),
  alertContainer:  document.querySelector(".alertcontainer"),
  sessionSelect:   document.getElementById("academicSessionSelect"),
  publishBtn:      document.getElementById("publishbtn"),
  resultBadge:     document.getElementById("resultbadge"),
  dataTableBody:   document.querySelector("#dataTable tbody"),
  resultsList:     document.querySelector("#resultspublished"),
};

// After the above, cache the two spans in your button (assuming you've split them):
DOM.btnLabel   = DOM.publishBtn.querySelector(".btn-label");
DOM.btnSpinner = DOM.publishBtn.querySelector(".btn-spinner");

// ------------------------------------------------------
// LocalStorage Keys
// ------------------------------------------------------
const LS_KEYS = { SESSION: "selectedAcademicSession" };

// ------------------------------------------------------
// App State
// ------------------------------------------------------
const appState = {
  classId:       DOM.classInput.value,
  selectedSession: null,
  results:       [],
  isPublished:   false,
};

// ------------------------------------------------------
// Helpers
// ------------------------------------------------------
const saveToLS    = (k, v)    => localStorage.setItem(k, v);
const readFromLS  = (k, fallback) => localStorage.getItem(k) || fallback;

function showAlert(type, msg) {
  DOM.alertContainer.innerHTML = "";
  const a = document.createElement("div");
  a.className = `alert alert-${type} d-flex align-items-center mt-3`;
  a.setAttribute("role","alert");
  a.innerHTML = `<i class="fa-solid fa-circle-check me-2"></i>${msg}`;
  DOM.alertContainer.append(a);
  setTimeout(()=> DOM.alertContainer.innerHTML="", 3000);
}

function setButtonLoading(on) {
  if (on) {
    DOM.publishBtn.disabled = true;
    DOM.btnSpinner.classList.remove("d-none");
    DOM.btnLabel.textContent = appState.isPublished
      ? "Unpublishing…" : "Publishing…";
  } else {
    DOM.publishBtn.disabled = false;
    DOM.btnSpinner.classList.add("d-none");
    DOM.btnLabel.textContent = appState.isPublished
      ? "Unpublish Result" : "Publish Result";
  }
}


const loadingTableData = () => {
  DOM.dataTableBody.innerHTML = `
    <tr>
      <td colspan="11" class="text-center">
        <div class="d-flex align-items-center justify-content-center">
          <div class="spinner-border spinner-border-sm me-2" aria-hidden="true"></div>
          <div role="status">Loading Annual Results...</div>
        </div>
      </td>
    </tr>`;
};

// ------------------------------------------------------
// Init: bind & initial load
// ------------------------------------------------------
(function init() {
  DOM.publishBtn.addEventListener("click", onPublishClick);
  DOM.sessionSelect.addEventListener("change", onSessionChange);
  window.addEventListener("DOMContentLoaded", loadSavedSession);

  // parse subject list once
  const raw = DOM.subjectListInput?.value ?? "[]";
  appState.subjectsMeta = JSON.parse(raw.replace(/'/g, '"'));

  // kick off
  loadSavedSession();
})();

// ------------------------------------------------------
// Session select handlers
// ------------------------------------------------------
function onSessionChange() {
  appState.selectedSession = DOM.sessionSelect.value;
  saveToLS(LS_KEYS.SESSION, appState.selectedSession);
  fetchAndRender();
}

function loadSavedSession() {
  DOM.sessionSelect.value = readFromLS(LS_KEYS.SESSION, DOM.sessionSelect.value);
  appState.selectedSession = DOM.sessionSelect.value;
  fetchAndRender();
}

// ------------------------------------------------------
// Publish click handler
// ------------------------------------------------------
async function onPublishClick() {
  if (!appState.results.length) {
    return showAlert("warning", "No result to publish");
  }

  setButtonLoading(true);
  const url = appState.isPublished
    ? "/Teachers_Portal/unpublishannualclassresult/"
    : "/Teachers_Portal/publishannualclassresult/";

  try {
    await publishstudentresult(
      url,
      appState.results,
      { studentclass: appState.classId, selectedAcademicSession: appState.selectedSession },
      showAlert
    );
    // re‑fetch to update badge & table
    setButtonLoading(true);
    await fetchAndRender();
  } catch (e) {
    console.error(e);
    showAlert("danger", "Failed to publish results");
  } finally {
    setButtonLoading(false);
  }
}

// ------------------------------------------------------
// Fetch + Render Pipeline
// ------------------------------------------------------
async function fetchAndRender() {
  DOM.alertContainer.innerHTML = "";
  loadingTableData()
  try {
    const data = await getannualclassresult({
      studentclass: appState.classId,
      selectedAcademicSession: appState.selectedSession
    });

    console.log(data)
    const handler = new AnnualClassResultHandler(data);
    appState.results = handler.getStudents();

    if (!appState.results.length) {
      renderNoData();
      return;
    }

    // update badge & table
    const first = appState.results[0];
    console.log(first)
    appState.isPublished = first.published;
    updateResultBadge(first.published);
    renderSubjectList(first.subjects);
    renderTable(appState.results);

  } catch (err) {
    console.error(err);
    showAlert("danger", "Error fetching annual class results");
  } finally {
    setButtonLoading(false);
  }
}

// ------------------------------------------------------
// Render Helpers
// ------------------------------------------------------
function renderNoData() {
  DOM.dataTableBody.innerHTML = `
    <tr><td colspan="14" class="text-center text-muted">
      No Student Records Found
    </td></tr>`;
}

function renderTable(rows) {
  const frag = document.createDocumentFragment();

  rows.forEach((r, i) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${i+1}</td>
      <td class="text-primary">${r.Name||"-"}</td>
      ${
        r.subjects?.length
          ? r.subjects.map(s => `<td>${s.Average||""}</td>`).join("")
          : '<td colspan="3" class="text-center text-muted">No Subjects</td>'
      }
      <td>${r.Total||"-"}</td>
      <td>${r.Average||"-"}</td>
      <td>${r.Grade||"-"}</td>
      <td>${r.Position||"-"}</td>
      <td>${r.Remarks||"-"}</td>
      <td>${r.Verdict||"-"}</td>
    `;
    frag.append(tr);
  });

  DOM.dataTableBody.innerHTML = "";
  DOM.dataTableBody.append(frag);
  new AnnualClassResultDataTable();
}

function renderSubjectList(subjects) {
  DOM.resultsList.innerHTML = subjects.map((s,i) => `
    <li class="list-group-item d-flex justify-content-between align-items-center 
        ${s.published?"text-success":"text-danger"} fw-bold">
      <span>${i+1}.</span> ${s.subject_name}
      <i class="fa-solid fa-${s.published?"check":"xmark"}"></i>
    </li>
  `).join("");
}

function updateResultBadge(isPub) {
  console.log(isPub)
  DOM.resultBadge.classList.toggle("bg-success", isPub);
  DOM.resultBadge.classList.toggle("bg-secondary", !isPub);
  DOM.resultBadge.innerHTML = isPub
    ? `<i class="fa-solid fa-check-circle me-2"></i>Result Published`
    : `<i class="fa-solid fa-circle-xmark me-2"></i>Result Not Published`;
}
