const openModalButton = document.getElementById("modal1")
const closeModalButton = document.getElementById("modal2")
const overlay = document.getElementById('overlay')


const modal = document.getElementById("modal")
openModalButton.addEventListener('click', () => {
        
 
    openModal(modal)
})

closeModalButton.addEventListener('click', () => {
        
        closeModal(modal)
    })


function openModal (modal){
    if (modal == null) return
    modal.classList.add('active')
    
    overlay.classList.add('active')
}

function closeModal (modal){
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}