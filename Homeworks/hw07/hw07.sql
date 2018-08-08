CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- Q1 --
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name, s.size FROM dogs AS d, sizes AS s WHERE d.height > s.min AND d.height <= s.max;

-- Q2 --
-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child FROM parents AS a, dogs AS b WHERE a.parent = b.name ORDER BY b.height DESC;

-- Q3 --
-- Filling out this helper table is optional

CREATE TABLE siblings AS
  select a.child
  from parents as a, dogs as b
  where a.parent= b.name order by -b.height;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  select a.name || " and " || b.name || " are " || b.size ||" siblings"
  from size_of_dogs as a, size_of_dogs as b, parents as c, parents as d
  where a.size= b.size and a.name!=b.name and c.child = a.name and d.child= b.name
  and c.parent=d.parent and a.name< b.name order by a.name;

-- Q4 --
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper (dogs, stack_height, last_height);
-- Add your INSERT INTOs here

CREATE TABLE stacks as
  with
    sums(names, total, n, max) as (
      select name, height, 1, height from dogs union
      select names || ", " || name, total+height, n+1, height
        from sums, dogs
        where n < 4 and max < height
    )
  select names, total from sums where n=4 and total>=170 order by total;
