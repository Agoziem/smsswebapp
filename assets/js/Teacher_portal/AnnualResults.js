// ------------------------------------------------------
// Imports
// ------------------------------------------------------
import AnnualResulthandler from "./utils/AnnualResulthandler.js";
import AnnualStudentResultDatatable from "./datatable/AnnualResultDatatable.js";
import {
  getannualresultdata,
  submitallstudentresult,
} from "./utils/serveractions.js";

// ------------------------------------------------------
// DOM References (cached once)
// ------------------------------------------------------
const DOM = {
  form: document.getElementById("getstudentresultform"),
  subjectSelect: null, // filled below
  classInput: null, // filled below
  sessionSelect: document.getElementById("academicSessionSelect"),
  publishBtns: document.querySelectorAll(".publishbtn"),
  alertContainerSmall: document.querySelector(".alertcontainer1"),
  alertContainerLarge: document.querySelector(".alertcontainer2"),
  resultBadge: document.getElementById("resultbadge"),
  dataTableBody: document.querySelector("#dataTable tbody"),
};

// after DOM.form exists, wire up subject & class inputs:
DOM.subjectSelect = DOM.form.querySelector("select");
DOM.classInput = DOM.form.querySelector("input");

// ------------------------------------------------------
// LocalStorage Keys
// ------------------------------------------------------
const LS_KEYS = {
  SESSION: "selectedresultAcademicSession",
  SUBJECT: "selectedresultsubject",
};

// ------------------------------------------------------
// App State
// ------------------------------------------------------
const appState = {
  studentclass: DOM.classInput.value,
  selectedSession: null,
  selectedSubject: null,
  studentResults: [],
  isPublished: false,
};

// ------------------------------------------------------
// Helpers
// ------------------------------------------------------
const saveToLS = (k, v) => localStorage.setItem(k, v);
const readFromLS = (k, def) => localStorage.getItem(k) || def;

function showAlert(type, msg) {
  const container =
    window.innerWidth < 768 ? DOM.alertContainerSmall : DOM.alertContainerLarge;

  container.innerHTML = "";
  const a = document.createElement("div");
  a.className = `alert alert-${type} d-flex align-items-center mt-3`;
  a.setAttribute("role", "alert");
  a.innerHTML = `<i class="fa-solid fa-circle-check me-2"></i>${msg}`;
  container.append(a);
  setTimeout(() => (container.innerHTML = ""), 5000);
}

