-- List all shows and linked genres
SELECT
    tv_shows.title,
    IFNULL(GROUP_CONCAT(tv_genres.name ORDER BY tv_genres.name ASC SEPARATOR ', '), 'NULL') AS genre
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_shows.title
ORDER BY tv_shows.title, genre;
