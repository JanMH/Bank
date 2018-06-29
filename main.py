import bank_data_import
import data_base_functions
import visualization



sparkasse = bank_data_import.parse_sparkasse_file('/home/jan/sparkasse.csv')
ing_diba = bank_data_import.parse_ing_diba_file('/home/jan/ing-diba.csv')

connection = data_base_functions.connect_to_bank_db()
data_base_functions.drop_table(connection)
data_base_functions.create_table(connection)
data_base_functions.insert_into_table(connection,sparkasse)
data_base_functions.insert_into_table(connection,ing_diba)


statement = """
        select to_char(date_trunc('month', transaction_date), 'YY-mm') as month, sum(amount) from bank_data
        group by month order by month;

       """


month, sum_by_month = zip(*connection.execute(statement).fetchall())

visualization.barchart(month,sum_by_month)
connection.commit()