// importa a lista de clientes da model
let clientes = require("../models/clienteModel");


const listaClientes = (req, res) => {
    // responde com a lista completa de clientes no 
    // formato JSON
    res.json(clientes)
};


const adicionarCliente = (req, res) => {
    // extrai os dados vindos do frontend
    const {nome, email, empresa} = req.body
};

// cria um novo cliente com id automatico
const novoCliente = {id: clientes.length+1, nome: 'Leandro', email: 'bbbbcccccc@gmail.com', empresa: 'Bradesco'};

// add o novo cliente no "banco de dados"
clientes.push(novoCliente);

// responde para o frontend confirmando q o novo cliente foi criado 
res.status(201).json(novoCliente);

// exportamos as funcoes para serem usadas em outras partes
modules.exports = {listaClientes,  adicionarCliente};