function setButtonLoading(btn, isLoading) {
  const label = btn.querySelector(".btn-label");
  const spinner = btn.querySelector(".btn-spinner");

  if (isLoading) {
    btn.disabled = true;
    spinner.classList.remove("d-none");
    label.textContent = appState.isPublished ? "Unpublishing…" : "Publishing…";
  } else {
    btn.disabled = false;
    spinner.classList.add("d-none");
    label.textContent = appState.isPublished
      ? "Unpublish Result"
      : "Publish Result";
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
// Init: bind & first load
// ------------------------------------------------------
(function init() {
  // form submit
  DOM.form.addEventListener("submit", (e) => {
    e.preventDefault();
    onFormSubmit();
  });

  // session/subject change
  DOM.sessionSelect.addEventListener("change", onFormSubmit);
  DOM.subjectSelect.addEventListener("change", onFormSubmit);

  // publish buttons
  DOM.publishBtns.forEach((btn) =>
    btn.addEventListener("click", onPublishClick)
  );

  // load saved selections
  window.addEventListener("DOMContentLoaded", loadSavedSelections);

  // first fetch
  loadSavedSelections();
})();

// ------------------------------------------------------
// Form / selection handlers
// ------------------------------------------------------
function onFormSubmit() {
  appState.selectedSession = DOM.sessionSelect.value;
  appState.selectedSubject = DOM.subjectSelect.value;
  saveToLS(LS_KEYS.SESSION, appState.selectedSession);
  saveToLS(LS_KEYS.SUBJECT, appState.selectedSubject);
  if (!appState.selectedSession || !appState.selectedSubject) {
    return;
  }
  fetchAndRender();
}

function loadSavedSelections() {
  const s = readFromLS(LS_KEYS.SESSION, DOM.sessionSelect.value);
  const subj = readFromLS(LS_KEYS.SUBJECT, DOM.subjectSelect.value);

  if (!s || !subj) {
    return;
  }

  DOM.sessionSelect.value = s;
  DOM.subjectSelect.value = subj;

  appState.selectedSession = s;
  appState.selectedSubject = subj;

  fetchAndRender();
}

// ------------------------------------------------------
// Fetch & render pipeline
// ------------------------------------------------------
async function fetchAndRender() {
  clearAlerts();
  // reset state
  appState.studentResults = [];
  appState.isPublished = false;
  
  loadingTableData()

  try {
    const payload = {
      studentclass: appState.studentclass,
      selectedAcademicSession: appState.selectedSession,
      studentsubject: appState.selectedSubject,
    };
    const data = await getannualresultdata(payload);
    console.log(data);
    const handler = new AnnualResulthandler(data);
    appState.studentResults = handler.getStudents();
    if (!appState.studentResults.length) {
      renderNoData();
      return;
    }

    // first row drives badge
    const first = appState.studentResults[0];
    appState.isPublished = Boolean(first.published);
    updateResultBadge(first.published);
    renderTable(appState.studentResults);
  } catch (err) {
    console.error(err);
    showAlert("danger", "Error fetching results");
  } finally {
    DOM.publishBtns.forEach((btn) => setButtonLoading(btn, false));
  }
}

// ------------------------------------------------------
// Render helpers
// ------------------------------------------------------
function renderNoData() {
  DOM.dataTableBody.innerHTML = `
    <tr><td colspan="10" class="text-center text-muted">
      No Student Records Found
    </td></tr>`;
}

function renderTable(rows) {
  const frag = document.createDocumentFragment();
  rows.forEach((r, i) => {
    const tr = document.createElement("tr");
    tr.setAttribute("data-rowindex", i + 1);
    tr.innerHTML = `
      <td>${i + 1}</td>
      <td class="text-primary text-uppercase">
        <a class="inputdetailsformmodelbtn text-decoration-none" style="cursor:pointer">
          ${r.Name || "-"}
        </a>
      </td>
      <td>${r.terms?.["1st Term"] ?? "-"}</td>
      <td>${r.terms?.["2nd Term"] ?? "-"}</td>
      <td>${r.terms?.["3rd Term"] ?? "-"}</td>
      <td>${r.Total ?? "-"}</td>
      <td>${r.Average ?? "-"}</td>
      <td>${r.Grade ?? "-"}</td>
      <td>${r.Position ?? "-"}</td>
      <td>${r.Remarks ?? "-"}</td>
    `;
    frag.append(tr);
  });

  DOM.dataTableBody.innerHTML = "";
  DOM.dataTableBody.append(frag);
  new AnnualStudentResultDatatable();
}

// ------------------------------------------------------
// Publish / unpublish handler
// ------------------------------------------------------
async function onPublishClick(e) {
  if (!appState.studentResults.length) {
    return showAlert("warning", "No result to publish");
  }

  // determine URL
  const url = appState.isPublished
    ? "/Teachers_Portal/unpublishannualresults/"
    : "/Teachers_Portal/publishannualresults/";

  // prepare state to submit
  const payload = {
    studentclass: appState.studentclass,
    selectedAcademicSession: appState.selectedSession,
    studentsubject: appState.selectedSubject,
  };

  // show loader on this button only
  DOM.publishBtns.forEach((btn) => setButtonLoading(btn, true));

  try {
    await submitallstudentresult(
      url,
      appState.studentResults,
      payload,
      showAlert
    );

    DOM.publishBtns.forEach((btn) => setButtonLoading(btn, true));
    await fetchAndRender();
  } catch (err) {
    console.error(err);
    showAlert("danger", "Failed to publish results");
  } finally {
    DOM.publishBtns.forEach((btn) => setButtonLoading(btn, false));
  }
}

// ------------------------------------------------------
// Badge updater
// ------------------------------------------------------
function updateResultBadge(isPublished) {
  DOM.resultBadge.classList.toggle("bg-success", isPublished);
  DOM.resultBadge.classList.toggle("bg-secondary", !isPublished);
  DOM.resultBadge.innerHTML = isPublished
    ? `<i class="fa-solid fa-check-circle me-2"></i>Result Published`
    : `<i class="fa-solid fa-circle-xmark me-2"></i>Result Not Published`;

  // update text on all publish buttons too
  DOM.publishBtns.forEach((btn) => {
    const label = btn.querySelector(".btn-label");
    label.textContent = isPublished ? "Unpublish Result" : "Publish Result";
  });
}

// ------------------------------------------------------
// Utility
// ------------------------------------------------------
function clearAlerts() {
  DOM.alertContainerSmall.innerHTML = "";
  DOM.alertContainerLarge.innerHTML = "";
}
