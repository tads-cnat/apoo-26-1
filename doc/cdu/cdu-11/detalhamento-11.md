# CDU 11. Avaliação de solicitação de agendamento 

- **Ator principal**: Psicólogo
- **Atores secundários**: não há	 
- **Resumo**: Um psicólogo a partir da lista de agendamentos não confirmados, seleciona um dado agendamento, visualiza os seus detalhes e confirma (ou não) o agendamento.
- **Pré-condição**: psicólogo devidamente logado e existirem agendamentos não confirmados.
- **Pós-Condição**:
  - No caso de "confirmação" - agendamento muda para o estado confirmado.
  - No caso de "não confirmação"- horário específico volta a ficar disponível, o agendamento muda de estado e é incluída uma justificativa.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 0 - o psicólogo a partir da tela principal, seleciona a opção "confirmar consultas". | |  
| | 1 - o sistema lista todos os agendamentos que ainda não foram confirmados, onde cada um possui um link associado. |
| 2 - o pscólogo clica em um dos agendamentos. |
| | 3 - o sistema exibe os detalhes do referido agendamento, com uma opção ao final para confirmar ou não. Em caso de não confirmação é necessário preencher um campo de justificativa. |
| 4 - o psicólogo escolhe a opção "confirmar" agendamento e submete o formulário. |
| | 5 - o sistema retorna à listagem dos agendamentos não confirmados (passo 1), com uma mensagem indicado que o agendamento foi confirmado com sucesso. (fim) | 

## Fluxo Alternativo I - Nenhum agendamento não confirmado
| Ações do ator | Ações do sistema |
| :---: |:---: | 
| | 1.1 - o sistema exibe uma mensagem indicando que não há agendamento em aberto. |  
| | 2.1 - o sistema permite que o usuário selecione a opção de retornar à página principal. (fim) |

## Fluxo Alternativo II - Identificador de agendamento inválido
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| | 3.2 - o sistema retorna para a lista dos agendamentos sem confirmação, com uma mensagem indicando que identificador de agendamento é inválido. (fim) |

## Fluxo Alternativo III - Escolha por "não confirmar"
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 4.3 - o psicólogo escolhe a opção "não confirmar" agendamento, preenche a justificativa e submete o formulário. | |
| | 5.3 - o sistema libera o horário, muda o estado do agendamento, incluindo a justificativa e retorna para a página principal com a mensagem "agendamento cancelado com sucesso". (fim) | 


## Fluxo Alternativo IV - Escolha por "não confirmar" - sem justificativa
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 4.4 - o psicólogo escolhe a opção "não confirmar" agendamento e submete o formulário. | |  
| | 5.4 - o sistema retorna à tela dos detalhes do agendamento, com uma mensagem indicando que a não confirmação necessita de uma justificativa. (passo 3 do fluxo principal) | 

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...