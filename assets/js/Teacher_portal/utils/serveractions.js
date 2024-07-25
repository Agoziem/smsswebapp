// -----------------------------------------------------------
// getting from the server
// -----------------------------------------------------------
async function getstudentdata(classdata) {
  const response = await fetch(`/Teachers_Portal/getstudentresults/`, {
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
// Function to update student result on the server
// -----------------------------------------------------------
function updatestudentresult(
  formDataObject,
  classdata,
  readJsonFromFile,
  displayalert
) {
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
      const type = "alert-success";
      const message = data;
      displayalert(type, message);
    })
    .catch((error) => console.error("Error:", error));
}

// -----------------------------------------------------------
// Function to submit all students result to the server
// -----------------------------------------------------------
function submitallstudentresult(url, data, classdata, displayalert) {
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
      const type = "alert-success";
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
function publishstudentresult(url, data, classdata, displayalert) {
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
        const type = "alert-success";
        const message = data.message;
        displayalert(type, message);
      } else if (data.type === "error") {
        const type = "alert-danger";
        const message = data.message;
        displayalert(type, message);
      } else {
        console.error("Unexpected response type:", data.type);
      }
    })
    .catch((error) => console.error("Error:", error));
}


export {
  getstudentdata,
  updatestudentresult,
  submitallstudentresult,
  getstudentresult,
  publishstudentresult,
};
