-- List all genres and the number of shows linked to each genre
SELECT genre AS genre, COUNT(show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
HAVING COUNT(show_id) > 0
ORDER BY number_of_shows DESC;
