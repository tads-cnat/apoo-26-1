# CDU 05. Agendar Teleconsulta  

- **Ator principal**: Paciente
- **Atores secundários**: Gateway de Pagamento, Sistema de E-mail	 
- **Resumo**: ...
- **Pré-condição**: O paciente deve estar autenticado no sistema. O psicólogo selecionado deve ter horários disponíveis em sua agenda.
- **Pós-Condição**: ...

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 1 - O Paciente acessa o perfil de um Psicólogo e visualiza sua agenda de disponibilidades. | | 
| 2 - O Paciente seleciona uma data e um horário disponível. | |
| | 3 - O Sistema altera o status daquele horário para "Reservado" por um período de 10 minutos e redireciona o Paciente para a tela de checkout. |
| | 4 - O Sistema apresenta o valor da consulta e as opções de pagamento (Cartão de Crédito ou PIX). |
| 5 - O Paciente seleciona "Cartão de Crédito", insere os dados do cartão e clica em "Pagar". | |
| | 6 - O Sistema envia os dados da transação para o Gateway de Pagamento externo. |
| | 7 - O Gateway de Pagamento autoriza a transação. |
| | 8 - O Sistema registra o Pagamento aprovado vinculado à Consulta. |
| | 9 - O Sistema altera o status da Consulta para "Agendada" e gera o link seguro da sala de videochamada. |
| | 10 - O Sistema dispara um e-mail de confirmação (contendo data, horário e link da sala) tanto para o Paciente quanto para o Psicólogo. |

## Fluxo Alternativo I - Pagamento Recusado

| Ações do ator | Ações do sistema |
| :---: |:---: |  
| | 7.1 - O Gateway de Pagamento recusa a transação do cartão de crédito. |
| | 8.1 - O Sistema exibe uma mensagem de erro ao Paciente ("Pagamento não autorizado"). |
| 9.1 - O Paciente pode escolher tentar novamente ou cancelar. | |
| 10.1 - O Paciente escolhe encerrar. | |
| | 11.1 - O sistema torna a exibir a tela inicial do sistema. |

## Fluxo Alternativo II - Tempo limite de reserva excedido (Pode ocorrer a qualquer momento entre os passos 3 e 7)

| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 3.2 - O Paciente não conclui o pagamento dentro dos 10 minutos estipulados | |  
| | 4.2 - O Sistema cancela o processo, exclui a reserva temporária e devolve o horário para o status "Disponível" na agenda do Psicólogo. |
| | 5.2 - O Sistema exibe a mensagem: "Sessão expirada. Por favor, reinicie o agendamento.", retornando ao passo 1 do fluxo principal. |

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...