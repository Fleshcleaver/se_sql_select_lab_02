import sqlite3
import pandas as pd

# Step 1: Create database connection
conn = sqlite3.connect('data.sqlite')

# Step 2: Query employeeNumber and lastName (should return 23 rows)
df_first_five = pd.read_sql_query("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# Step 3: Same data but columns reversed
df_five_reverse = df_first_five[['lastName', 'employeeNumber']]

# Step 4: Create alias 'ID' for employeeNumber
df_alias = pd.read_sql_query("""
    SELECT employeeNumber AS ID, lastName 
    FROM employees
""", conn)

# Step 5: Add 'role' column based on job title (Executive vs Not Executive)
df_executive = pd.read_sql_query("""
    SELECT *, 
    CASE 
        WHEN jobTitle LIKE '%President%' OR jobTitle LIKE '%VP%' 
        THEN 'Executive' 
        ELSE 'Not Executive' 
    END AS role
    FROM employees
""", conn)

# Step 6: Calculate name length (first row should have length 6)
df_name_length = pd.read_sql_query("""
    SELECT *, LENGTH(lastName) AS name_length 
    FROM employees
""", conn)

# Step 7: Short title (first 2 characters, first row should be 'Pr')
df_short_title = pd.read_sql_query("""
    SELECT *, SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)

# Step 8: Sum of rounded total prices (round each order first, then sum)
sum_total_price = pd.read_sql_query("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderdetails
""", conn).sum()

# Step 9: Extract day, month, year from orderDate
df_day_month_year = pd.read_sql_query("""
    SELECT *,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
    FROM orders
""", conn)
