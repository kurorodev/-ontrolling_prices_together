import registerNewUser from '/app/src/script/connector.js'

const $loginbutton = document.querySelector('.loginbutton')
const $registerbutton = document.querySelector('.registerbutton')
const $welcome = document.querySelector('.welcome')
const $register = document.querySelector('.register')
const $login = document.querySelector('.login')
const $submitregister = document.querySelector('.submitregister')
const $regemail = document.querySelector('.regemail')
const $regephonenum = document.querySelector('.regphonenum')
const $regpassword = document.querySelector('.regpassword')

let backpage = []
let currentpage = $welcome

$loginbutton.addEventListener('click',()=>{
    currentpage = $login
    backpage.push($welcome)

    const currentbackpage = backpage.slice(-1)[0]

    let anim = currentbackpage.animate({opacity: 0}, 300)
        anim.onfinish = ev => {
            currentbackpage.style.display = 'none'
            currentpage.style.display = 'block'
        }
})

$registerbutton.addEventListener('click',()=>{
    currentpage = $register
    backpage.push($welcome)

    const currentbackpage = backpage.slice(-1)[0]

    let anim = currentbackpage.animate({opacity: 0}, 300)
        anim.onfinish = ev => {
            currentbackpage.style.display = 'none'
            currentpage.style.display = 'block'
        }
})

$submitregister.addEventListener('click',()=>{
    const emailRegex = new RegExp('([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')
    const phoneNumRegex = new RegExp('(\\+7|8)[\\s(]*\\d{3}[)\\s]*\\d{3}[\\s-]?\\d{2}[\\s-]?\\d{2}')
    const passwordRegex = new RegExp('(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}')

    const boolRegexedEmail = emailRegex.test($regemail.value)
    const boolRegexedPhoneNum = phoneNumRegex.test($regephonenum.value)
    const boolRegexedPassword = passwordRegex.test($regpassword.value)

    alert('Проверка')

    if(boolRegexedEmail && boolRegexedPhoneNum && boolRegexedPassword){
        const userData = JSON.stringify({userdata:{email: $regemail.value, phone_number:$regephonenum.value, password: $regpassword.value}})
        const tryRegister = registerNewUser(userData)
    }
    else{
        alert('Какое-то поле заполненно неверно')
    }
})

function returnBackPage() {
    const currentbackpage = backpage.slice(-1)[0]
    let anim = currentpage.animate({opacity: 0}, 300)
        anim.onfinish = ev => {
            currentpage.style.display = 'none'
            currentbackpage.style.display = 'block'
            currentpage = currentbackpage
        }
    backpage.pop()
}



