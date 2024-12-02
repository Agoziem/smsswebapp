// -----------------------------------------------------------
// Imports
// -----------------------------------------------------------
import StudentDataHandler from "./utils/StudentResulthandler.js";
import DataTable from "./datatable/StudentResultDatatable.js";
import {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
} from "./utils/serveractions.js";

// -----------------------------------------------------------
// DOM Elements
// -----------------------------------------------------------
const inputStudentResultModal = document.querySelector(
  "#inputStudentResultModal"
);
const inputform = inputStudentResultModal.querySelector(
  "#inputStudentResultform"
);
const getstudentresultform = document.querySelector("#getstudentresultform");
const subjectselect = getstudentresultform.querySelector("select");
const classinput = getstudentresultform.querySelector("input");
const termSelect = document.getElementById("termSelect");
const Examforminput = document.querySelector(".Examinput");
const academicSessionSelect = document.getElementById("academicSessionSelect");
const alertcontainer1 = document.querySelector(".alertcontainer1"); // for small screen
const alertcontainer2 = document.querySelector(".alertcontainer2"); // for large screen

// -----------------------------------------------------------
// Global States
// -----------------------------------------------------------
let classdata = { studentclass: classinput.value };
let studentResult = [];
let state;

// -----------------------------------------------------------
// Event Listeners
// -----------------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
  getstudentresultform.addEventListener("submit", handleFormSubmit);
  inputform.addEventListener("submit", handleStudentResultSubmit);
  document.querySelectorAll(".publishbtn").forEach((btn) => {
    btn.addEventListener("click", exportTableToJSON);
  });

  loadsavedSelection();
});

// -----------------------------------------------------------
// Event Handlers
// -----------------------------------------------------------
function handleFormSubmit(event) {
  event.preventDefault();
  saveformSelections();
}

function handleStudentResultSubmit(event) {
  event.preventDefault();
  const formData = new FormData(inputform);
  const formDataObject = Object.fromEntries(formData);

  classdata = {
    ...classdata,
    studentsubject: subjectselect.value,
    selectedTerm: termSelect.value,
    selectedAcademicSession: academicSessionSelect.value,
  };

  updatestudentresult(
    formDataObject,
    classdata,
    readJsonFromFile,
    displayalert
  );
  $(inputStudentResultModal).modal("hide");
}

// -----------------------------------------------------------
// Form Management
// -----------------------------------------------------------
function saveformSelections() {
  localStorage.setItem("selectedresultTerm", termSelect.value);
  localStorage.setItem(
    "selectedresultAcademicSession",
    academicSessionSelect.value
  );
  localStorage.setItem("selectedresultsubject", subjectselect.value);

  classdata = {
    ...classdata,
    selectedTerm: termSelect.value,
    selectedAcademicSession: academicSessionSelect.value,
    studentsubject: subjectselect.value,
  };

  updateExamInput();
  readJsonFromFile();
}

function loadsavedSelection() {
  termSelect.value =
    localStorage.getItem("selectedresultTerm") || termSelect.value;
  academicSessionSelect.value =
    localStorage.getItem("selectedresultAcademicSession") ||
    academicSessionSelect.value;
  subjectselect.value =
    localStorage.getItem("selectedresultsubject") || subjectselect.value;

  classdata = {
    ...classdata,
    selectedTerm: termSelect.value,
    selectedAcademicSession: academicSessionSelect.value,
    studentsubject: subjectselect.value,
  };

  updateExamInput();
  readJsonFromFile();
}

function updateExamInput() {
  const isMoralInstruction = subjectselect.value === "Moral instruction";
  Examforminput.innerHTML = `
    <label for="Exam" class="form-label">Exam Score (${
      isMoralInstruction ? 100 : 60
    })</label>
    <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="${
      isMoralInstruction ? 100 : 60
    }">
  `;
}

