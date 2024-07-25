// imports
import StudentDataHandler from "./utils/StudentResulthandler.js";
import DataTable from "./datatable/StudentResultDatatable.js";
import {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
} from "./utils/serveractions.js";

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
const rowcheckboxes = document.querySelector(".rowgroup");
document.querySelectorAll(".publishbtn").forEach((btn) => {
  btn.addEventListener("click", exportTableToJSON);
});
const alertcontainer1 = document.querySelector(".alertcontainer1"); // for small screen
const alertcontainer2 = document.querySelector(".alertcontainer2"); // for large screen

// -----------------------------------------------------------
// Global States
// -----------------------------------------------------------
let classdata = {
  studentclass: classinput.value,
};
let studentResult = [];
let state;

// -----------------------------------------------------------
// event listener to save form selections on submit
// -----------------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
  getstudentresultform.addEventListener("submit", (e) => {
    e.preventDefault();
    saveformSelections();
  });
});

document.addEventListener("DOMContentLoaded", () => {
  loadsavedSelection();
});

// -----------------------------------------------------------
// Function to update student result on form submit
// -----------------------------------------------------------
document.addEventListener("DOMContentLoaded", () => {
  document
    .getElementById("inputStudentResultform")
    .addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(inputform);
      const formDataObject = {};
      formData.forEach((value, key) => {
        formDataObject[key] = value;
      });
      classdata.studentsubject =
        subjectselect.options[subjectselect.selectedIndex].value;
      (classdata.selectedTerm = termSelect.value),
        (classdata.selectedAcademicSession = academicSessionSelect.value),
        updatestudentresult(
          formDataObject,
          classdata,
          readJsonFromFile,
          displayalert
        );
      $(inputStudentResultModal).modal("hide");
    });
});

// -----------------------------------------------------------
// Function to save selected values to localStorage
// -----------------------------------------------------------
function saveformSelections() {
  localStorage.setItem("selectedresultTerm", termSelect.value);
  localStorage.setItem(
    "selectedresultAcademicSession",
    academicSessionSelect.value
  );
  localStorage.setItem("selectedresultsubject", subjectselect.value);
  classdata.selectedTerm = termSelect.value;
  classdata.selectedAcademicSession = academicSessionSelect.value;
  classdata.studentsubject =
    subjectselect.options[subjectselect.selectedIndex].value;

  // check whether the subject is Moral to adjust the Exam input Restrictions
  if (subjectselect.value === "Moral instruction") {
    Examforminput.innerHTML = "";
    Examforminput.innerHTML = `
                            <label for="Exam" class="form-label">Exam Score (100)</label>
                            <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="100">`;
  } else {
    Examforminput.innerHTML = "";
    Examforminput.innerHTML = `
                            <label for="Exam" class="form-label">Exam Score (60)</label>
                            <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="60">`;
  }
  readJsonFromFile();
}

// -----------------------------------------------------------
// Function to load saved values from localStorage
// -----------------------------------------------------------
function loadsavedSelection() {
  const savedTerm = localStorage.getItem("selectedresultTerm");
  const savedAcademicSession = localStorage.getItem(
    "selectedresultAcademicSession"
  );
  const savedsubject = localStorage.getItem("selectedresultsubject");

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

  if (savedsubject !== null) {
    subjectselect.value = savedsubject;
    classdata.studentsubject = subjectselect.value;
  } else {
    classdata.studentsubject = subjectselect.value;
  }

  // check whether the subject is Moral to adjust the Exam input Restrictions
  if (subjectselect.value === "Moral instruction") {
    Examforminput.innerHTML = "";
    Examforminput.innerHTML = `
                            <label for="Exam" class="form-label">Exam Score (100)</label>
                            <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="100">`;
  } else {
    Examforminput.innerHTML = "";
    Examforminput.innerHTML = `
                            <label for="Exam" class="form-label">Exam Score (60)</label>
                            <input type="number" class="form-control" id="Exam" name="Exam" min="0" max="60">`;
  }

  readJsonFromFile();
}

// -----------------------------------------------------------
// Function to read JSON data from Server
// -----------------------------------------------------------
async function readJsonFromFile() {
  try {
    const jsonData = await getstudentdata(classdata);
    const studentHandler = new StudentDataHandler(jsonData);
    const studentsWithCalculatedFields = studentHandler.getStudents();
    //   populaterowcheckbox(studentsWithCalculatedFields)
    studentResult = studentsWithCalculatedFields;
    updateResultBadge("update", studentsWithCalculatedFields[0]);
    populatetable(studentsWithCalculatedFields);
    const dataTable = new DataTable(inputStudentResultModal, inputform);
  } catch (error) {
    console.error("Error reading JSON file:", error);
  }
}

// -----------------------------------------------------------
// Function to populate the Table rows
// -----------------------------------------------------------
function populatetable(tabledata) {
  const tbody = document.querySelector("#dataTable").lastElementChild;
  tbody.innerHTML = tabledata
    .map(
      (data, index) => `
        <tr data-rowindex='${index + 1}'>
            <td>${index + 1}</td>
            <td class="text-primary text-uppercase"><a class="inputdetailsformmodelbtn text-decoration-none" style="cursor:pointer">${
              data.Name
            }</a></td>
            <td>${data["1sttest"]}</td>
            <td>${data["1stAss"]}</td>
            <td>${data["MidTermTest"]}</td>
            <td>${data["2ndTest"]}</td>
            <td>${data["2ndAss"]}</td>
            <td>${data["CA"] || "-"}</td>
            <td>${data["Exam"]}</td> 
            <td>${data["Total"] || "-"}</td>
            <td>${data["Grade"] || "-"}</td>
            <td>${data["Position"] || "-"}</td>
            <td>${data["Remarks"] || "-"}</td>
            <td>${data["studentID"] || "-"}</td>
        </tr>`
    )
    .join("");
}

// -----------------------------------------------------------
// Function to export Table data to JSON
// -----------------------------------------------------------
function exportTableToJSON() {
  const url =
    state === "published"
      ? "/Teachers_Portal/unpublishstudentresults/"
      : "/Teachers_Portal/submitallstudentresult/";
  const datatosubmit = studentResult;
  classdata.studentsubject =
    subjectselect.options[subjectselect.selectedIndex].value;
  classdata.studentclass = classinput.value;
  (classdata.selectedTerm = termSelect.value),
    (classdata.selectedAcademicSession = academicSessionSelect.value),
    submitallstudentresult(url, datatosubmit, classdata, displayalert);
  updateResultBadge("setbadge", datatosubmit[0]);
}

// --------------------------------
// display alert message
// --------------------------------
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
  if (window.innerWidth < 768) {
    alertcontainer1.appendChild(alertdiv);
  } else {
    alertcontainer2.appendChild(alertdiv);
  }

  setTimeout(() => {
    alertdiv.remove();
  }, 3000);
}

// ------------------------------------------------------------------------------------------------
// function to update the result badge
// ------------------------------------------------------------------------------------------------
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
       Result Published`
    : `<i class="fa-solid fa-circle-plus me-2"></i>
       Result Not Published`;

  document.querySelectorAll(".publishbtn").forEach((btn) => {
    btn.innerHTML = studentresult.published
      ? `UnPublish Result <i class="fa-solid fa-right-from-bracket ms-2"></i>`
      : `Publish Result <i class='fa-solid fa-left-from-bracket ms-2'></i>`;
  });
}
