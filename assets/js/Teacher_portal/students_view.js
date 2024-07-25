import { addStudent, updateStudent, deleteStudents } from './utils/studentApi.js';

// Modal Elements
const addandeditstudentdetailModal = document.querySelector('#AddandeditStudentModal');
const modallabel = addandeditstudentdetailModal.querySelector('#AddandeditStudentModalLabel');
const modalformsubmitbtn = addandeditstudentdetailModal.querySelector('#mainsubmitbtn');
const spinner = document.querySelector('.spinner-border');
const deletestudentModal = document.querySelector('#deletestudentModal');
const deleteallstudentbtn = document.querySelector('#deleteallstudentbtn');
const addandeditstudentdetailform = document.querySelector('#addandeditstudentdetailform');
const studentclass = document.querySelector('#studentclass').value;
const alertcontainer = document.querySelector('.alertcontainer');
const deletestudentbtn = document.querySelector('#deletestudentbtn');
const removestudentsactionbtn = document.querySelector('#removestudentsactionbtn');
const removeallstudentactionbtn = document.querySelector('#removeallstudentactionbtn');
const datatablesSimple = document.getElementById('datatablesSimple');

// DataTable Initialization
let dataTable = new simpleDatatables.DataTable(datatablesSimple);
let rowToRemove;
let rowstoremove = [];
let studentidtoremove = [];
let isedit = false;

// Event Listeners
addandeditstudentdetailform.addEventListener('submit', processform);
datatablesSimple.addEventListener('click', handleTableClick);
deletestudentbtn.addEventListener('click', removestudents);
deleteallstudentbtn.addEventListener('click', removeallstudents);
addandeditstudentdetailModal.addEventListener('hidden.bs.modal', resetModal);

// Handle Table Clicks (Checkbox and Edit)
function handleTableClick(e) {
    const target = e.target;

    if (isCheckboxInCell(target)) {
        handleCheckboxClick(target);
    } else if (isEditLinkInCell(target)) {
        e.preventDefault();
        handleEditClick(target);
    }
}

function isCheckboxInCell(target) {
    return target.tagName === 'INPUT' && target.type === 'checkbox' && target.closest('td');
}

function isEditLinkInCell(target) {
    return target.tagName === 'A' && target.closest('td');
}

function handleCheckboxClick(target) {
    const row = target.closest('tr');
    const studentid = target.value;
    const rowIndex = parseInt(row.dataset.index);

    if (target.checked) {
        addRowToRemove(rowIndex, studentid);
    } else {
        removeRowFromRemoveList(rowIndex, studentid);
    }
}

function handleEditClick(target) {
    rowToRemove = target.closest('tr');
    changeMode(target);
}

/**
 * ADDING FUNCTIONS
 */

// Form Submission Validation
function processform(e) {
    e.preventDefault();

    if (addandeditstudentdetailform.checkValidity() === false) {
        addandeditstudentdetailform.classList.add('was-validated');
    } else {
        addandeditstudentdetailform.classList.remove('was-validated');
        isedit ? submitUpdateFormDetails() : submitFormDetails();
    }
}

// Submit New Student Record
async function submitFormDetails() {
    const studentname = addandeditstudentdetailform.querySelector('#student_name').value;
    const Student_sex = addandeditstudentdetailform.querySelector('#Student_sex').value;

    await submitToServer(studentname, Student_sex);
    spinner.classList.add('.d-none');
    resetFormInputs();
    hideModal();
}

