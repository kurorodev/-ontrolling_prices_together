import saveFile from "/app/src/script/connector.js"

const $submitfile = document.querySelector('.submitfile')
const $modelimage = document.getElementById('modelimage')

$submitfile.addEventListener('click',async () => {
    const file = $modelimage.files[0]
    const formData = new FormData();
    formData.append('file', file)

    try{
        const resoult = JSON.parse(await saveFile(formData))
        alert(resoult)
    }
    catch(error){
        alert('Ошибка загрузки файла ' + error)
    }
})