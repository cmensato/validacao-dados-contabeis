-- Validação 01: Lançamentos sem valor informado
SELECT
    id,
    entry_date,
    account,
    amount,
    cost_center
FROM accounting_entries
WHERE amount IS NULL;


-- Validação 02: Receitas com valor negativo
SELECT
    id,
    entry_date,
    account,
    amount
FROM accounting_entries
WHERE account LIKE '%Receita%'
  AND amount < 0;


-- Validação 03: Centro de custo não informado
SELECT
    id,
    entry_date,
    account,
    amount,
    cost_center
FROM accounting_entries
WHERE cost_center IS NULL;
