// Parallax
$(document).ready(function(){
    $(window).scroll(function (event){
        var s = $(this).scrollTop();
        var w = $(this).outerWidth();
        var h = $('.content').outerHeight();
        var h_b = $('.parallax').outerHeight();
        var p = s/h*100;
        var p_b = s/h_b*100;
        var o = 1-1/100*p_b;

        var z_1 = 1+(w/10000*p_b);
        $('.parallax__fog').css('transform', 'scale('+z_1+')');
        $('.parallax__fog').css('opacity', o);

        var z_2 = 1+(w/5000000*p);
        $('.parallax__mountain_1').css('transform', 'scale('+z_2+')');

        var hr = w/2000*p_b;
        var z_3 = 1+(w*0.000005*p_b);
        $('.parallax__mountain_2').css('transform', 'translate3d('+hr+'px,0,0) scale('+z_3+')');

        var hr_2 = w/1500*p_b;
        var z_4 = 1+(w*0.00001*p_b);
        $('.parallax__mountain_3').css('transform', 'translate3d('+hr_2+'px,0,0) scale('+z_4+')');
    });
});

// Login Form
var loginEmail = document.querySelector(".form-style[name='login-email']");
var loginPassword = document.querySelector(".form-style[name='login-password']");

function validateEmail(email) {
    var re = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i;
    return re.test(email);
}

function validatePassword(password) {
    return password.length >= 8;
}

function validateLoginForm(e) {
    var loginEmailValue = loginEmail.value;
    var loginPasswordValue = loginPassword.value;
    var hasErrors = false;
    if (!validateEmail(loginEmailValue)) {
        alert("Пожалуйста, введите корректный email-адрес");
        hasErrors = true;
    }
    if (!validatePassword(loginPasswordValue)) {
        alert("Пароль должен быть не меньше 8 символов");
        hasErrors = true;
    }
    if (!hasErrors && loginEmailValue === "admin@gmail.com" && loginPasswordValue === "admin1234") {
        window.location.href = "shop.html"; // Перенаправление на новую страницу
    } else if (hasErrors) {
        e.preventDefault();
    }
}
document.getElementById("loginButton").addEventListener("click", function(event) {
    event.preventDefault();
    validateLoginForm(event);
});

// Register Form
var registerFullname = document.querySelector(".form-style[name='register-fullname']");
var registerPhone = document.querySelector(".form-style[name='register-phone']");
var registerEmail = document.querySelector(".form-style[name='register-email']");
var registerPassword = document.querySelector(".form-style[name='register-password']");

function validateFullname(fullname) {
    return fullname.length > 0;
}

function validatePhone(phone) {
    var re = /^\+?\d{10,15}$/;
    return re.test(phone);
}

function validateRegisterForm(e) {
    var registerFullnameValue = registerFullname.value;
    var registerPhoneValue = registerPhone.value;
    var registerEmailValue = registerEmail.value;
    var registerPasswordValue = registerPassword.value;
    var hasErrors = false;
    if (!validateFullname(registerFullnameValue)) {
        alert("Пожалуйста, введите ваше полное имя");
        hasErrors = true;
    }
    if (!validatePhone(registerPhoneValue)) {
        alert("Пожалуйста, введите корректный номер телефона");
        hasErrors = true;
    }
    if (!validateEmail(registerEmailValue)) {
        alert("Пожалуйста, введите корректный email-адрес");
        hasErrors = true;
    }
    if (!validatePassword(registerPasswordValue)) {
        alert("Пароль должен быть не меньше 8 символов");
        hasErrors = true;
    }
    if (hasErrors) {
        e.preventDefault();
    }
}

document.getElementById("registerButton").addEventListener("click", function(event) {
    event.preventDefault();
    validateRegisterForm(event);
});