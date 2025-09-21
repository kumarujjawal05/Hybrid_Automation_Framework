import psycopg2


def get_users_from_db():
    users = []
    try:
        conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="1234",
            dbname="user_db",
            port="5432"
        )
        print("Postgres Connection Established")

        cursor = conn.cursor()
        cursor.execute('SELECT username, password FROM "user";')  # fetch only needed cols
        users = cursor.fetchall()

        print("Data retrieved from the 'user' table:")
        for row in users:
            print(row)

        cursor.close()
        conn.close()
        print("Postgres Connection Closed")

    except psycopg2.Error as e:
        print(f"Error with Postgres: {str(e)}")

    return users
