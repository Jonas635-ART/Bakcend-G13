





Lesson 2
1 -> SELECT * FROM movies where id = 6;
2 -> SELECT * FROM movies where year between 2000 and 2010;
3-> SELECT * FROM movies where year not between 2000 and 2010;
4 -> SELECT * FROM movies where id in(1,2,3,4,5);
Lesson 3
1 -> SELECT * FROM movies where Title like '%Toy Story%';
2 -> SELECT * FROM movies where Director like '%John%';
3 -> SELECT * FROM movies where Director not like '%John%';
4 -> SELECT * FROM movies where Title like '%WALL-%';
Lesson 4
1 -> SELECT Distinct Director FROM movies order by Director ASC;
2 -> SELECT Title,YEAR FROM movies order by year DESC Limit 4;
3 -> SELECT Title FROM movies order by Title ASC Limit 5; 
4 -> SELECT Title FROM movies order by Title ASC Limit 5 offset 5;
Lesson5 
1-> SELECT City, Population FROM north_american_cities where Country like '%Canada%';
2-> SELECT City, Latitude FROM north_american_cities where Country like '%United States%' Order by Latitude DESC;
3-> SELECT city, longitude FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;
4-> SELECT City, Population FROM north_american_cities 
where Country like '%Mexico%' 
order by Population DESC limit 2;
5-> SELECT Country, City, Population FROM north_american_cities WHERE Country like '%United States' Order by Population DESC LIMIT 2 offset 2;
Lesson 6
1-> SELECT title, domestic_sales, international_sales 
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
2->SELECT title, domestic_sales, international_sales
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;
3 -> SELECT title, Rating 
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id order by Rating Desc;
lesson 7
1 -> SELECT DISTINCT building FROM employees;
2 -> SELECT building_name, Capacity FROM Buildings;
3 -> SELECT DISTINCT building_name, role 
FROM buildings 
  LEFT JOIN employees
    ON building_name = building;
lesson 8
1 -> SELECT Building, name, role FROM employees where building is null;
2 -> SELECT DISTINCT building_name
FROM buildings 
  LEFT JOIN employees
    ON building_name = building
WHERE role IS NULL;
lesson 9 
1 ->SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
2 -> SELECT title, rating * 10 AS rating_percent
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
3 -> SELECT title, year
FROM movies
WHERE year % 2 = 0;
lesson 10 

































































