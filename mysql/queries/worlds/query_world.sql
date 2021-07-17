-- 1
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_id = countries.id WHERE languages.language = 'Slovene';

-- 2
SELECT countries.name, COUNT(cities.id) FROM countries
JOIN cities ON cities.country_id = countries.id GROUP BY countries.id ORDER BY COUNT(cities.id) DESC;

-- 3
SELECT cities.name, cities.population, cities.country_id FROM cities
JOIN countries ON cities.country_id = countries.id  WHERE countries.name = "Mexico" AND cities.population > 500000;

-- 4
SELECT countries.name, languages.language, languages.percentage FROM countries
JOIN languages ON languages.country_id = countries.id WHERE languages.percentage > 89 ORDER BY languages.percentage DESC;

-- 5
SELECT countries.name, countries.surface_area, countries.population FROM countries 
WHERE surface_area < 501 AND countries.population > 100000;

-- 6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM countries
WHERE countries.capital > 200 AND countries.government_form = "Constitutional Monarchy" AND countries.life_expectancy > 75;

-- 7
SELECT countries.name, cities.name, cities.district, cities.population FROM cities
JOIN countries ON cities.country_id = countries.id WHERE cities.population > 500000 AND cities.district = "Buenos Aires";

-- 8
SELECT countries.region, COUNT(countries.id) FROM countries
GROUP BY countries.region ORDER BY COUNT(countries.id) DESC;
