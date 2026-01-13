# Validação de Dados Contábeis

Este repositório apresenta um conjunto de validações aplicadas a dados contábeis, com foco na integridade, consistência e confiabilidade das informações utilizadas em processos de fechamento.

O objetivo do projeto é identificar inconsistências comuns em registros contábeis — como campos obrigatórios ausentes, valores incompatíveis com a natureza da conta e falhas de preenchimento — antes que esses dados impactem balancetes e relatórios gerenciais.

---

## O que é validado

As validações contemplam situações recorrentes em ambientes financeiros, incluindo:

- Lançamentos sem valor informado  
- Receitas com valores inconsistentes  
- Ausência de centro de custo  
- Regras básicas de negócio aplicadas aos lançamentos  

Esses pontos são críticos para garantir a qualidade da informação e reduzir retrabalho durante o fechamento contábil.

---

## Como o projeto está organizado

- **data/**  
  Contém conjuntos de dados fictícios utilizados para simular cenários de inconsistência.

- **regras_negocio/**  
  Documentação das regras contábeis consideradas nas validações.

- **sql/**  
  Consultas utilizadas para verificar consistência e integridade dos dados.

- **src/**  
  Scripts em Python responsáveis pela execução das validações.

- **testes/**  
  Cenários avaliados e resultados esperados para cada validação.

---

## Abordagem

As validações foram implementadas de forma simples e objetiva, priorizando clareza, rastreabilidade e facilidade de manutenção.  
A lógica aplicada reflete situações reais encontradas em sistemas financeiros e ERPs, com foco na prevenção de erros antes do fechamento.

---

## Observações

- Os dados utilizados neste repositório são fictícios  
- O projeto tem finalidade demonstrativa  
- As regras podem ser expandidas conforme a necessidade do processo contábil  

---

## Próximos passos

- Inclusão de novas regras de validação  
- Ampliação dos cenários analisados  
- Evolução do processo conforme maior complexidade dos dados  
