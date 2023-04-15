
 mapboxgl.accessToken = 'pk.eyJ1Ijoib2tmcyIsImEiOiJjbDFodTNjMG8wNnh6M2tycHN0ZDhzamYzIn0.H1VgtMiBAjkMEe7GXREzvA';
 var map = new mapboxgl.Map({
   container: 'map',
   style: 'mapbox://styles/mapbox/streets-v11',
   center: [6.800465, 6.124938],
   zoom: 12,
 });

// const contactForm = document.querySelector('#contact_form');

// contactForm .addEventListener('submit', function (e) {
//     e.preventDefault();
//     submitcontactformdata()
//   })
  
//   function submitcontactformdata() {
//     var userformdata = {
//       'name': contactForm.Name.value,
//       'email': contactForm.email.value,
//       'message': contactForm.message.value,
//     }
  
//     var url = '/submit_contact_form/'
//     fetch(url, {
//       method: 'POST',
//       headers: {
//         'content-Type': 'application/json',
//         'X-CSRFToken': csrftoken
//       },
//       body: JSON.stringify({ 'userformdata': userformdata })
//     })
//       .then((response) => {
//         return response.json();
//       })
//       .then((data) => {
//       contactForm.Name.value = ''
//       contactForm.email.value = ''
//       contactForm.message.value = ''
//       //   document.getElementById('contact_form_alert').style.display = "block"
//       //   document.getElementById('contact_form_alert').style.opacity = "1"
//       console.log('Data :', data)
//       })
//   }
  
  // New Form Js

  document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var form = this;
    var btn = form.querySelector('#submit-btn');

    // Change button text to spinner icon
    btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> submitting...';
    var userformdata = {
            'name': form.Name.value,
            'email': form.email.value,
            'message': form.message.value,
          }
    // Send Ajax request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/submit_contact_form/' );
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    xhr.onload = function() {
      if (xhr.status === 200) {
        // Change button text back to original
        btn.innerHTML = 'Send Message';

        // Display success alert
        var successAlert = document.querySelector('.alert-success');
        successAlert.style.display = 'flex';
        setTimeout(function() {
          successAlert.style.display = 'none';
        }, 3000);
        form.reset();
        
      } else {
        // Change button text back to original
        btn.innerHTML = 'Send Message';

        // Display error alert
        var errorAlert = document.querySelector('.alert-danger');
        errorAlert.style.display = 'flex';
        setTimeout(function() {
          errorAlert.style.display = 'none';
        }, 3000);
      }
    };
    xhr.send(JSON.stringify({ userformdata: userformdata }));
  });

  // Close the Alert Box at the Here Section

const notice = document.querySelector('.notice');
const closeBtn = notice.querySelector('.close-btn');

closeBtn.addEventListener('click', () => {
  notice.style.display = 'none';
});