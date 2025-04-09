// condicionais 

let idade = 17;

if(idade >= 18){
    console.log("Você é maior de idade...");
}
else {
    console.log("Você é menor de idade....");
}

let media = 7;

if(media >= 7 && media <= 10){
    console.log("Aprovado");
}
else {
    console.log("Reprovado");
}

const IdadeInput = document.getElementById('IdadeInput ');
const verficarIdade = document.getElementById('verficarIdade ');
const resultadoVerificacao = document.getElementById('resultado ');

verficarIdade.addEventListener('click',function(){
    let idadeDigitada = parseInt(IdadeInput.value);
    if(!isNaN(idadeDigitada)){
        if(idadeDigitada >= 18){
            resultadoVerificacao.textContent = 'Você é maior de idade ';
            resultadoVerificacao.style.color = 'blue ';
        }
        else{
            resultadoVerificacao.textContent = 'Você é menor de idade ';
            resultadoVerificacao.style.color = 'red ';
        }
    }
    else{
        resultadoVerificacao.textContent = 'Por favor escreva uma idade válida! ';
        resultadoVerificacao.style.color = 'orange ';
    }
})