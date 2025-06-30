from dotenv import load_dotenv
import os

load_dotenv()


DATABASE_MYSQL_W = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'charset': 'utf8mb4'
}

DATABASE_MYSQL_NAME = 'library_group1_hiunter'


DATABASE_MONGO_W = {
    
}

