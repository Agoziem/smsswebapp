
// Hambuger trigger Code 
const hambuger = document.querySelector('.hambuger');
const navMenu = document.querySelector('.nav-bar-sm');

hambuger.addEventListener('click', () => {
  hambuger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll("#nav-item-m-sm").forEach(n =>
  n.addEventListener("click", () => {
    hambuger.classList.remove("active");
    navMenu.classList.remove("active");
  }));


  // Navbar dropdown Code for large Screen //////////////////////////


const dropdowntrigger = document.querySelector('.dropdowntrigger');
const dropdownlist = document.querySelector('.dropdownlist');

if (user !== 'AnonymousUser') {
  dropdowntrigger.addEventListener('click', () => {
    dropdownlist.classList.toggle("active");
    dropdownbtn.classList.toggle("active");
  })
}

  // Navbar dropdown Code for Small Screen //////////////////////////

var trigger = document.getElementsByClassName('trigger');
for (i = 0; i < trigger.length; i++) {
  var countn = trigger[i].getAttribute("data-count")
  const dropdownmenu = document.querySelector(`#drop-down-menu${countn}`);
  const dropdownbtn = document.querySelector(`#dropdownbtn${countn}`);
  trigger[i].addEventListener('click', () => {
    dropdownmenu.classList.toggle("active");
    dropdownbtn.classList.toggle("active");

})
}
//function myFunction() {
//     // Declare variables
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById('myInput');
//     filter = input.value.toUpperCase();
//     ul = document.getElementById("myUL");
//     li = ul.getElementsByTagName('li');
  
  
//     // Loop through all list items, and hide those who don't match the search query
//     for (i = 0; i < li.length; i++) {
//       a = li[i].getElementsByTagName("a")[0];
//       txtValue = a.textContent || a.innerText;
//       if (txtValue.toUpperCase().indexOf(filter) > -1) {
//         li[i].style.display = '';
  
//       } else {
//         li[i].style.display = 'none';
//       }
//     }
//   }
  
//   function myFunctionb() {
//     // Declare variables
//     var input, filter, ul, li, a, i, txtValue;
//     input = document.getElementById('myInput');
//     filter = input.value.toUpperCase();
//     ul = document.getElementById("myUL");
//     li = ul.getElementsByTagName('li');
  
  
//     // Loop through all list items, and hide those who don't match the search query
//     for (i = 0; i < li.length; i++) {
//       a = li[i].getElementsByTagName("a")[0];
//       txtValue = a.textContent || a.innerText;
//       if (txtValue.toUpperCase().indexOf(filter) > -1) {
//         li[i].style.display = '';
  
//       } else {
//         li[i].style.display = 'none';
//       }
//     }
//   }



// const contactformTrigger = document.querySelector('#contactform_trigger');

// contactformTrigger.addEventListener('click', () => {
//     contactForm.classList.remove("d-none");
//     contactformTrigger.style.display='none';
// })


// Get all elements with class="closebtn"
// var close = document.getElementsByClassName("closebtn");
//       var i;
//       for (i = 0; i < close.length; i++) {
//         close[i].onclick = function () {
//           var div = this.parentElement;
//           div.style.opacity = "0";
//           setTimeout(function () { div.style.display = "none"; }, 600);
//         }
//       }


var subform = document.getElementById('sub_form');

subform.addEventListener('submit', function (e) {
  e.preventDefault()
  submitsubformdata()
})

function submitsubformdata() {
  var userdata = {
    'email': subform.email.value,
  }

  var url = '/submit_sub_form/'
  fetch(url, {
    method: 'POST',
    headers: {
      'content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ 'userdata': userdata })
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      subform.email.value = ''
    //   document.getElementById('sub_form_alert1').style.display = "block"
    //   document.getElementById('sub_form_alert1').style.opacity = "1"
      console.log('Data :', data)
    })
}


var swiper = new Swiper(".slider_content", {

    spaceBetween: 25,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    centerSlide: 'true',
    fade: "true",
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      520: {
        slidesPerView: 2,
      },
      950: {
        slidesPerView: 3,
      },
    },
  });
  
