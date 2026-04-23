SELECT 
    s.name AS Продавец,
    s.age AS Возраст,
    s.gender AS Пол,
    d.name AS Отдел,
    d.floor AS Этаж
FROM sellers s
INNER JOIN departments d ON s.department_id = d.id
WHERE s.age > 30
