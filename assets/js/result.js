const result_btn = document.getElementById('result_btn');
const spinner = result_btn.querySelector('.spinner-border');

result_btn.addEventListener('click', () => {
    // Show spinner
    spinner.classList.remove('d-none');
    result_btn.disabled = true;
  
    // Call the function that generates the PDF
    myFunction()
      .then(() => {
        // PDF generation is finished, stop spinner
        spinner.classList.add('d-none');
        result_btn.disabled = false;
        // Add your code to start downloading the PDF here
      })
      .catch((error) => {
        // PDF generation encountered an error, display error message
        spinner.classList.add('d-none');
        result_btn.disabled = false;
        result_btn.innerHTML = 'Error: ' + error.message;
      });
  });

  function myFunction(e){
    var element = document.getElementById('container_result');
    var opt =
    {
        margin: 0.2,
        filename: 'Result' + '.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 4 },
        jsPDF: { unit: 'in', format: 'A3', orientation: 'Portrait' }
    };
    // New Promise-based usage:
    return new Promise((resolve, reject) => {
        html2pdf().set(opt).from(element).save()
        .then(() => {
            // PDF generation is complete, resolve the promise
            resolve();
          })
          .catch((error) => {
            // PDF generation encountered an error, reject the promise with the error
            reject(error);
          });
      });
}


