// Vamos importar o modulo "readline" para interagir com a entrada e saida do terminal
const readline = require('readline').createInterface({
    input:process.stdin, // define a entrada com o fluxo de entrada padrão (teclado)
    output:process.stdout, // define a saida como o fluxo de saida padrao (terminal)
});

// Exibe uma pergunta no terminal e espera pela resposta do usuario
readline.question('Diga um número: ', (numeroDigitado) => {
    // Converte a entrda do usuario, (q é uma string), para um numero inteiro
    const n = parseInt(numeroDigitado);

    // Verifica se a conversao para o numero interio foi bem sucedida
    if (!isNaN(n)) {
         // Se o numero for divisivel por 2 e restar 0, é par, senao, ímpar
         if(n % 2 == 0) {
            console.log(`O ${n} é um número é par`);
         } else {
            console.log(`O ${n} é um número é impar`);
         } 
    } else {
        console.log('O valor de entrda não é um inteiro! ')
    }
    // Fechar a interface do 'readline', encerrando a interacao com o terminal
    readline.close();
})
    
