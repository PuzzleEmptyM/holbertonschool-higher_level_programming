-- List records with names and display score and name (in this order)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
