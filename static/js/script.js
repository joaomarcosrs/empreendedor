const myurl = JSON.parse(document.getElementById('url_').innerHTML);
const inputSearchRegistros = document.querySelector('.form-search input');
const tableRegistros = document.querySelectorAll('.table tbody tr');

function VisualizarRegistros() {
    
    window.location.href = myurl + '/home/registros';
}

function Atendimento() {
    window.Location.href = myurl + '/home/registrar_atendimento';
}

const filterRegs = (containsText, inputValue, returnMatchedRegs) => containsText
    .filter(regs => {
        const matchedRegs = regs.textContent.toUpperCase().includes(inputValue);
        return returnMatchedRegs ? matchedRegs : !matchedRegs
    })

const manipulateClasses = (containsText, classRegAdd, classRegRemove) => {
    containsText.forEach(regs => {
        regs.classList.remove(classRegRemove);
        regs.classList.add(classRegAdd);    
    })
}

const hideRegs = (containsText, inputValue) => {
    const regsToHide = filterRegs(containsText, inputValue, false)
    manipulateClasses(regsToHide, 'hidden', 'table-row')

}

const showRegs = (containsText, inputValue) => {
    const regsToShow = filterRegs(containsText, inputValue, true)
    manipulateClasses(regsToShow, 'table-row', 'hidden')
}

inputSearchRegistros.addEventListener('input', event => {
    const inputValue = event.target.value.trim().toUpperCase();
    const containsText = Array.from(tableRegistros)

    hideRegs(containsText, inputValue);
    showRegs(containsText, inputValue);

});