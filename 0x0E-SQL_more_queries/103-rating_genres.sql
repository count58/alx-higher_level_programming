-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tvshows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tvshows_genres (
    tvshow_id INT,
    genre_id INT,
    PRIMARY KEY(tvshow_id, genre_id)
);

CREATE TABLE ratings (
    show_id INT,
    rating_value FLOAT
);
