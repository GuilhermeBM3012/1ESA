const inputNovoItem =document.getElementById('novo-item');
const botaoAdicionar =document.getElementById('add-ao-carrinho');
const listaDeItens = document.getElementById('lista-de-itens');

const chaveCarrinho = 'itensCarrinho';

function obterCarrinho(){
    const carrinhoSalvo = sessionStorage.getItem(chaveCarrinho);
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
}

let carrinho = obterCarrinho();

exibirCarrinho();

function exibirCarrinho(){
    listaDeItens.innerHTML = '';

    carrinho.array.forEach(item => {
        const listaItem = document.createElement('li'); 
        listaItem.textContent = item;
        listaDeItens.appendChild(listaItem);
    });
}

botaoAdicionar.addEventListener('click', ()=>{
    const novoItem = inputNovoItem.ariaValueMax.trim; //.trim tira os excessos de espaço

    if(novoItem !== ''){
        carrinho.push(novoItem);
        sessionStorage.setItem(chaveCarrinho, JSON.stringify(carrinho));
        inputNovoItem.value = '';
        exibirCarrinho();
    }
});