import {getShopInfo, saveFile} from "/app/src/script/connector.js"

let shopdict;
const $submitfile = document.querySelector('.submitfile')
const $modelimage = document.getElementById('modelimage')

window.addEventListener('copy', async() => {
    alert('aaaa')
    const request = JSON.parse(await getShopInfo())
    console.log(request)
});

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

$('.input-file input[type=file]').on('change', function(){
	let file = this.files[0];
	$(this).next().html(file.name);
});

//$options = document.getElementById("options")//.innerHTML = '<option value="Вариант 3"> bbbbbbb/option>'

//$options.insertAdjacentHTML('beforeend','<option value="Вариант 3"> bbbbbbb/option>')
