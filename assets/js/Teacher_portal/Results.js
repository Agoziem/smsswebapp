// ------------------------------------------------------
// Imports
// ------------------------------------------------------
import StudentDataHandler from "./utils/StudentResulthandler.js";
import DataTable from "./datatable/StudentResultDatatable.js";
import {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
} from "./utils/serveractions.js";

// ------------------------------------------------------
// DOM References (cached once)
// ------------------------------------------------------
const DOM = {
  form: document.getElementById("getstudentresultform"),
  subjectSelect: null, // wired below
  classInput: null, // wired below
  termSelect: document.getElementById("termSelect"),
  sessionSelect: document.getElementById("academicSessionSelect"),
  examContainer: document.querySelector(".Examinput"),
  modal: document.getElementById("inputStudentResultModal"),
  inputForm: null, // wired below
  publishBtns: document.querySelectorAll(".publishbtn"),
  alertSmall: document.querySelector(".alertcontainer1"),
  alertLarge: document.querySelector(".alertcontainer2"),
  resultBadge: document.getElementById("resultbadge"),
  dataTableBody: document.querySelector("#dataTable tbody"),
};

// wire up form & inputs after DOM.form exists
DOM.subjectSelect = DOM.form.querySelector("select");
DOM.classInput = DOM.form.querySelector("input");
DOM.inputForm = DOM.modal.querySelector("#inputStudentResultform");

// ------------------------------------------------------
// LocalStorage Keys
// ------------------------------------------------------
const LS_KEYS = {
  TERM: "selectedresultTerm",
  SESSION: "selectedresultAcademicSession",
  SUBJECT: "selectedresultsubject",
};

// ------------------------------------------------------
// App State
// ------------------------------------------------------
const appState = {
  studentclass: DOM.classInput.value,
  selectedTerm: null,
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
  const container = window.innerWidth < 768 ? DOM.alertSmall : DOM.alertLarge;
  container.innerHTML = "";
  const a = document.createElement("div");
  a.className = `alert alert-${type} d-flex align-items-center mt-3`;
  a.setAttribute("role", "alert");
  a.innerHTML = `<i class="fa-solid fa-circle-check me-2"></i>${msg}`;
  container.append(a);
  setTimeout(() => (container.innerHTML = ""), 3000);
}

function setButtonLoading(btn, isLoading, text) {
  btn.disabled = isLoading;
  btn.innerHTML = isLoading
    ? `<span class="spinner-border spinner-border-sm me-2" role="status"></span>${text}`
    : text;
}

const loadingTableData = () => {
  DOM.dataTableBody.innerHTML = `
    <tr>
      <td colspan="14" class="text-center">
        <div class="d-flex align-items-center justify-content-center">
          <div class="spinner-border spinner-border-sm me-2" aria-hidden="true"></div>
          <div role="status">Loading Subject Results...</div>
        </div>
      </td>
    </tr>`;
};

// ------------------------------------------------------
// Init: bind & first load
// ------------------------------------------------------
(function init() {
  // form submissions
  DOM.form.addEventListener("submit", (e) => {
    e.preventDefault();
    onFormSubmit();
  });
  DOM.inputForm.addEventListener("submit", (e) => {
    e.preventDefault();
    onStudentSubmit();
  });

  // select changes
  DOM.termSelect.addEventListener("change", onFormSubmit);
  DOM.sessionSelect.addEventListener("change", onFormSubmit);
  DOM.subjectSelect.addEventListener("change", onFormSubmit);

  // publish buttons
  DOM.publishBtns.forEach((btn) =>
    btn.addEventListener("click", onPublishClick)
  );

  // load saved & first fetch
  window.addEventListener("DOMContentLoaded", loadSavedSelections);
  loadSavedSelections();
})();

// ------------------------------------------------------
// Form / selection handlers
// ------------------------------------------------------
function onFormSubmit() {
  appState.selectedTerm = DOM.termSelect.value;
  appState.selectedSession = DOM.sessionSelect.value;
  appState.selectedSubject = DOM.subjectSelect.value;
  saveToLS(LS_KEYS.TERM, appState.selectedTerm);
  saveToLS(LS_KEYS.SESSION, appState.selectedSession);
  saveToLS(LS_KEYS.SUBJECT, appState.selectedSubject);

  updateExamInput();
  if (
    !appState.selectedTerm ||
    !appState.selectedSession ||
    !appState.selectedSubject
  ) {
    return;
  }
  fetchAndRender();
}

