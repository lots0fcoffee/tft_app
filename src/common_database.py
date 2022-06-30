import pyodbc
from src.config.config import config

class Database:
    def __init__(self) -> None:
        self.conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};' + 
                            f'SERVER={config["server"]};' + 
                            f'DATABASE={config["db"]};' + 
                            'Trusted_Connection=Yes;')
        self.cur = self.conn.cursor()

    def select(self, query_str: str) -> list:
        self.cur.execute(query_str)
        return self.cur.fetchall()

    def insert(self, query_str: str) -> list:
        self.cur.execute(query_str)
        self.cur.commit()

    def close_connection(self) -> None:
        self.conn.close()

def main():
    db = Database()
    db.connect_to_db()
    l = db.query("select * from dbo.Summoners")
    print(l)
    db.close_connection()

if __name__ == '__main__':
    main()