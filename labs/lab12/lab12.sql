.read su18data.sql
.read sp18data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, denero FROM students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 13 ORDER BY smallest ASC LIMIT 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color 
  from students as first, students as second 
  where first.pet = second.pet AND first.song = second.song AND first.time < second.time;
