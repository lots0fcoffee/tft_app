import pyodbc
from src.config.config import config

def connect_to_db() -> object:
    conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0}; SERVER=MIKE-DESKTOP; DATABASE=MAIN_TFT; Trusted_Connection=Yes;')
    cur = conn.cursor()
    return cur

def insert_into_db():
    pass

def main():
    cur = connect_to_db()
    cur.execute("select * from dbo.Summoners")

    l = cur.fetchall()

    print(l)

if __name__ == '__main__':
    main()