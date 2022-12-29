
 mapboxgl.accessToken = 'pk.eyJ1Ijoib2tmcyIsImEiOiJjbDFodTNjMG8wNnh6M2tycHN0ZDhzamYzIn0.H1VgtMiBAjkMEe7GXREzvA';
 var map = new mapboxgl.Map({
   container: 'map',
   style: 'mapbox://styles/mapbox/streets-v11',
   center: [6.800465, 6.124938],
   zoom: 12,
 });

const contactForm = document.querySelector('#contact_form');

contactForm .addEventListener('submit', function (e) {
    e.preventDefault();
    submitcontactformdata()
  })
  
  function submitcontactformdata() {
    var userformdata = {
      'name': contactForm.Name.value,
      'email': contactForm.email.value,
      'message': contactForm.message.value,
    }
  
    var url = '/submit_contact_form/'
    fetch(url, {
      method: 'POST',
      headers: {
        'content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify({ 'userformdata': userformdata })
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
      contactForm.Name.value = ''
      contactForm.email.value = ''
      contactForm.message.value = ''
      //   document.getElementById('contact_form_alert').style.display = "block"
      //   document.getElementById('contact_form_alert').style.opacity = "1"
      console.log('Data :', data)
      })
  }
  