function loadSavedSelections() {
  DOM.termSelect.value = readFromLS(LS_KEYS.TERM, DOM.termSelect.value);
  DOM.sessionSelect.value = readFromLS(
    LS_KEYS.SESSION,
    DOM.sessionSelect.value
  );
  DOM.subjectSelect.value = readFromLS(
    LS_KEYS.SUBJECT,
    DOM.subjectSelect.value
  );

  appState.selectedTerm = DOM.termSelect.value;
  appState.selectedSession = DOM.sessionSelect.value;
  appState.selectedSubject = DOM.subjectSelect.value;

  updateExamInput();
  if (
    appState.selectedTerm &&
    appState.selectedSession &&
    appState.selectedSubject
  ) {
    fetchAndRender();
  }
}

function updateExamInput() {
  const max = DOM.subjectSelect.value === "Moral instruction" ? 100 : 60;
  DOM.examContainer.innerHTML = `
    <label for="Exam" class="form-label">Exam Score (${max})</label>
    <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="${max}">
  `;
}

// ------------------------------------------------------
// Modal submission
// ------------------------------------------------------
function onStudentSubmit() {
  console.log("calling the function ")
  const formData = Object.fromEntries(new FormData(DOM.inputForm));
  const payload = {
    selectedClass:appState.studentclass,
    selectedTerm: appState.selectedTerm,
    selectedSession: appState.selectedSession,
    selectedSubject: appState.selectedSubject,
  };

  updatestudentresult(formData, payload, fetchAndRender, showAlert);
  $(DOM.modal).modal("hide");
}

// ------------------------------------------------------
// Fetch & render pipeline
// ------------------------------------------------------
async function fetchAndRender() {
  DOM.publishBtns.forEach((btn) => setButtonLoading(btn, true, "Loading…"));
  loadingTableData();
  try {
    const payload = {
      studentclass: appState.studentclass,
      selectedTerm: appState.selectedTerm,
      selectedAcademicSession: appState.selectedSession,
      studentsubject: appState.selectedSubject,
    };
    const data = await getstudentdata(payload);
    const handler = new StudentDataHandler(data);
    appState.studentResults = handler.getStudents();

    if (!appState.studentResults.length) {
      renderNoData();
      return;
    }

    const first = appState.studentResults[0];
    appState.isPublished = Boolean(first.published);
    updateResultBadge(first.published);
    renderTable(appState.studentResults);
  } catch (err) {
    console.error(err);
    showAlert("danger", "Error fetching results");
  } finally {
    DOM.publishBtns.forEach((btn) => setButtonLoading(
      btn,
      false,
      appState.isPublished ? "Unpublish Result" : "Publish Result"
    ));
  }
}

// ------------------------------------------------------
// Render helpers
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
    tr.setAttribute("data-rowindex", i + 1);
    tr.innerHTML = `
      <td>${i + 1}</td>
      <td class="text-primary text-uppercase">
        <a class="inputdetailsformmodelbtn text-decoration-none" style="cursor:pointer">
          ${r.Name ?? "-"}
        </a>
      </td>
      <td>${r["1sttest"] ?? "-"}</td>
      <td>${r["1stAss"] ?? "-"}</td>
      <td>${r["MidTermTest"] ?? "-"}</td>
      <td>${r["2ndTest"] ?? "-"}</td>
      <td>${r["2ndAss"] ?? "-"}</td>
      <td>${r["CA"] ?? "-"}</td>
      <td>${r["Exam"] ?? "-"}</td>
      <td>${r["Total"] ?? "-"}</td>
      <td>${r["Grade"] ?? "-"}</td>
      <td>${r["Position"] ?? "-"}</td>
      <td>${r["Remarks"] ?? "-"}</td>
      <td>${r["studentID"] ?? "-"}</td>
    `;
    frag.append(tr);
  });
  DOM.dataTableBody.innerHTML = "";
  DOM.dataTableBody.append(frag);
  new DataTable(DOM.modal, DOM.inputForm);
}

// ------------------------------------------------------
// Publish / export handler
// ------------------------------------------------------
async function onPublishClick() {
  if (!appState.studentResults.length) {
    return showAlert("warning", "No result to publish");
  }

  const url = appState.isPublished
    ? "/Teachers_Portal/unpublishstudentresults/"
    : "/Teachers_Portal/submitallstudentresult/";

  DOM.publishBtns.forEach((btn) =>
    setButtonLoading(
      btn,
      true,
      appState.isPublished ? "Unpublishing…" : "Publishing…"
    )
  );

  try {
    await submitallstudentresult(
      url,
      appState.studentResults,
      {
        studentclass: appState.studentclass,
        selectedTerm: appState.selectedTerm,
        selectedAcademicSession: appState.selectedSession,
        studentsubject: appState.selectedSubject,
      },
      showAlert
    );
    appState.isPublished = !appState.isPublished;
    updateResultBadge(appState.isPublished);
  } catch (err) {
    console.error(err);
    showAlert("danger", "Failed to publish results");
  } finally {
    DOM.publishBtns.forEach((btn) =>
      setButtonLoading(
        btn,
        false,
        appState.isPublished ? "Unpublish Result" : "Publish Result"
      )
    );
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
}
