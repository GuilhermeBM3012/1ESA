console.log('Script externo rodando para o DOM '); // Document Object Model 

const tituloElemento = document.getElementById('tituloDinamico'); // seleciona o elemento <h2> pelo seu id
tituloElemento.textContent = 'Texto alterado pelo JavaScript'; // alterando o texto do h2 
tituloElemento.style.color = 'green'; // alterando a cor do texto

const botaoElemento = document.getElementById('meuBotão'); // seleciona o botao pelo seu id
botaoElemento.addEventListener('click', function(){
    alert('Botão foi clicado!! ');
})