// Submit to Server
async function submitToServer(studentname, Student_sex) {
    spinner.classList.remove('.d-none');
    const studentdata = { studentclass, studentname, Student_sex };

    try {
        const data = await addStudent(studentdata);
        addDetailsToDOM(data.student_ID, data.student_name, data.student_id, data.student_sex);
        displayAlert('alert-success', data.message);
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * UPDATING FUNCTIONS
 */

// Change Mode to Edit
function changeMode(target) {
    isedit = true;
    const tablerow = target.closest('tr');
    tablerow.classList.add('is-edit');

    populateFormForEdit(tablerow);
    updateModalForEdit();
    showModal();
}

// Populate Form for Edit
function populateFormForEdit(tablerow) {
    const studentnameinput = addandeditstudentdetailform.querySelector('#student_name');
    const studentsexinput = addandeditstudentdetailform.querySelector('#Student_sex');

    studentnameinput.value = tablerow.firstElementChild.nextElementSibling.innerText;
    studentsexinput.value = tablerow.lastElementChild.innerText;
}

// Update Modal for Edit
function updateModalForEdit() {
    modallabel.innerText = "Update Student's data";
    modalformsubmitbtn.innerText = 'Update Record';
}

// Update Existing Student Record
function submitUpdateFormDetails() {
    const edittablerow = document.querySelector('tr.is-edit');
    const studentID = edittablerow.firstElementChild.firstElementChild.value;
    const studentname = addandeditstudentdetailform.querySelector('#student_name').value;
    const Student_sex = addandeditstudentdetailform.querySelector('#Student_sex').value;

    submitUpdateToServer(studentID, studentname, Student_sex);
    dataTable.rows.remove(parseInt(rowToRemove.dataset.index));

    resetFormInputs();
    hideModal();
    isedit = false;
    setUIState();
}

// Submit Update to Server
async function submitUpdateToServer(studentID, studentname, Student_sex) {
    const updatestudentdata = { studentID, studentclass, studentname, Student_sex };

    try {
        const data = await updateStudent(updatestudentdata);
        addDetailsToDOM(data.student_ID, data.student_name, data.student_id, data.student_sex);
        displayAlert('alert-success', data.message);
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * DELETING FUNCTIONS
 */

// Remove Students
function removestudents() {
    removeFromServer(studentidtoremove);
    dataTable.rows.remove(rowstoremove);
    dataTable.refresh();
    hideDeleteModal();
    setUIState();
}

// Remove All Students
function removeallstudents() {
    const tablesrows = Array.from(datatablesSimple.firstElementChild.nextElementSibling.children);
    tablesrows.forEach((row) => {
        rowstoremove.push(parseInt(row.dataset.index));
        studentidtoremove.push(row.firstElementChild.firstElementChild.value);
    });

    removeFromServer(studentidtoremove);
    dataTable.rows.remove(rowstoremove);
    dataTable.refresh();
    hideDeleteAllModal();
    setUIState();
}

// Remove from Server
async function removeFromServer(studentidtoremove) {
    try {
        const data = await deleteStudents(studentidtoremove);
        displayAlert('alert-success', data.message);
    } catch (error) {
        console.error('Error:', error);
    }
}

/**
 * UTILITY FUNCTIONS
 */

// Add New Row to DataTable
function addDetailsToDOM(student_ID, studentname, student_id, Student_sex) {
    const newRow = [
        `<input class="form-check-input me-3" type="checkbox" value="${student_ID}" id="selectstudentcheckbox">`,
        `<a class="editstudentinfo text-decoration-none" data-bs-toggle="modal" data-bs-target="#AddandeditStudentModal" style="cursor:pointer">${studentname}</a>`,
        `${student_id}`,
        `${Student_sex}`
    ];
    dataTable.rows.add(newRow);
    dataTable.refresh();
}

// Modal Reset
function resetModal() {
    resetFormInputs();
    addandeditstudentdetailform.classList.remove('was-validated');
    setUIState();
}

// Reset Form Inputs
function resetFormInputs() {
    addandeditstudentdetailform.querySelector('#student_name').value = '';
    addandeditstudentdetailform.querySelector('#Student_sex').value = '';
}

// Show Modal
function showModal() {
    $(addandeditstudentdetailModal).modal('show');
}

// Hide Modals
function hideModal() {
    $(addandeditstudentdetailModal).modal('hide');
}

function hideDeleteModal() {
    $(deletestudentModal).modal('hide');
}

function hideDeleteAllModal() {
    $(document.querySelector('#deleteallstudentModal')).modal('hide');
}

// Display Alert
function displayAlert(type, message) {
    const alertdiv = document.createElement('div');
    alertdiv.classList.add('alert', type, 'd-flex', 'align-items-center', 'mt-3');
    alertdiv.setAttribute('role', 'alert');
    alertdiv.innerHTML = `
        <i class="fa-solid fa-circle-check h6 me-2"></i>
        <div>${message}</div>
    `;
    alertcontainer.appendChild(alertdiv);

    setTimeout(() => {
        alertdiv.remove();
    }, 3000);
}

// Update UI State
function setUIState() {
    resetModalLabelAndButton();
    handleNoEntriesFound();
    resetSelections();
}

// Reset Modal Label and Button
function resetModalLabelAndButton() {
    modallabel.innerText = "Add Student Record";
    modalformsubmitbtn.innerText = 'Add Student';
}

// Handle No Entries Found
function handleNoEntriesFound() {
    const tablesrows = Array.from(datatablesSimple.lastElementChild.children);
    const noEntriesFound = tablesrows.length === 1 && tablesrows[0].firstElementChild.innerText === 'No entries found';

    if (noEntriesFound) {
        removestudentsactionbtn.classList.add('d-none');
        removeallstudentactionbtn.classList.add('d-none');
    } else {
        removestudentsactionbtn.classList.remove('d-none');
        removeallstudentactionbtn.classList.remove('d-none');
    }
}

// Reset Selections
function resetSelections() {
    rowstoremove = [];
    studentidtoremove = [];
    const tablesrows = Array.from(datatablesSimple.lastElementChild.children);
    tablesrows.forEach((row) => {
        row.classList.remove('is-edit');
        row.firstElementChild.firstElementChild.checked = false;
    });
}

// add Row to Remove List
function addRowToRemove(rowIndex, studentid) {
    if (rowstoremove.indexOf(rowIndex) === -1 && studentidtoremove.indexOf(studentid) === -1) {
        rowstoremove.push(rowIndex);
        studentidtoremove.push(studentid);
    }
}

// Remove Row from Remove List
function removeRowFromRemoveList(rowIndex, studentid) {
    const indexToRemove = rowstoremove.indexOf(rowIndex);
    const idToRemove = studentidtoremove.indexOf(studentid);

    if (indexToRemove !== -1) {
        rowstoremove.splice(indexToRemove, 1);
        studentidtoremove.splice(idToRemove, 1);
    }
}
