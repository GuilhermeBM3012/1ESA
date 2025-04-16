const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
})
readline.question('Diga o preço da sua compra: ', (preco) => {
    const numero = parseFloat(preco);

    if (!isNaN(preco)) {
        if (preco > 100) {
            let desconto = (preco * 0.1);
            let final = preco - desconto;
            console.log(`Vc ganhou um desconto de 10%. Ent a sua compra deu R$ ${final}`);
        } else {
            console.log(`Sua compra deu ${preco}`);
        }
    }
    readline.close();
})

