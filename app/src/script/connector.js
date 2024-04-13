function getShopInfo(){
    alert('aaaaaa')
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/request", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            let x = xhr.responseText
            alert(x)
        }
        if (this.status != 200) {
            alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
        }}
    xhr.send()
}

function registerNewUser(){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/register_new_user", true);
    xhr.setRequestHeader("Content-Type", "register/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert('YES')
        }
        if (this.status != 200) {
            alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
        }}
    xhr.send(JSON.stringify({userdata:{username:$username.value,userpassword:$password.value}}))
}

export default registerNewUser