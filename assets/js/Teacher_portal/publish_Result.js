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
const alertcontainer = document.querySelector(".alertcontainer");
const termSelect = document.getElementById("termSelect");
const academicSessionSelect = document.getElementById("academicSessionSelect");
const publishButton = document.getElementById("publishbtn");
const subjectsresultlist = document.querySelector("#resultspublished");
const resultbadge = document.querySelector("#resultbadge");

// Parse subject list
const subjectlist = document.querySelector(".subjectlist").value;
const mainsubjectlist = JSON.parse(subjectlist.replace(/'/g, '"'));


// ------------------------------------------------------
// Event Listeners
// ------------------------------------------------------
publishButton.addEventListener("click", publishResult);
termSelect.addEventListener("change", saveSelection);
academicSessionSelect.addEventListener("change", saveSelection);
window.addEventListener("DOMContentLoaded", loadSelection);


// ------------------------------------------------------
// Global Variables
// ------------------------------------------------------
let ClassResult = [];
let state; // Published or unpublished
const classdata = {
  studentclass: classinput.value,
};

// ------------------------------------------------------
// Function to save selected values to localStorage
// ------------------------------------------------------
function saveSelection() {
  const { value: term } = termSelect;
  const { value: session } = academicSessionSelect;

  localStorage.setItem("selectedTerm", term);
  localStorage.setItem("selectedAcademicSession", session);

  classdata.selectedTerm = term;
  classdata.selectedAcademicSession = session;

  readJsonFromFile();
}

// ------------------------------------------------------
// Function to load saved values from localStorage
// ------------------------------------------------------
function loadSelection() {
  termSelect.value = localStorage.getItem("selectedTerm") || termSelect.value;
  academicSessionSelect.value =
    localStorage.getItem("selectedAcademicSession") || academicSessionSelect.value;

  classdata.selectedTerm = termSelect.value;
  classdata.selectedAcademicSession = academicSessionSelect.value;

  readJsonFromFile();
}


// ------------------------------------------------------
// Function to fetch and handle student results
// ------------------------------------------------------
async function readJsonFromFile() {
  try {
    const jsonData = await getstudentresult(classdata);
    const studentHandler = new ClassResulthandler(jsonData);
    ClassResult = studentHandler.getStudents();

    if (ClassResult.length) {
      updateResultBadge("update", ClassResult[0]);
      showStudentSubjectResults(ClassResult[0]);
      populatetable(ClassResult);
      console.log(ClassResult)
      new ClassResultDataTable(); // Initialize DataTable
    } else {
      displayalert("alert-warning", "No Student Records Found");
    }
  } catch (error) {
    console.error("Error fetching student results:", error);
  }
}

// ------------------------------------------------------
// Function to populate the table
// ------------------------------------------------------
function populatetable(tableData) {
  const tbody = document.querySelector("#dataTable").lastElementChild;

  if (!Array.isArray(tableData) || !tableData.length) {
    tbody.innerHTML = `
      <tr>
        <td colspan="10" class="text-center text-muted">No Student Records Found</td>
      </tr>`;
    return;
  }

  tbody.innerHTML = tableData
    .map(
      (data, index) =>
        `<tr>
          <td scope="row">${index + 1}</td>
          <td class="text-primary">${data.Name ?? "-"}</td>
          ${data.subjects
            ?.map(
              (subject) =>
                `<td>${
                  subject.Total && subject.Total !== "-" ? subject.Total : ""
                }</td>`
            )
            .join("") || ""}
          <td>${data.Total ?? "-"}</td>
          <td>${data.Ave ?? "-"}</td>
          <td>${data.Grade ?? "-"}</td>
          <td>${data.Position ?? "-"}</td>
          <td>${data.Remarks ?? "-"}</td>
        </tr>`
    )
    .join("");
}


// ------------------------------------------------------
// Function to publish or unpublish results
// ------------------------------------------------------
function publishResult() {
  if (!ClassResult.length) {
    displayalert("alert-warning", "No result to publish");
    return;
  }

  const url =
    state === "published"
      ? "/Teachers_Portal/unpublishclassresult/"
      : "/Teachers_Portal/publishstudentresult/";

  const classdata = {
    studentclass: classinput.value,
    selectedTerm: termSelect.value,
    selectedAcademicSession: academicSessionSelect.value,
  };

  publishstudentresult(url, ClassResult, classdata, displayalert).then(() => {
    location.reload();
  });
}


// ------------------------------------------------------
// Function to display alert messages
// ------------------------------------------------------
function displayalert(type, message) {
  const alertdiv = document.createElement("div");
  alertdiv.className = `alert ${type} d-flex align-items-center mt-3`;
  alertdiv.setAttribute("role", "alert");
  alertdiv.innerHTML = `
    <i class="fa-solid fa-circle-check h6 me-2"></i>
    <div>${message}</div>`;
  alertcontainer.appendChild(alertdiv);

  setTimeout(() => alertdiv.remove(), 3000);
}


// ------------------------------------------------------
// Function to update the result badge
// ------------------------------------------------------
function updateResultBadge(type, studentresult) {
  if (!("published" in studentresult)) return;
  if (type === "setbadge") {
    studentresult.published = !studentresult.published;
  }

  state = studentresult.published ? "published" : "unpublished";
  const isPublished = studentresult.published;

  resultbadge.classList.replace(
    isPublished ? "bg-secondary" : "bg-success",
    isPublished ? "bg-success" : "bg-secondary"
  );
  resultbadge.innerHTML = isPublished
    ? `<i class="fa-solid fa-check-circle me-2"></i><span> Result Published </span>`
    : `<i class="fa-solid fa-circle-xmark me-2"></i><span> Result Not Published </span>`;
  publishButton.innerHTML = isPublished ? "Unpublish Result" : "Publish Result";
}

// ------------------------------------------------------
// Function to show published subjects
// ------------------------------------------------------
function showStudentSubjectResults(student) {
  subjectsresultlist.innerHTML = student.subjects
    .map((subject, index) => {
      const isPublished = subject.published;
      return `<li class="list-group-item d-flex justify-content-between align-items-center ${
        isPublished ? "text-success" : "text-danger"
      } fw-bold">
        <div><span class="me-2">${index + 1}.</span>${subject.subject_name}</div>
        <i class="fa-solid fa-${isPublished ? "check" : "xmark"} me-3 fw-bold"></i>
      </li>`;
    })
    .join("");
}