// -----------------------------------------------------------
// Data Management
// -----------------------------------------------------------
async function readJsonFromFile() {
  try {
    const jsonData = await getstudentdata(classdata);
    const studentHandler = new StudentDataHandler(jsonData);
    const studentsWithCalculatedFields = studentHandler.getStudents();

    studentResult = studentsWithCalculatedFields;
    updateResultBadge("update", studentsWithCalculatedFields[0]);
    populatetable(studentsWithCalculatedFields);
    new DataTable(inputStudentResultModal, inputform);
  } catch (error) {
    console.error("Error reading JSON file:", error);
  }
}

// -----------------------------------------------------------
// Table Management
// -----------------------------------------------------------
function populatetable(tableData) {
  const tbody = document.querySelector("#dataTable").lastElementChild;
  tbody.innerHTML = tableData.length
    ? tableData
        .map(
          (data, index) => `
          <tr data-rowindex="${index + 1}">
              <td scope="row">${index + 1}</td>
              <td class="text-primary text-uppercase">
                <a class="inputdetailsformmodelbtn text-decoration-none" style="cursor:pointer">
                  ${data.Name ?? "-"}
                </a>
              </td>
              <td>${data["1sttest"] ?? "-"}</td>
              <td>${data["1stAss"] ?? "-"}</td>
              <td>${data["MidTermTest"] ?? "-"}</td>
              <td>${data["2ndTest"] ?? "-"}</td>
              <td>${data["2ndAss"] ?? "-"}</td>
              <td>${data["CA"] ?? "-"}</td>
              <td>${data["Exam"] ?? "-"}</td>
              <td>${data["Total"] ?? "-"}</td>
              <td>${data["Grade"] ?? "-"}</td>
              <td>${data["Position"] ?? "-"}</td>
              <td>${data["Remarks"] ?? "-"}</td>
              <td>${data["studentID"] ?? "-"}</td>
          </tr>`
        )
        .join("")
    : `<tr data-rowindex="1">
          <td colspan="14" class="text-center">No Student Records Found</td>
       </tr>`;
}

// -----------------------------------------------------------
// Result Submission
// -----------------------------------------------------------
function exportTableToJSON() {
  const url =
    state === "published"
      ? "/Teachers_Portal/unpublishstudentresults/"
      : "/Teachers_Portal/submitallstudentresult/";

  submitallstudentresult(url, studentResult, classdata, displayalert).then(()=>{
    location.reload();
  })
}

// -----------------------------------------------------------
// Notifications
// -----------------------------------------------------------
function displayalert(type, message) {
  const alertdiv = document.createElement("div");
  alertdiv.classList.add("alert", type, "d-flex", "align-items-center", "mt-3");
  alertdiv.setAttribute("role", "alert");
  alertdiv.innerHTML = `
    <i class="fa-solid fa-circle-check h6 me-2"></i>
    <div>${message}</div>
  `;

  (window.innerWidth < 768 ? alertcontainer1 : alertcontainer2).appendChild(
    alertdiv
  );
  setTimeout(() => alertdiv.remove(), 3000);
}

// -----------------------------------------------------------
// Result Badge Update
// -----------------------------------------------------------
function updateResultBadge(type, studentresult) {
  if (type === "setbadge") studentresult.published = !studentresult.published;

  state = studentresult.published ? "published" : "unpublished";
  const badge = document.querySelector("#resultbadge");

  badge.classList.toggle("bg-success", studentresult.published);
  badge.classList.toggle("bg-secondary", !studentresult.published);
  badge.innerHTML = studentresult.published
    ? `<i class="fa-solid fa-check-circle me-2"></i> Result Published`
    : `<i class="fa-solid fa-circle-plus me-2"></i> Result Not Published`;

  document.querySelectorAll(".publishbtn").forEach((btn) => {
    btn.innerHTML = studentresult.published
      ? `UnPublish Result <i class="fa-solid fa-right-from-bracket ms-2"></i>`
      : `Publish Result <i class='fa-solid fa-left-from-bracket ms-2'></i>`;
  });
}
