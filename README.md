Api soma

Construção da API REST utilizando Python e Flask, aplicando conceitos de back-end, integração cliente–servidor e autenticação por token.

Servidor Flask com rota GET
O Flask funciona como um intermediário entre o cliente e o servidor. O decorador `@app.route` define qual caminho (rota) e qual método HTTP a função vai responder. A rota `/api/soma` recebe dois números pela URL e retorna a 
soma em formato JSON.

Cliente Python consumindo a API
Com o uso biblioteca `requests`, é possível fazer requisições HTTP diretamente pelo código Python. A resposta possui três partes importantes: o status (200 = sucesso), os cabeçalhos com metadados e o corpo em JSON.

Rota POST com corpo JSON e cabeçalho
Rotas GET e POST:
GET: os dados viajam visíveis na URL — indicado para buscar informações.
POST: os dados viajam no corpo da requisição, fora da URL — indicado para enviar informações com mais segurança.

Autenticação com Bearer Token
A proteção das rotas pelo cabeçalho `Authorization` com o padrão Bearer token. O servidor verifica se o token enviado é válido antes de liberar o acesso. Caso contrário, retorna o status `401 Unauthorized`.  

Resultados:

*cliente.py
 Status: 200 | Corpo: {'resultado': 5.0}

*cliente_post.py
 Status: 200 | Corpo: {'resultado': 17, 'chamado_por': 'turma-ciberseguranca'}

*cliente_token.py
 Com token válido: 200
 Sem token: 401
 Token errado: 401
