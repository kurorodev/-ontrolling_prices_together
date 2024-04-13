const $loginbutton = document.querySelector('.loginbutton')
const $registerbutton = document.querySelector('.registerbutton')
const $welcome = document.querySelector('.welcome')
const $register = document.querySelector('.register')
const $login = document.querySelector('.login')
const $submit1 = document.querySelector('.submit1')

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

