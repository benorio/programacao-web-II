import psycopg2

class DB:
     @staticmethod
     def connection():
         conn = psycopg2.connect(
             host = "localhost",
             database = "loja",
             user = "postgres",
             password = "benorio")
         return conn