// ------------------------------------------------------
// Imports
// ------------------------------------------------------
import ClassResulthandler from "./utils/ClassResulthandler.js";
import ClassResultDataTable from "./datatable/ClassResultDatatable.js";
import {
  getstudentresult,
  publishstudentresult,
} from "./utils/serveractions.js";

// ------------------------------------------------------
// DOM References (cached once)
// ------------------------------------------------------
const DOM = {
  classInput: document.querySelector(".classinput"),
  alertContainer: document.querySelector(".alertcontainer"),
  termSelect: document.getElementById("termSelect"),
  sessionSelect: document.getElementById("academicSessionSelect"),
  publishBtn: document.getElementById("publishbtn"),
  resultsList: document.querySelector("#resultspublished"),
  resultBadge: document.querySelector("#resultbadge"),
  dataTableBody: document.querySelector("#dataTable tbody"),
  subjectListInput: document.querySelector(".subjectlist"),
};

// ------------------------------------------------------
// LocalStorage Keys
// ------------------------------------------------------
const LS_KEYS = {
  TERM: "selectedTerm",
  SESSION: "selectedAcademicSession",
};

// ------------------------------------------------------
// App State
// ------------------------------------------------------
const appState = {
  classId: DOM.classInput.value,
  selectedTerm: null,
  selectedSession: null,
  results: [],
  isPublished: false,
};

// ------------------------------------------------------
// Helpers: localStorage
// ------------------------------------------------------
const saveToLS = (key, value) => localStorage.setItem(key, value);
const readFromLS = (key, fallback) => localStorage.getItem(key) || fallback;

