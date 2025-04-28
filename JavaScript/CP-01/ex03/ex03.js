const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})
readline.question('Diga um numero: ', (num) => {
    const numero = parseInt(num);

    if (!isNaN(numero)) {
        if (numero == 0) {
            console.log('Seu numero é zero');
        } else if (numero > 0) {
            console.log('Seu numero é positivo');
        } else {
            console.log('Seu numero é negativo');
        }
    }
    readline.close()
})
