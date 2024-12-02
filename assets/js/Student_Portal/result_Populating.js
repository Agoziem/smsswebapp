const classSelect = document.getElementById("class");
const sessionSelect = document.getElementById("sessionSelect");
const StudentsSelect = document.getElementById("Students");
const userInput = document.querySelector("#studentId");

userInput.addEventListener("input", processinput);
function processinput() {
  // Get the input element
  const processedValue = userInput.value.toLowerCase().replace(/\s/g, "");
  userInput.value = processedValue;
}

sessionSelect?.addEventListener("input", populateClass)
classSelect?.addEventListener("input", populateClass);

function populateClass() {
  const classname = classSelect.value;
  const sessionID = sessionSelect.value;
  if (classname && sessionID) {
    fetch(`/Result_portal/${classname}/${sessionID}`)
      .then((response) => response.json())
      .then((data) => {
        StudentsSelect.innerHTML = "";
        data.forEach((student) => {
          const option = document.createElement("option");
          option.value = student.student_name;
          option.textContent = student.student_name;
          StudentsSelect.appendChild(option);
        });
      })
      .catch((error) => console.error(error));
  } else {
    StudentsSelect.innerHTML = "";
  }
}
