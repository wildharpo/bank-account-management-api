import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

class RepoBase:
    def get_db_connection(self):
        # get the DB connection properties

        server_host = os.getenv('MYSQL_HOST')
        server_user = os.getenv('MYSQL_USER')
        server_password = os.getenv('MYSQL_PASSWORD')
        server_database = os.getenv('MYSQL_DATABASE')

        # create a DB connection
        mydb = mysql.connector.connect(
            host=server_host,
            user=server_user,
            password=server_password,
            database=server_database
        )

        # return the DB connection object
        return mydb
    
    def select_data(self, sql_query:str):
        db_conn = self.get_db_connection()
        db_cursor = db_conn.cursor(dictionary=True)
        db_cursor.execute(sql_query)
        query_result = db_cursor.fetchall()
        return query_result
    
    def select_data_by_id(self, sql_query:str, id_argument:tuple[int]):
        db_conn = self.get_db_connection()
        db_cursor = db_conn.cursor(dictionary=True)
        db_cursor.execute(sql_query, id_argument)
        query_result = db_cursor.fetchone()
        return query_result