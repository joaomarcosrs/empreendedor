# Empreendedor

O link do projeto é https://sala-do-empreendedor.herokuapp.com/

Alguns templates apenas são visualizados caso o login seja feito. Para rodar teste basta usar as credenciais

Login: joaomarcos

Senha: admin

Atualmente, estão ativas para CRUD e teste apenas as urls:

https://sala-do-empreendedor.herokuapp.com/home/registro_atendimento

onde, é feito um registro de atendimento, com validação de CPF e CNPJ.

e

https://sala-do-empreendedor.herokuapp.com/home/registros

onde, são visualizados os registros de atendimento.

Pontos melhorados:

1. Na página de https://sala-do-empreendedor.herokuapp.com/home/registros, um  modal foi implementado para quando clicar no CNPJ, apareçam informações detalhadas de cada atendimento.

2. Foi criado a tela de autenticação de login do usuário é a tela inicial para acessar a aplicação.

3. Foi criado a home onde vai ser possível acessar o html para registrar atendimento e sessão de usuário.

4. Redirecionamento da url usando json, para chamar a função no javascript.

5. Foi criado um filtro em JS para selecionar os registros de acordo com o que é digitado no campo do input.

6. O html foi estendido para todas as outras telas.


Pontos que devem ser melhorados:

HTML deve ser melhorado com a estilização do CSS.

Quando criada a tela de autenticação o ideal será que as informações como usuário, data e horário sejam armazenadas no banco de dados em todos os atendimentos.
