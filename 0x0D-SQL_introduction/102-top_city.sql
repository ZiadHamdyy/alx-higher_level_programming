-- displays the top 3 of cities temperature during July
-- and August ordered by temperature (descending)
SELECT city, AVG(temperature * 9/5 + 32) AS avg_temperature_fahrenheit
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC
LIMIT 3;
