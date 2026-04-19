SELECT 
    s.name AS Продавец,
    d.name AS Отдел,
    COUNT(sl.merch_id) AS Количество_продаж,
    SUM(sl.amount) AS Всего_единиц_товара
FROM sales sl
INNER JOIN sellers s ON sl.seller_id = s.id
INNER JOIN departments d ON s.department_id = d.id
GROUP BY s.id
ORDER BY Всего_единиц_товара DESC
LIMIT 3;