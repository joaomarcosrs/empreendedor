const myurl = JSON.parse(document.getElementById('url_').innerHTML);

function VisualizarRegistros() {
    
    window.location.href = myurl + '/home/registros';
}

function Atendimento() {
    window.Location.href = myurl + '/home/registrar_atendimento';
}

