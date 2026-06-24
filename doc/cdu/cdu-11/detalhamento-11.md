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
| | 5 - o sistema retorna à listagem dos agendamentos não confirmados (passo 1), com uma mensagem indicado que o agendamento foi confirmado com sucesso. | 

## Fluxo Alternativo I - ...
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - ... | |  
| | 1.2 - ... |

## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - ... | |  
| | 2.2 - ... |  

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...