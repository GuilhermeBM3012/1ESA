// criação do framework express, q facilita criar um servidor http no 
// node.js
const express = require("express");

// importa o cors, q irá nos possibilitar que o frontend(react) possa 
// se comunicar com o backend sem bloqueios
const cors = requiere("cors");

// cria a aplicação express, q será o nosso servidor 
const app = express();

// habilita o cors q possibilita que o frontend acesse a API sem 
// restrições de segurança
app.use(cors());

// importa rotas do cliente q criamos em outro arquivo
const clienteRoutes = require("./routes/clienteRoutes");

// toda vez q eu acessar /clientes, serei redirecionado para as rotas 
// dos clientes
app.use("/clientes", clienteRoutes);


// define a porta do servidor(5000)
const PORT = 5000;

app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
})
