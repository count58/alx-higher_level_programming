0x0D. SQL - Introduction

Here's a brief introduction to SQL:

SQL Introduction:
What is SQL?
SQL stands for Structured Query Language.
It's a standard language for interacting with relational databases.
With SQL, you can create, delete, fetch rows, and modify rows, etc.
Types of SQL Commands:
DDL (Data Definition Language): It deals with database schemas and descriptions, and allows you to create, alter, or delete tables.

CREATE: Create objects in the database
ALTER: Alters the structure of the database
DROP: Delete objects from the database
DML (Data Manipulation Language): It allows you to work with the data.

SELECT: Retrieve data from the database
INSERT: Insert data into a table
UPDATE: Updates existing data in a table
DELETE: Deletes records from a table
DCL (Data Control Language): It includes commands like GRANT and REVOKE, which mainly deal with the rights and permissions.

Basic SQL Commands:
SELECT: Retrieves data from a table

sql
Copy code
SELECT column1, column2 FROM table_name;
WHERE: Used to filter records

sql
Copy code
SELECT column1, column2 FROM table_name WHERE condition;
INSERT INTO: Used to insert new records in a table

sql
Copy code
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
UPDATE: Used to modify existing records

sql
Copy code
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
DELETE: Used to delete existing records

sql
Copy code
DELETE FROM table_name WHERE condition;
This is just a very basic introduction. SQL is a vast topic with many advanced features like JOINS, GROUP BY, HAVING, etc., which you would likely explore in depth in the module 0x0D. SQL - Introduction or subsequent modules.
