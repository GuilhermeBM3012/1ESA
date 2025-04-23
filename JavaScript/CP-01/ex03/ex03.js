const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout,
});

rl.question('Digite um número: ', (input) => {
    const numero = parseFloat(input);

    if (!isNaN(numero)) {
        if (numero === 0) {
            console.log('Seu numero é zero');
        } else if (numero > 0) {
            console.log('Seu numero é positivo');
        } else {
            console.log('Seu numero é negativo');
        }
    }
    readline.close()
})