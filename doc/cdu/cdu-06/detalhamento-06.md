# CDU 06. Agendar sessão presencial 

- **Ator principal**: Paciente
- **Atores secundários**: não possui	 
- **Resumo**: O paciente consulta os horários disponíveis de um psicólogo, seleciona um horário específico e confirma o agendamento.
- **Pré-condição**: O paciente está devidamente autenticado no sistema.
- **Pós-Condição**: As informações do agendamento são persistidas com sucesso.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 0 - a partir de uma pesquisa pelos profissionais da clínica, o paciente seleciona um psicólogo específico. | |  
| | 1 - o sistema exibe os detalhes do psicólogo e os 10 (dez) próximo horários disponíveis do profissional. |
| 2 - o paciente seleciona o horário mais conveniente para ele. | |
| | 3 - o sistema exibe os detalhes do agendamento, com destaque para o valor a ser corbado e pede confirmação do mesmo. |
| 4 - o paciente confirma o agendamento. | |
| | 5 - o sistema dá a opção de pagamento nesse momento ou presencialmente antes da consulta. |
| 6 - o paciente escolhe pagar presencialmente antes da consulta. | |
| | 7 - o sistema retorna à página das consultas agendadas com a mensagem de que a consulta foi registrada com sucesso. |

## Fluxo Alternativo I - Paciente com restrição no cadastro
| Ações do ator | Ações do sistema |
| :---: |:---: | 
| 1.1 - ... | |  
| | 1.2 - ... |

## Fluxo Alternativo II - Pagamento no momento do agendamento
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 2.1 - ... | |  
| | 2.2 - ... |  

## Fluxo Alternativo III - Profissional sem horários disponíveis
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 2.1 - ... | |  
| | 2.2 - ... | 

## Fluxo Alternativo IV - Paciente deseja mais possibilidades de horário
| Ações do ator | Ações do sistema |
| :---: | :---: | 
| 2.1 - ... | |  
| | 2.2 - ... | 

> Obs. as seções a seguir apenas serão utilizadas na segunda unidade do PDSWeb (segundo orientações do gerente do projeto).

## Diagrama de Interação (Sequência ou Comunicação)

> Substituir pela imagem correspondente...

## Diagrama de Classes de Projeto

> Substituir pela imagem contendo as classes (modelo, visão e templates) que implementam o respectivo CDU...