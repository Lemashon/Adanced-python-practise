import psycopg2

# Connect to the "postgres" database (default database for PostgreSQL)
conn = psycopg2.connect(
    host="localhost",
    port=,
    database="postgres",
    user="",
    password=""
)

# Create a cursor
cur = conn.cursor()

# Create a new database
cur.execute("CREATE DATABASE database2")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
