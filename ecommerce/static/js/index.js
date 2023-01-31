// signup page validation

const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
const repeatPassword = document.getElementById('repeatPassword');
const checkbox = document.getElementById('checkbox');
const emailValidation = document.getElementById('emailValidation');
const passwordStrnth = document.getElementById('passwordStrnth');
const matchPassword = document.getElementById('matchPassword');
const sumbitBtn = document.getElementById('submit');

form.addEventListener('submit', (e) => {
    e.preventDefault();
});

email.addEventListener('keypress', (event) => {
    let emailValue = event.target.value;
    if(emailValue) {
        
    } else{
        emailValidation.innerHTML = 'email can\'t be empty';
    }
});
