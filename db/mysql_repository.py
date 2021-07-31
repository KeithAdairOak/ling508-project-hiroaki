import mysql.connector


class MysqlRepository:

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'sakila',
            #            'host': 'mysql',  # When you run this on your machine change it to 'localhost'
            #            'port': '3306',  # When you run this on your machine change it to '32000'
            'host': 'localhost',  # When you run this on your machine change it to 'localhost'
            'port': '32000',  # When you run this on your machine change it to '32000'
            'database': 'French_Terms'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
