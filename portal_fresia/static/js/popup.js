var myModal = document.getElementById('myModal')
var myInput = document.getElementById('myInput')

myModal.addEventListener('shown.coreui.modal', function () {
  myInput.focus()
})