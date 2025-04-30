for (let i = 0; i < 5; i++) {
    console.log(`Numero: ${i}`);
}


let cont = 0;
while (cont < 5) { // usa quando n tem a quant de vezes q vai rodar 
    console.log(`Contador está em: ${cont}`);
    cont++;
}


const pessoa = {
    nome: 'Ana',
    idade: 30,
    cidade: 'São Paulo'
};
// tem um objeto(pessoa) c/ 3 propriedades 
for (const propriedade in pessoa) {
    console.log(`${propriedade}: ${pessoa[propriedade]}`)
}


const cores = ['vermelho', 'azul', 'preto'];
for (const cor of cores) {
    console.log(cor);
}

const resultado = document.getElementById('resultado')
const carro = {
    marca: 'Ford',
    modelo: 'Mustang',
    ano: '2007',
    cor: 'Azul',
    ligar: function () {
        console.log('O carro está ligado! ');
        exibirMensagem('O carro está ligado! ');
    },

    obterDetalhes: function () {
        return `${this.marca} ${this.modelo} ${this.ano} ${this.cor}`
    }
};

console.log('---Objeto Literal---');
console.log(`Marca: ${carro.marca}`); // acessando a propriedade marca usando a notção de ponto
console.log(`Modelo: ${carro['modelo']}`); // acessando a propriedade modelo usando a notção de colchetes
carro.ligar(); // chamando o metodo ligar usando a notação de ponto

const detalhesCarro = carro.obterDetalhes();
console.log(`Detalhes do carro: ${detalhesCarro}`);
exibirMensagem(`Detalhes do carro: ${detalhesCarro}`);

console.log('---Exibindo o objeto---')
for (const propriedade in carro) {
    console.log(`${propriedade}: ${carro[propriedade]}`);
    exibirMensagem(`${propriedade}: ${carro[propriedade]}`);
}


// Outra forma de exibir um objeto (converte o objeto para uma String JSON --> usa p/ se comunicar c/ o servidor)
const carroJSON = JSON.stringify(carro); // converte o objeto(carro) no modelo string JSON
console.log(`Objeto carro com o JSON: ${carroJSON}`);
exibirMensagem(`Objeto carro com o JSON: ${carroJSON}`);


// Funções construtoras --> usada para criar multiplos objetos com uma unica estrutura
// Usa a palavra chave new para invocar um construtor
function Pessoa(nome, idade, profissao) {
    this.nome = nome; // cria uma propriedade 'nome' p/ o novo objeto e atribui o valor do parametro nome
    this.idade = idade;
    this.profissao = profissao;
    this.saudar = function () {
        console.log(`Olá, meu nome é: ${this.nome} e eu sou ${this.profissao}`);
    }
}

// Criando instancias (objetos) da funcao construtora Pessoa usando o 'new'
const pessoa1 = new Pessoa('Carlos', 32, 'Engenheiro de Software');
const pessoa2 = new Pessoa('Diego', 18, 'Bombeiro');

console.log('---Funçoes Construtoras---');
console.log(`Nome da pessoa1: ${pessoa1.nome}`);
pessoa1.saudar();
console.log(`Nome da pessoa2: ${pessoa2.nome}`);
pessoa2.saudar();


function exibirMensagem(mensagem) {
    const paragrafo = document.createElement('p'); // cria um novo elemento <p> 
    paragrafo.textContent = mensagem; // define o texto do paragrafo com a mensagem 
    resultado.appendChild(paragrafo); // add o paragrafo elemento 'resultado' no html 
}
