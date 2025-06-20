import pymysql
import settings

def connection(config):
    conn = pymysql.connect(**config)
    return conn

def search_data_about_books(db_conn, param):
    with db_conn.cursor() as cursor:
        cursor.execute(f'USE {settings.DATABASE_MYSQL_NAME}')
        cursor.execute('SELECT * FROM books')
        return cursor.fetchall()


def search_data_about_customers(db_conn, param):
    with db_conn.cursor() as cursor:
        cursor.execute(f'USE {settings.DATABASE_MYSQL_NAME}')
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()