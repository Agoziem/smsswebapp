import { showSpinner, hideSpinner } from "../../utils/displayspinner.js";

// -----------------------------------------------------------
// getting from the server
// -----------------------------------------------------------
async function getstudentdata(classdata) {
  if (
    classdata.selectedTerm === "" ||
    classdata.selectedAcademicSession === "" ||
    classdata.studentsubject === ""
  ) {
    return;
  }
  // showSpinner("updatesubjectspinner", "subjectbtnmessage", "Loading...");
  const response = await fetch(`/Teachers_Portal/getstudentresults/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  // hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  return data;
}

// ---------------------------------------------------
// function to get Student Annual Result
// ---------------------------------------------------
async function getannualresultdata(classdata) {
  // showSpinner("updatesubjectspinner", "subjectbtnmessage", "Loading...");
  console.log(classdata);
  const response = await fetch(`/Teachers_Portal/annualresultcomputation/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  // hideSpinner("updatesubjectspinner", "subjectbtnmessage", "load Results");
  return data;
}

// -----------------------------------------------------
// Function to get Class Annual Result
// ------------------------------------------------------
async function getannualclassresult(classdata) {
  const response = await fetch(
    `/Teachers_Portal/annualclassresultcomputation/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify(classdata),
    }
  );
  const data = await response.json();
  return data;
}

// -----------------------------------------------------------
// Function to update student result on the server
// -----------------------------------------------------------
function updatestudentresult(
  formDataObject,
  classdata,
  readJsonFromFile,
  displayalert
) {
  if (
    classdata.selectedClass === "" ||
    classdata.selectedTerm === "" ||
    classdata.selectedAcademicSession === "" ||
    classdata.studentsubject === ""
  ) {
    return;
  }
  const fullresultdata = {
    formDataObject,
    classdata,
  };
  fetch(`/Teachers_Portal/updatestudentresults/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(fullresultdata),
  })
    .then((response) => response.json())
    .then((data) => {
      readJsonFromFile();
      const type = "success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

// -----------------------------------------------------------
// Function to submit all students result to the server
// -----------------------------------------------------------
async function submitallstudentresult(url, data, classdata, displayalert) {
  const resulttosubmit = {
    data,
    classdata,
  };
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(resulttosubmit),
  })
    .then((response) => response.json())
    .then((data) => {
      const type = "success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

// -----------------------------------------------------------
// function to get class result
// -----------------------------------------------------------
async function getstudentresult(classdata) {
  const response = await fetch(`/Teachers_Portal/getstudentsubjecttotals/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(classdata),
  });
  const data = await response.json();
  return data;
}

// -----------------------------------------------------------
// Function to publish class result
// -----------------------------------------------------------
async function publishstudentresult(url, data, classdata, displayalert) {
  const fulldata = {
    data,
    classdata,
  };
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(fulldata),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.type === "success") {
        const type = "success";
        const message = data.message;
        displayalert(type, message);
      } else if (data.type === "error") {
        const type = "danger";
        const message = data.message;
        displayalert(type, message);
      } else {
        console.error("Unexpected response type:", data.type);
      }
      return data.type || "error";
    })
    .catch((error) => console.error("Error:", error));
}

export {
  getstudentdata,
  getannualclassresult,
  getannualresultdata,
  updatestudentresult,
  submitallstudentresult,
  getstudentresult,
  publishstudentresult,
};
