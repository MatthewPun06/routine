import psycopg2

# Update these with your DB credentials
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "routine_db"
DB_USER = "matthew"
DB_PASSWORD = "PUN18943"

try:
    # Connect to your database
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()

    # Test query: list tables in public schema
    cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")
    tables = cur.fetchall()
    print("Tables in database:", tables)

    # Optional: test a simple SELECT if you have a users table
    cur.execute("SELECT * FROM users LIMIT 5;")
    rows = cur.fetchall()
    print("First 5 users:", rows)

    cur.close()
    conn.close()
    print("Database connection successful!")

except Exception as e:
    print("Error connecting to database:", e)