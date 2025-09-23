import psycopg2


def get_users_from_db(valid=None):
    users = []
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="1234",
            dbname="saucedemo_db",
            port="5432"
        )
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
