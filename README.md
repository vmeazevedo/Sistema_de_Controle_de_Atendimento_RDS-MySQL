## Sistema de Controle de Atendimento utilizando RDS-MySQL direto da cloud AWS
O algoritmo consiste em um sistema de controle para consultórios via interface gráfica PyQt5, interligado a uma base de dados RDS-MySQL diretamente da cloud da AWS, não havendo a necessidade de um servidor local. O sistema permite o controle das atividades/atendimentos realizados em um consultório de forma simples e fácil, permitindo realizar cadastro de atendimento, consultas a base e por item a escolha do profissional.

## Requirements
Será necessário instalar a biblioteca abaixo:

- mysql-connector
- PyQt5

## Criando instancia RDS-MySQL
- Selecione MySQL
- Version: MySQL 8.0.11
-> Free tier
- Entre com os dados de base, username e password:

db instance: "nome da base de dados"

username: "seu usuário"

password: "sua senha"

- DB instance size e Storage é default não mexer
- VPC: Default
- Subnet group: default
- Public acess: Yes
- VPC security group: Create new

New VPC security group name: <entrar_com_o_nome>

- Availability Zone: escolher onde você ta conectado


## Tela inicial
Ao abrir a interface nos é apresentado as opções abaixo:
- Cadastrar: Permite realizar o registro de um novo atendimento na base de dados na nuvem.
- Consultar: Permite consultar o histórico de atendimento realizados.
- Pesquisar: Permite pesquisar por um registro específico através de campos pré definidos.

![1](https://user-images.githubusercontent.com/40063504/102730553-dc09c700-4313-11eb-8f77-c8bff9356711.PNG)

## Tela de cadastro
- Tela de cadastro inicialmente

![2](https://user-images.githubusercontent.com/40063504/102730555-df04b780-4313-11eb-9820-b56c3fc1fee8.PNG)

- Tela de cadastro preenchida. Ao clicar me "Inserir Dados" os dados registrados vão automaticamente para a base de dados RDS na cloud.

![3](https://user-images.githubusercontent.com/40063504/102730559-e1671180-4313-11eb-8f32-8503ac5f7cab.PNG)

## Tela de consulta a base
- Quando clicamos "Consultar" a interface trás para o usuário todo o histórico de atendimento realizado.

![4](https://user-images.githubusercontent.com/40063504/102730563-e3c96b80-4313-11eb-9c37-cf54331cf0db.PNG)

## Tela de pesquisa por item
- Nessa tela podemos realizar uma pesquisa com filtros através dos checkbox e os campos de preenchimento.

![5](https://user-images.githubusercontent.com/40063504/102730587-edeb6a00-4313-11eb-9b48-e8442ebd5798.PNG)

- Resultado da pesquisa por item.

![4](https://user-images.githubusercontent.com/40063504/102730593-f17ef100-4313-11eb-8691-144634cae76d.PNG)
