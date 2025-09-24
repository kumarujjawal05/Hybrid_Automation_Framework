import psycopg2

def get_connection():
    """Establishes a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1234",
        dbname="saucedemo_db",
        port="5432"
    )
    return conn
def get_users_from_db(valid=None):
    users = []
    try:
        conn = get_connection()
        print("Postgres Connection Established")

        cursor = conn.cursor()
        if valid is None:
            cursor.execute("SELECT username, password FROM users")
        else:
            cursor.execute("SELECT username, password FROM users WHERE is_valid = %s", (valid,))        
            users = cursor.fetchall()

        print("Data retrieved from the 'users' table:")
        for row in users:
            print(row)

        cursor.close()
        conn.close()
        print("Postgres Connection Closed")

    except psycopg2.Error as e:
        print(f"Error with Postgres: {str(e)}")

    return users


def get_products_from_db():

    """
        Fetch product names from the products table.
        """
    products = []

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT name FROM products")
        
        # cur.execute("SELECT name FROM products;")
        rows = cur.fetchall()

        products = [row[0] for row in rows]  # only product_name
        print("Products retrieved from DB:", products)

        cur.close()
        conn.close()

    except Exception as e:
        print("Error fetching products:", e)

    return products

  