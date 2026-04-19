SELECT 
    m.name AS Товар,
    m.measure AS Цена,
    m.measure_type AS Ед_изм,
    s.name AS Продавец,
    d.name AS Отдел,
    d.floor AS Этаж,
    sl.amount AS Количество,
    sl.date AS Дата,
    (sl.amount * m.measure) AS Сумма
FROM sales sl
INNER JOIN merch m ON sl.merch_id = m.id
INNER JOIN sellers s ON sl.seller_id = s.id
INNER JOIN departments d ON s.department_id = d.id
WHERE m.id = 3 
ORDER BY sl.date;