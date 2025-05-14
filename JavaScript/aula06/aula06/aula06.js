// Obter referências aos botões do tema e da pág
const botaoClaro = document.getElementById('temaClaro');
const botaoEscuro = document.getElementById('temaEscuro');
const body = document.body; 

// Define uma chave para armazenar a preferência do tema no LocalStorage
const chaveTema = 'preferenciaTema';

// Função para aplicar um tema específico ao corpo da pág
function aplicarTema(tema){
    body.classList.remove('tema-claro', 'tema-escuro'); // remove qualquer coisa q tenha no temaClaro e temaEscuro
    body.classList.add(`Tema - ${tema}`); // add o tema escolhido

    // Salva a preferência do tema no LocalStorage
    localStorage.setItem(chaveTema, tema);
}

// Verificar se já existe uma preferência de tema salva no LocalStorage ao carregar a pág
const temaSalvo = localStorage.getItem(chaveTema);

if(temaSalvo){
    aplicarTema(temaSalvo)
}else{
    aplicarTema('claro');
}

// Add um evento de click ao botão 'Claro'
botaoClaro.addEventListener('click', ()=> {
    // quando o botão for clicado, chama a função para aplicar o tema claro
    aplicarTema('claro');
});
// Add um evento de click ao botão 'Escuro'
botaoEscuro.addEventListener('click', ()=> {
    // quando o botão for clicado, chama a função para aplicar o tema escuro
    aplicarTema('escuro');
});