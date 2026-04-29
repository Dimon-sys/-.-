SELECT 
    d.name AS Отдел,
    d.floor AS Этаж,
    s.name AS Сотрудник,
    s.age AS Возраст,
    s.gender AS Пол
FROM departments d
LEFT JOIN sellers s ON s.department_id = d.id
WHERE d.id = 1 
ORDER BY s.name;
