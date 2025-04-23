function calcularIMC() {
    const peso = parseFloat(document.getElementById('peso').value);
    const altura = parseFloat(document.getElementById('altura').value);
   
    if (isNaN(peso) || isNaN(altura) || altura <= 0) {
      document.getElementById('resultadoIMC').innerText = "Por favor, insira valores válidos.";
      document.getElementById('categoriaIMC').innerText = "";
      return;
    }
   
    const imc = peso / (altura * altura);
    document.getElementById('resultadoIMC').innerText = `Seu IMC é ${imc.toFixed(2)}`;
   
    let categoria = "";
   
    if (imc < 18.5) {
        categoria = "Abaixo do peso";
      } else if (imc < 25.0) {
        categoria = "Peso normal";
      } else if (imc < 30.0) {
        categoria = "Sobrepeso";
      } else if (imc < 35.0) {
        categoria = "Obesidade grau 1";
      } else if (imc < 40.0) {
        categoria = "Obesidade grau 2";
      } else {
        categoria = "Obesidade grau 3";
      }
     
    document.getElementById('categoriaIMC').innerText = `Categoria: ${categoria}`;
  }