// importa o servidor
const express = require("express");

// cria um "mini-servidor" de rotas
const router = express.Router();

//
const {listaCliente, adicionarCliente} = require("../controllers/clienteController");