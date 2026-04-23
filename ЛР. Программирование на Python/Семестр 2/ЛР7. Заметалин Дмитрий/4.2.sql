SELECT 
    m.name AS Товар,
    m.measure AS Цена,
    m.measure_type AS Ед_изм,
    SUM(sl.amount) AS Всего_продано,
    COUNT(sl.merch_id) AS Количество_продаж,
    SUM(sl.amount * m.measure) AS Общая_выручка
FROM sales sl
INNER JOIN merch m ON sl.merch_id = m.id
INNER JOIN sellers s ON sl.seller_id = s.id
WHERE s.department_id = 1
    AND sl.date = '2025-03-01'
GROUP BY m.id
