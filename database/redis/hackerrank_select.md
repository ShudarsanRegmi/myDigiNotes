# Problems from hackerrank involving select command

### Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
```sql
(select city,length(city) from STATION order by length(city), city asc) union (select city,length(city) from STATION order by
 length(city) desc, city asc);
```

### fetch all cities whose name starts with vowel

```sql
SELECT CITY from STATION WHERE city like "a%" or city like "e%" or city like "i%" or city like "o%" or city like "u%";
```
### Fetch distinct cities whose name ends with vowels
```sql
SELECT DISTINCT CITY from STATION WHERE city like "%a" or city like "%e" or city like "%i" or city like "%o" or city like "%u";
```
### Fetch distinct cities which starts and ends with vowels
```sql
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';
```
