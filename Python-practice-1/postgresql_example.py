import psycopg2

# Connect to the "postgres" database (default database for PostgreSQL)
conn = psycopg2.connect(
    host="localhost",
    port=5000,
    database="postgres",
    user="postgres",
    password="Allen-1998"
)

# Create a cursor
cur = conn.cursor()

# Create a new database
cur.execute("CREATE DATABASE database1")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

# Connect to the new "mydatabase" database
conn = psycopg2.connect(
    host="localhost",
    port=5000,
    database="database1",
    user="postgres",
    password="Allen-1998"
)

# Create a cursor
cur = conn.cursor()

# Create the "testtable" table with a "data" column of type jsonb
cur.execute("CREATE TABLE testtable (data jsonb)")

# Insert some data into the table
data1 = {'name': 'John', 'age': 30}
cur.execute("INSERT INTO testtable (data) VALUES (%s)", (data1,))

data2 = {'name': 'Alice', 'age': 25}
cur.execute("INSERT INTO testtable (data) VALUES (%s)", (data2,))
            
data3 = {'name': 'Bob', 'age': 35}
cur.execute("INSERT INTO testtable (data) VALUES (%s)", (data3,))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

