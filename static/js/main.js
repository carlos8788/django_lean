// console.log('django.views')
const formulario = document.getElementById('formulario')
console.log(formulario)

formulario.addEventListener('submit', (event) => {
    event.preventDefault()
    alert('Formulario enviado')
    formulario.reset()

})