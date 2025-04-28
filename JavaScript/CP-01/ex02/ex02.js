function calcular() {
    const peso = parseFloat(document.getElementById('peso').value);
    const altura = parseFloat(document.getElementById('altura').value);

    const res = peso / (altura * altura)
    document.getElementById('Resultado').innerHTML = `Seu IMC é ${res.toFixed(2)}`;

    let categoria = '';
    if (res < 18.5) {
        categoria = 'Abaixo do peso';
    } else if (18.5 < res < 24.9) {
        categoria = 'Peso normal';
    } else if ( 25 < res < 29.9) {
        categoria = 'Sobrepeso';
    } else if (30 < res < 34.9) {
        categoria = 'Obesidade grau 1';
    } else {
        categoria = 'Obesidade grau 2';
    }

    document.getElementById('categoria').innerHTML = `Sua categoria é ${categoria}`;

}
