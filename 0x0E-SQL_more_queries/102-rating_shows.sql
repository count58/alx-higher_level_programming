-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
CREATE TABLE tvshows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    ...
);

CREATE TABLE ratings (
    show_id INT,
    rating_value FLOAT,
    ...
);
