SELECT 
    m.name AS Товар,
    m.measure_type AS Единица_измерения,
    SUM(sl.amount) AS Всего_продано,
    SUM(sl.amount * m.measure) AS Общая_выручка
FROM sales sl
INNER JOIN merch m ON sl.merch_id = m.id
GROUP BY m.id
ORDER BY Общая_выручка DESC;