import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def create_conn():
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        database="guvi_streamlit"
        )
    return db

