# Hello world
import ui
import db
import settings
import log_writer
import log_stats

def get_action_result(action, db_conn):
    if action == 1:
        name = ui.author_name()
        
        return db.search_data_about_books(db_conn, name)
        
    if ans == 2:
        name = ui.customer_name()
        return db.search_data_about_customers(db_conn, name)    
    if ans == 3:
        res = log_stats.get_statistics()
        print(res)
    print('Некорректный ввод.')


def menu(db_conn):
    while (ans := ui.main_menu()) != 0:    
        result = get_action_result(ans, db_conn)
        ui.print_table_data(result)

def main():
    try:
        db_conn = db.connection(settings.DATABASE_MYSQL_W)
        menu(db_conn)
        db_conn.close()
    except Exception as error:
        print('Произошла ошибка. ', error)


if __name__ == '__main__':
    main()