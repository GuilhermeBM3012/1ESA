// 1º FORMA DE DECLARAR UM ARRAY: (+ usado)

const { stdout } = require('process');

// --> pd ser string
const frutas = ['maça', 'melancia', 'laranja'];
// --> pd ser numeros
const num = [10, 20, 30, 40];
// --> pd ser string e numero juntos (pd colocar de varios tipos de dados) 
const misturado = [1, 'dois', 3, 'quatro', true, null, undefined, { chave: 'valor' }];
// --> pd ficar sem nenhum elemnto
const vazio = [];


// 2º FORMA DE DECLARAR UM ARRAY:

// --> Com uma função cosntrutora
const cores = new Array('vermelho', 'preto', 'branco');


// ACESSANDO OS ELEMENTOS DO ARRAY:
const linguagens = ['js', 'python', 'html'];

// --> 1º elemento:
const primeiraLinguagem = linguagens[0];
console.log(`A 1º linguagem é ${primeiraLinguagem}`);
// --> 2º elemento:
const segundaLinguagem = linguagens[1];
console.log(`A 2º linguagem é ${segundaLinguagem}`);
// --> 3º elemento:
const terceiraLinguagem = linguagens[2];
console.log(`A 3º linguagem é ${terceiraLinguagem}`);
// --> Pegando o último elemnto, mas sem saber quantos tem:
const ultimaLinguagem = linguagens[linguagens.lenght - 1] // dentro das [] serve para colocar a qaunt de elementos q tem na const linguagens
console.log(`A última linguagem é ${ultimaLinguagem}`);


// MODIFICANDO OS ELEMNTOS DO ARRAY:
let coresMutaveis = ['branco', 'azul', 'rosa'];
coresMutaveis[1] = 'verde' // peguei o 2º elemento e troquei por verde
console.log(`Array, depois da alteração: ${coresMutaveis}`);
coresMutaveis[coresMutaveis.lenght] = 'roxo'; // conta quantos elementos tem e inseri o elemnto roxo (sendo o 3º item)


// MÉTODOS DE TRABALHAR COM O ARRAY:
let planetas = ['Terra', 'Júpter'];

// push(): adiciona 1 ou + elemntos ao final do array e retorna o novo componente
const novoComprimentoPush = planetas.push('Saturno', 'Urano');

// pop(): remove o último elemento do array
const ultimoPlanetaRemovido = planeta.pop(); // se n colocar nd nos () ele vai tirar o ultimo elemento adicionado ou n (Urano)

// shift(): remove o primeiro elemento do array
const primeiroPlanetaRemovido = planetas.shift();

// indexOf: diz a psição do elemento no array
const indiceTerra = planetas.indexOf('Terra');

// join(): mostra todos os elemntos do array, separando-os pelo elemento colocado nos ()
const stringPlanetas = planetas.join('-');


// VISUALIZANDO AS INFORMAÇÕES ATRAVÉS DE UM LAÇO DE REPETIÇÃO: 
const coresInteracao = ['laranja', 'cinza', 'ciano'];
for (let i = 0; i < coresInteracao.lenght; i++) {
    console.log(`Cor no índice: ${i}: ${coresInteracao[i]}`) // 'Cores no indice 0: laranja' e assim para todas as cores até o for acabar
}

// --> Laço for...of (+ moderno e legível p/ interar sobre valores)
for (const cor of coresInteracao) {
    console.log(`Cor: ${cor}`);
}

// --> for...each
coresInteracao.forEach(function (cor, indice) {
    console.log(`Cor: ${cor} no indice ${indice}`);
})


// COMO CRIAR UM ARRAY NO JS, RECEBENDO DADOS DO USUARIO:
readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})

const listaCompras = [];
function addItem() {
    readline.question('Diga o item p/ add na sua lista de compras: ', (itemCompras) => {
        const itemFormatado = itemCompras.trim(); // remove os espaços extras em branco
        if (itemFormatado.toLowerCase() === 'FIM') {
            console.log(`\nSua lista de compras ficou assim: `);
            listaCompras.forEach((produto, indice) => {
                console.log(`${indice + 1}. ${produto}`);
            });
            readline.close();
        } else if (itemFormatado != '') {
            listaCompras.push(itemFormatado);
            console.log(`"${itemFormatado}" foi add à sua lista `);
            addItem();
        } else {
            console.log('Diga u item válido!!!');
            addItem();
        }
    });
}

// --> Inicia o processo de add itens a lista de compras, chamando a fução pela 1º vez
console.log('Bem vindo a sua lista de compras! ');
addItem();