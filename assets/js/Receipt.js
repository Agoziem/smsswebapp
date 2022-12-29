
const reciept_btn = document.getElementById('reciept_btn');


reciept_btn.addEventListener('click',
    function (e) {
        var element = document.getElementById('container_result2');
        var opt =
        {
            margin: 0.5,
            filename: 'Payment Receipt' + '.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 4 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'Portrait' }
        };
        // New Promise-based usage:
        html2pdf().set(opt).from(element).save();

    }
)