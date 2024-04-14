export function getShopInfo(){
    alert('aaaaaa')
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/get_shop_info", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    return new Promise(resolve =>{
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                let result = xhr.responseText
                return resolve(result)
            }
            if (this.status != 200) {
                alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
            }}
    }
)}

export function registerNewUser(jsonData){
    let xhr = new XMLHttpRequest();
    alert(1)
    xhr.open("POST", "/register", true);
    alert(2)
    xhr.setRequestHeader("Content-Type", "application/json");
    alert(3)
    xhr.send(jsonData)
    return new Promise(resolve => {
        alert(5)
        xhr.onreadystatechange = function(){
        if (xhr.readyState === 4 && xhr.status === 200) {
            const result = xhr.responseText
            // alert(result)
            return resolve(result)
        }
        if (this.status != 200) {
            alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
        }}
    })
}

export function LoginIn(jsonData){
    let xhr = new XMLHttpRequest();
    alert(1)
    xhr.open("POST", "/login", true);
    alert(2)
    xhr.setRequestHeader("Content-Type", "application/json");
    alert(3)
    xhr.send(jsonData)
    return new Promise(resolve => {
        alert(5)
        xhr.onreadystatechange = function(){
        if (xhr.readyState === 4 && xhr.status === 200) {
            const result = xhr.responseText
            // alert(result)
            return resolve(result)
        }
        if (this.status != 200) {
            alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
        }}
    })
}

export function saveFile(formData){
    let xhr = new XMLHttpRequest();
    alert(1)
    xhr.open("POST", "/save_file", true);
    alert(2)
    // xhr.setRequestHeader("Content-Type", "application/document");
    alert(formData)
    xhr.send(formData)
    return new Promise(resolve => {
        alert(5)
        xhr.onreadystatechange = function(){
        if (xhr.readyState === 4 && xhr.status === 200) {
            const result = xhr.responseText
            return resolve(result)
        }
        if (this.status != 200) {
            alert('Ошибка: '+(this.status ? this.statusText : 'запрос не удался'))
        }}
    })
}