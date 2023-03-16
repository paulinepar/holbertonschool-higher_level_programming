-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
--The tv _genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
AND name = 'Comedy'
GROUP BY tv_shows.title
ORDER BY tv_shows.title;