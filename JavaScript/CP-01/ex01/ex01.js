var agora = new Date()
var hora = agora.getHours()

if (hora > 6 && hora < 12) {
    document.getElementById('saudacao').innerText = 'BOM DIA! '
} else if (hora > 12 && hora < 18 ) {
    document.getElementById('saudacao').innerText = 'BOM TARDE! '
} else {
    document.getElementById('saudacao').innerText = 'BOM NOITE! '
}