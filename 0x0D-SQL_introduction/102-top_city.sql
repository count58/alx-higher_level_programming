--  a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT 
    city,
    AVG(temperature_f) AS avg_temperature
FROM 
    hbtn_0c_0.temperatures
WHERE 
    MONTH(date) IN (7, 8)  -- July and August have month values 7 and 8 respectively
GROUP BY 
    city
ORDER BY 
    avg_temperature DESC
LIMIT 3;
