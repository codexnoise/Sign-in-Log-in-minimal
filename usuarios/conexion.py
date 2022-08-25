import mysql.connector
from decouple import config


def conectar():
    database = mysql.connector.connect(
        host=config('MYSQL_HOST'),
        user=config('MYSQL_USER'),
        passwd=config('MYSQL_PASSWORD'),
        database=config('MYSQL_DATABASE'),
        port=config('MYSQL_PORT')
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]
