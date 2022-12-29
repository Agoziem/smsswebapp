const result_btn = document.getElementById('result_btn');

result_btn.addEventListener('click',
    function (e) {
        var element = document.getElementById('container_result');
        var opt =
        {
            margin: 0.5,
            filename: 'Result' + '.pdf',
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 4 },
            jsPDF: { unit: 'in', format: 'letter', orientation: 'Portrait' }
        };
        // New Promise-based usage:
        html2pdf().set(opt).from(element).save();

    }
)