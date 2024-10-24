# Database Exercises

---

### Task 1: Create Database and Table
```sql
CREATE DATABASE my_database;
USE my_database;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
INSERT INTO customers (name, age) 
VALUES ('John Doe', 30), ('Jane Smith', 25), ('Alice Brown', 28), ('Bob White', 40);
SELECT * FROM customers WHERE age > 30;

