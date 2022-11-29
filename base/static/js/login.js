document.addEventListener('DOMContentLoaded', () => {
    let eye = document.getElementById('show-password');
    let password_field = document.getElementById('password-field');
    eye.addEventListener('click', (e) => {
        
        if(eye.classList.contains('fa-eye'))
        {
            eye.classList.add('fa-eye-slash');
            eye.classList.remove('fa-eye');
            password_field.type = "text";
        }

        else{
            eye.classList.add('fa-eye');
            eye.classList.remove('fa-eye-slash');
            password_field.type = "password";
        }
    })
    



})