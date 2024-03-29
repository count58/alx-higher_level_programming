-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT 
    city,
    AVG(temperature_f) AS avg_temperature
FROM 
    hbtn_0c_0.temperatures
GROUP BY 
    city
ORDER BY 
    avg_temperature DESC;
