import pyodbc



def connect_to_bank_db():
    return pyodbc.connect("Driver={PostgreSQL Driver};Database=bank_data;Uid=bank_user;Pwd=bank_user")

def drop_table(connection):
    connection.execute("drop table if exists bank_data")

def create_table(connection):
    statement = """
    CREATE TABLE IF NOT EXISTS bank_data (
                id BIGSERIAL PRIMARY KEY, 
                account_number TEXT, 
                transaction_date DATE, 
                transaction_type TEXT, 
                transaction_purpose TEXT, 
                recipient TEXT, 
                amount REAL, 
                currency TEXT 
            )
            """
    connection.execute(statement)


def insert_into_table(connection, data):
    statement = "INSERT INTO bank_data (account_number,transaction_date, transaction_type, transaction_purpose, recipient, amount, currency) values(?,?,?,?,?,?,?)"
    for row in data:
        connection.execute(statement, row)
