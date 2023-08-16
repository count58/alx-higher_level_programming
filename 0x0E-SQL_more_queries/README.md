0x0E-SQL_more_queries

Let's break down each of the queries provided in the "SQL_more_queries" section and understand what they do:

1. **Joining Tables**:
    ```sql
    SELECT employees.first_name, employees.last_name, departments.name AS department_name
    FROM employees
    JOIN departments ON employees.department_id = departments.id;
    ```
    This query retrieves the first name and last name of employees and the name of the department they belong to. The `JOIN` operation combines rows from the `employees` and `departments` tables based on the matching `department_id`. 

2. **Aggregate Functions**:
    ```sql
    SELECT AVG(salary) AS average_salary, MIN(salary) AS minimum_salary, MAX(salary) AS maximum_salary
    FROM employees;
    ```
    This query utilizes aggregate functions to perform calculations on the `salary` column of the `employees` table:
    - `AVG(salary)` computes the average salary.
    - `MIN(salary)` finds the lowest salary.
    - `MAX(salary)` identifies the highest salary.

3. **Group By**:
    ```sql
    SELECT departments.name AS department_name, COUNT(employees.id) AS number_of_employees
    FROM departments
    JOIN employees ON departments.id = employees.department_id
    GROUP BY departments.name;
    ```
    This query groups employees by their respective departments and counts how many employees are in each department. The `GROUP BY` clause groups the results by the department name.

4. **Having Clause**:
    ```sql
    SELECT departments.name AS department_name, AVG(employees.salary) AS average_salary
    FROM employees
    JOIN departments ON employees.department_id = departments.id
    GROUP BY departments.name
    HAVING AVG(employees.salary) > 50000;
    ```
    This query is similar to the previous one but introduces the `HAVING` clause. After grouping employees by department, it filters out departments where the average salary is not greater than 50,000. Unlike the `WHERE` clause, which filters rows before aggregation, the `HAVING` clause filters after aggregation.

5. **Subquery**:
    ```sql
    SELECT first_name, last_name
    FROM employees
    WHERE department_id = (SELECT id FROM departments WHERE name = 'Sales');
    ```
    This query fetches the first and last names of employees working in the 'Sales' department. The subquery `(SELECT id FROM departments WHERE name = 'Sales')` retrieves the ID of the 'Sales' department, which the main query then uses to filter the employees.

6. **Union**:
    ```sql
    SELECT first_name FROM employees
    UNION
    SELECT first_name FROM managers;
    ```
    The `UNION` operation combines the results of two or more SELECT statements. In this query, the unique first names from both the `employees` and `managers` tables are combined into a single list.

7. **Case**:
    ```sql
    SELECT first_name, last_name, 
           CASE 
               WHEN salary > 70000 THEN 'High'
               WHEN salary > 50000 THEN 'Medium'
               ELSE 'Low'
           END AS salary_level
    FROM employees;
    ```
    This query classifies employees based on their salary level using the `CASE` statement. It's a conditional expression that allows for if-else logic. Here, it categorizes salaries into 'High', 'Medium', or 'Low'.

I hope that provides a clearer understanding of each query! If you have further questions or need more detail on any particular query, please let me know.
