const datatablesSimple = document.getElementById('datatablesSimple');
let dataTable = new simpleDatatables.DataTable(datatablesSimple);
let columns = dataTable.columns;
let isedit = false;
const columntoggles = document.querySelectorAll('.columntoggle');
const inputStudentResultModal = document.querySelector('#inputStudentResultModal')
const inputStudentResultform = document.querySelector('#inputStudentResultform')
const getstudentresultform = document.querySelector('#getstudentresultform');
const subjectselect = getstudentresultform.querySelector('select');
const classinput = getstudentresultform.querySelector('input');


function setUIState() {
    isedit = false
    // const tablesrows = Array.from(datatablesSimple.lastElementChild.children);
    // if (tablesrows.length === 1 && tablesrows[0].firstElementChild.innerText === 'No entries found') {
    //     return;
    // } else {
    //     tablesrows.forEach((row) => {
    //         row.classList.remove('is-edit');
    //         const checkbox = row.firstElementChild.firstElementChild;
    //         checkbox.checked = false;
    //     })
    // }
}


window.addEventListener('DOMContentLoaded', () => {
    const studentsubject = subjectselect.options[subjectselect.selectedIndex].value;
    const studentclass = classinput.value
    getstudentdata(studentsubject, studentclass)
})

function cleartabledata() {
    let rowstoremove = []
    for (let i = 1; i <= dataTable.totalPages; i++) {
        dataTable.page(i);
        const tablesrows = Array.from(datatablesSimple.lastElementChild.children);
        tablesrows.forEach((row) => {
            const rowindex = parseInt(row.dataset.index);
            rowstoremove.push(rowindex)
        })
    }
    dataTable.rows.remove(rowstoremove)
    dataTable.refresh()
    rowstoremove = []
}
getstudentresultform.addEventListener('submit', (e) => {
    e.preventDefault()
    cleartabledata()
    const studentsubject = subjectselect.options[subjectselect.selectedIndex].value;
    const studentclass = classinput.value
    getstudentdata(studentsubject, studentclass)
})

columntoggles.forEach((columntoggle) => {
    columntoggle.addEventListener('click', hidecolumn);
})

function hidecolumn(e) {
    if (e.target.type === 'checkbox') {
        const columnindex = parseInt(e.target.value)
        if (e.target.checked) {
            columns.hide([columnindex]);
        } else {
            columns.show([columnindex])
        }
    }
}

datatablesSimple.addEventListener('click', function (e) {
    const target = e.target;
    // Check if the click is on an <a> element inside a <td>
    if (target.tagName === 'A' && target.closest('td')) {
        e.preventDefault();
        rowToRemove = target.closest('tr');
        changemode(target)
    }
});

// set the mode to isedit = true and peforming some actions
function changemode(target) {
    isedit = true;
    const tablerow = target.closest('tr')

    const tabledata = Array.from(tablerow.children)

    const studentnameinput = inputStudentResultform.querySelector('#student_name')
    studentnameinput.value = tabledata[0].innerText

    const FirstTest = inputStudentResultform.querySelector('#FirstTest')
    FirstTest.value = tabledata[1].innerText ? tabledata[1].innerText : '-'

    const FirstAss = inputStudentResultform.querySelector('#FirstAss')
    FirstAss.value = tabledata[2].innerText

    const MidTermTest = inputStudentResultform.querySelector('#MidTermTest')
    MidTermTest.value = tabledata[3].innerText

    const SecondAss = inputStudentResultform.querySelector('#SecondAss')
    SecondAss.value = tabledata[4].innerText

    const SecondTest = inputStudentResultform.querySelector('#SecondTest')
    SecondTest.value = tabledata[5].innerText

    const CA = inputStudentResultform.querySelector('#CA')
    CA.value = tabledata[6].innerText

    const Exam = inputStudentResultform.querySelector('#Exam')
    Exam.value = tabledata[7].innerText

    const Total = inputStudentResultform.querySelector('#Total')
    Total.value = tabledata[8].innerText

    const Grade = inputStudentResultform.querySelector('#Grade')
    Grade.value = tabledata[9].innerText

    // const SubjectPosition = inputStudentResultform.querySelector('#SubjectPosition')
    // SubjectPosition.value = tabledata[10].innerText

    const Remark = inputStudentResultform.querySelector('#Remark')
    Remark.value = tabledata[10].innerText

    $(inputStudentResultModal).modal('show');
}

inputStudentResultform.addEventListener('submit',processinputform)

function processinputform(e) {
    e.preventDefault();
    const subject = subjectselect.options[subjectselect.selectedIndex].value;
    const studentnameinput = inputStudentResultform.querySelector('#student_name')
    const FirstTest = inputStudentResultform.querySelector('#FirstTest')
    const FirstAss = inputStudentResultform.querySelector('#FirstAss')
    const MidTermTest = inputStudentResultform.querySelector('#MidTermTest')
    const SecondAss = inputStudentResultform.querySelector('#SecondAss')
    const SecondTest = inputStudentResultform.querySelector('#SecondTest')
    const Exam = inputStudentResultform.querySelector('#Exam')

    
    const studentdata = {
        subject: subject,
        student_class: classinput.value,
        studentname: studentnameinput.value,
        FirstTest: FirstTest.value ? FirstTest.value : "0",
        FirstAss: FirstAss.value ? FirstAss.value : "0",
        MidTermTest: MidTermTest.value ? MidTermTest.value : "0",
        SecondAss: SecondAss.value ? SecondAss.value : "0", 
        SecondTest: SecondTest.value ? SecondTest.value : "0",
        Exam: Exam.value ? Exam.value : "0",
    }

    cleartabledata()
    updatestudentresult(studentdata)
    setUIState()

    $(inputStudentResultModal).modal('hide');
}


// getting from the server
function getstudentdata(subject,Class) {
    fetch(`/Teachers_Portal/${subject}/${Class}/getstudentresults`)
        .then(response => response.json())
        .then(data => {
            dataTable.insert(data);
        })
        .catch(error => console.error('Error:', error));
}

function updatestudentresult(studenteresultdata) {
    fetch(`/Teachers_Portal/updatestudentresults`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(studenteresultdata)
    })
        .then(response => response.json())
        .then(data => {
            dataTable.insert(data);
            dataTable.refresh()
        })
        .catch(error => console.error('Error:', error));
}

inputStudentResultModal.addEventListener('hidden.bs.modal', function () {
    setUIState()
});
