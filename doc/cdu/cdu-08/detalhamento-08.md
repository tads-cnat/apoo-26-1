# CDU 08. Cancelar agendamento

- **Ator principal**: Paciente
- **Atores secundários**: não há	 
- **Resumo**: Um paciente ao acessar a lista dos seus agendamentos, seleciona a opção de cancelar um dado agendamento. São apresentados os detalhes do agendamento e é solicitada uma conmfirmação do cancelamento.
- **Pré-condição**: Paciente devidamente logado e agendamemto efetuado anteriormente.
- **Pós-Condição**: Alteração do estado da consulta para cancelado.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 0 - A partir da tela principal do sistema, o paciente clica na opção para apresentação dso seus agendamentos | |  
| | 1 - O sistema apresenta a lista de agendamentos do paciente logado |
| | 2 - Para cada agendamento o sistema apresenta três opções: (a) visualizar detalhes, (b) alterar agendamento e (c) cancelar agandamento |
| 3 - O paciente seleciona a opção de cancelar agendamente para um dado agendamento | |
| | 4 - O sistema apresenta os detalhes do agendamento e questiona se o paciente confirma o cancelamento |
| 5 - O paciente confirma o cancelamento | |
| | 6 - O sistema altera o estado do agendamento e retorna a tela principal do sistema, com a apresentação da mensagem de agendamento cancelado com sucesso | 

## Fluxo Alternativo I - Nenhum agendamento
| Ações do ator | Ações do sistema |
| :---: |:---: | 
| | 1.1 - O sistema apresenta a mensagem indicando que nenhum agendamento identificado para o paciente |  

## Fluxo Alternativo II - Cancelamento com menos de 24h
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| | 4.2 - O sistema apresenta os detalhes do agendamento, com a observação que o agendamento é para menos de 24h e por essa razão não pode ser cancelado e precisará ser pago |
| | 5.2 - O sistema colicita a informação se o paciente irá comparecer à sessão |
| 6.2 - O paciente informa que não deverá comparecer | |
| | 7.2 - O sistema atualiza o estado do agendamento, retornando a listagem dos agendamentos do paciente |  

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...