// ------------------------------------------------------
// Init: load selections & bind events
// ------------------------------------------------------
(function init() {
  DOM.publishBtn.addEventListener("click", onPublishClick);
  DOM.termSelect.addEventListener("change", onSelectionChange);
  DOM.sessionSelect.addEventListener("change", onSelectionChange);
  window.addEventListener("DOMContentLoaded", loadSavedSelection);

  // parse once
  const rawList = DOM.subjectListInput?.value ?? "[]";
  appState.subjectsMeta = JSON.parse(rawList.replace(/'/g, '"'));

  // first fetch
  loadSavedSelection();
})();


const loadingTableData = () => {
  DOM.dataTableBody.innerHTML = `
    <tr>
      <td colspan="14" class="text-center">
        <div class="d-flex align-items-center justify-content-center">
          <div class="spinner-border spinner-border-sm me-2" aria-hidden="true">
          </div>
          <div role="status">Loading Class Results...</div>
        </div>
      </td>
    </tr>`;
};

// ------------------------------------------------------
// Event Handlers
// ------------------------------------------------------
function onSelectionChange() {
  appState.selectedTerm = DOM.termSelect.value;
  appState.selectedSession = DOM.sessionSelect.value;

  saveToLS(LS_KEYS.TERM, appState.selectedTerm);
  saveToLS(LS_KEYS.SESSION, appState.selectedSession);

  DOM.publishBtn.disabled = true
  DOM.publishBtn.innerHTML = `<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
    <span role="status">fetching...</span>
  `;
  fetchAndRender();
}

function loadSavedSelection() {
  DOM.termSelect.value = readFromLS(LS_KEYS.TERM, DOM.termSelect.value);
  DOM.sessionSelect.value = readFromLS(
    LS_KEYS.SESSION,
    DOM.sessionSelect.value
  );

  appState.selectedTerm = DOM.termSelect.value;
  appState.selectedSession = DOM.sessionSelect.value;

  fetchAndRender();
}

async function onPublishClick() {
  if (!appState.results.length) {
    return showAlert("warning", "No result to publish");
  }

  // button inner content
  DOM.publishBtn.disabled = true;
  DOM.publishBtn.innerHTML = `<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
    <span role="status">${
      appState.isPublished ? "unpublishing" : "publishing"
    }...</span>
  `;
  const url = appState.isPublished
    ? "/Teachers_Portal/unpublishclassresult/"
    : "/Teachers_Portal/publishstudentresult/";

  try {
    await publishstudentresult(
      url,
      appState.results,
      {
        studentclass: appState.classId,
        selectedTerm: appState.selectedTerm,
        selectedAcademicSession: appState.selectedSession,
      },
      showAlert
    );

    // refetch on success
    fetchAndRender();
  } catch (err) {
    console.error(err);
    showAlert("danger", "Failed to publish results");
    DOM.publishBtn.disabled = false;
  }
}

// ------------------------------------------------------
// Fetch + Render Pipeline
// ------------------------------------------------------
async function fetchAndRender() {
  clearAlert();
  loadingTableData()
  try {
    const payload = {
      studentclass: appState.classId,
      selectedTerm: appState.selectedTerm,
      selectedAcademicSession: appState.selectedSession,
    };
    const jsonData = await getstudentresult(payload);
    const handler = new ClassResulthandler(jsonData);
    appState.results = handler.getStudents();

    if (!appState.results.length) {
      renderNoData();
      return;
    }

    updateResultBadge(appState.results[0].published);
    renderSubjectList(appState.results[0].subjects);
    renderTable(appState.results);
    DOM.publishBtn.disabled = false;
  } catch (err) {
    console.error(err);
    showAlert("danger", "Error fetching student results");
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

function renderTable(dataArray) {
  const frag = document.createDocumentFragment();
  dataArray.forEach((row, idx) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${idx + 1}</td>
      <td class="text-primary">${row.Name || "-"}</td>
      ${row.subjects.map((s) => `<td>${s.Total || ""}</td>`).join("")}
      <td>${row.Total || "-"}</td>
      <td>${row.Ave || "-"}</td>
      <td>${row.Grade || "-"}</td>
      <td>${row.Position || "-"}</td>
      <td>${row.Remarks || "-"}</td>`;
    frag.appendChild(tr);
  });

  DOM.dataTableBody.innerHTML = "";
  DOM.dataTableBody.appendChild(frag);

  // initialize DataTable plugin
  new ClassResultDataTable();
}

function renderSubjectList(subjects) {
  DOM.resultsList.innerHTML = subjects
    .map(
      (s, i) => `
    <li class="list-group-item d-flex justify-content-between align-items-center 
      ${s.published ? "text-success" : "text-danger"} fw-bold">
      <span>${i + 1}.</span> ${s.subject_name}
      <i class="fa-solid fa-${s.published ? "check" : "xmark"}"></i>
    </li>`
    )
    .join("");
}

function updateResultBadge(isPublished) {
  appState.isPublished = isPublished;
  DOM.resultBadge.classList.toggle("bg-success", isPublished);
  DOM.resultBadge.classList.toggle("bg-secondary", !isPublished);
  DOM.resultBadge.innerHTML = isPublished
    ? `<i class="fa-solid fa-check-circle me-2"></i>Result Published`
    : `<i class="fa-solid fa-circle-xmark me-2"></i>Result Not Published`;
  DOM.publishBtn.innerHTML = isPublished
    ? `Unpublish Result <i class="fa-solid fa-right-from-bracket ms-2"></i>`
    : `Publish Result <i class="fa-solid fa-right-from-bracket ms-2"></i>`;
}

function showAlert(type, message) {
  clearAlert();
  const alertDiv = document.createElement("div");
  alertDiv.className = `alert alert-${type} d-flex align-items-center mt-3`;
  alertDiv.setAttribute("role", "alert");
  alertDiv.innerHTML = `<i class="fa-solid fa-circle-check h6 me-2"></i>${message}`;
  DOM.alertContainer.appendChild(alertDiv);
  setTimeout(clearAlert, 3000);
}

function clearAlert() {
  DOM.alertContainer.innerHTML = "";
}
