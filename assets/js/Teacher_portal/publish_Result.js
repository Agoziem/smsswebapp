// imports
import ClassResulthandler from "./utils/ClassResulthandler.js";
import ClassResultDataTable from "./datatable/ClassResultDatatable.js";
import {
  getstudentresult,
  publishstudentresult,
} from "./utils/serveractions.js";

// ------------------------------------------------------
// DOM Elements
// ------------------------------------------------------
const classinput = document.querySelector(".classinput");
const subjectlistinput = document.querySelector(".subjectlist");
const subjectlist = subjectlistinput.value;
const modifiedList = subjectlist.replace(/'/g, '"');
let jsonstring = `${modifiedList}`;
let mainsubjectlist = JSON.parse(jsonstring);
const alertcontainer = document.querySelector(".alertcontainer");
const termSelect = document.getElementById("termSelect");
const academicSessionSelect = document.getElementById("academicSessionSelect");
const publishButton = document.getElementById("publishbtn");

// ------------------------------------------------------
// Event Listeners
// ------------------------------------------------------

publishButton.addEventListener("click", publishResult);

termSelect.addEventListener("change", function () {
  saveSelection();
});

academicSessionSelect.addEventListener("change", function () {
  saveSelection();
});

window.addEventListener("DOMContentLoaded", () => {
  loadSelection();
});

//   ------------------------------------------------------
//   Global Variables
//   ------------------------------------------------------
let ClassResult = [];
let classdata = {
  studentclass: classinput.value,
};
let state;
// ------------------------------------------------------
// Function to save selected values to localStorage
// ------------------------------------------------------
function saveSelection() {
  localStorage.setItem("selectedTerm", termSelect.value);
  localStorage.setItem("selectedAcademicSession", academicSessionSelect.value);
  classdata.selectedTerm = termSelect.value;
  classdata.selectedAcademicSession = academicSessionSelect.value;
  readJsonFromFile();
}

// ------------------------------------------------------
// Function to load saved values from localStorage
// ------------------------------------------------------
function loadSelection() {
  const savedTerm = localStorage.getItem("selectedTerm");
  const savedAcademicSession = localStorage.getItem("selectedAcademicSession");

  if (savedTerm !== null) {
    termSelect.value = savedTerm;
    classdata.selectedTerm = termSelect.value;
  } else {
    classdata.selectedTerm = termSelect.value;
  }

  if (savedAcademicSession !== null) {
    academicSessionSelect.value = savedAcademicSession;
    classdata.selectedAcademicSession = academicSessionSelect.value;
  } else {
    classdata.selectedAcademicSession = academicSessionSelect.value;
  }
  readJsonFromFile();
}

// ------------------------------------------------------
// function to get Student Result
// ------------------------------------------------------
async function readJsonFromFile() {
  try {
    const jsonData = await getstudentresult(classdata);
    const studentHandler = new ClassResulthandler(jsonData);
    const studentsWithCalculatedFields = studentHandler.getStudents();
    ClassResult = studentsWithCalculatedFields;
    updateResultBadge("update", studentsWithCalculatedFields[0]);
    showStudentSubjectResults(studentsWithCalculatedFields[0]);
    populatetable(studentsWithCalculatedFields);
    const dataTable = new ClassResultDataTable();
  } catch (error) {
    console.error("Error reading JSON file:", error);
  }
}

// ------------------------------------------------------
// function to Populate the Table
// ------------------------------------------------------
function populatetable(tabledata) {
  const tbody = document.querySelector("#dataTable").lastElementChild;
  tbody.innerHTML = tabledata
    .map(
      (data, index) =>
        `
        <tr>
            <td>${index + 1}</td>
            <td class="text-primary">${data.Name}</td>
              ${mainsubjectlist
                .map((subject) => `<td>${data[subject].Total}</td>`)
                .join("")}
            <td>${data.Total}</td>
            <td>${data.Ave}</td>
            <td>${data.Grade}</td>
            <td>${data.Position}</td>
            <td>${data.Remarks}</td>
        </tr>`
    )
    .join("");
}

// ------------------------------------------------------------------
// function to publish Result /////////////////////////////////////
// ------------------------------------------------------------------
function publishResult() {
  const url =
    state === "published"
      ? "/Teachers_Portal/unpublishclassresult/"
      : "/Teachers_Portal/publishstudentresult/";
  if (ClassResult.length === 0) {
    displayalert("alert-warning", "No result to publish");
    return;
  }
  const data = ClassResult;
  console.log(data);
  (classdata.studentclass = classinput.value),
    (classdata.selectedTerm = termSelect.value),
    (classdata.selectedAcademicSession = academicSessionSelect.value),
    publishstudentresult(url, data, classdata, displayalert);
  updateResultBadge("setbadge", data[0]);
}

// ------------------------------------------------------------------
// function to display Alert /////////////////////////////////////
// ------------------------------------------------------------------
function displayalert(type, message) {
  const alertdiv = document.createElement("div");
  alertdiv.classList.add(
    "alert",
    `${type}`,
    "d-flex",
    "align-items-center",
    "mt-3"
  );
  alertdiv.setAttribute("role", "alert");
  alertdiv.innerHTML = `
                        <i class="fa-solid fa-circle-check h6 me-2"></i>
                        <div>
                           ${message}
                        </div>
                        `;
  alertcontainer.appendChild(alertdiv);

  setTimeout(() => {
    alertdiv.remove();
  }, 3000);
}

// -----------------------------------------------------------------------
// function to update the result badge and the button test //////////////
// -----------------------------------------------------------------------
function updateResultBadge(type, studentresult) {
  if (type === "setbadge") {
    studentresult.published = !studentresult.published;
  }
  state = studentresult.published ? "published" : "unpublished";
  const badge = document.querySelector("#resultbadge");
  studentresult.published
    ? badge.classList.replace("bg-secondary", "bg-success")
    : badge.classList.replace("bg-success", "bg-secondary");
  badge.innerHTML = studentresult.published
    ? `<i class="fa-solid fa-check-circle me-2"></i>
        <span> Result Published </span>`
    : `<i class="fa-solid fa-circle-xmark me-2"></i>
        <span> Result Not Published </span>`;
  publishButton.innerHTML = studentresult.published
    ? "Unpublish Result"
    : "Publish Result";
}

// -----------------------------------------------------------------------
// function to show the Student Subject Results Published
// -----------------------------------------------------------------------
const showStudentSubjectResults = (student) => {
  const subjectsresultlist = document.querySelector("#resultspublished");
  const studentResult = student;
  const studentResultKeys = Object.keys(studentResult);
  const studentSubjectResult = studentResultKeys.filter((key) => {
    return mainsubjectlist.includes(key);
  });
  const studentSubjectResultData = studentSubjectResult.map(
    (subject, index) => {
      if (studentResult[subject].published) {
        return `<li
            class="list-group-item d-flex justify-content-between align-items-center text-success fw-bold"
          >
          <div>
            <span class="me-2">${index + 1}.</i>
            ${studentResult[subject].subject_name}
          </div>
            <i class="fa-solid fa-check me-3 fw-bold "></i>
          </li>`;
      } else {
        return `<li
            class="list-group-item d-flex justify-content-between align-items-center text-danger fw-bold"
          >
             <div>
                <span class="me-2">${index + 1}.</i>
                ${studentResult[subject].subject_name}
              </div>
            <i class="fa-solid fa-xmark me-3 fw-bold "></i>
          </li>`;
      }
    }
  );
  subjectsresultlist.innerHTML = studentSubjectResultData.join("");
};
