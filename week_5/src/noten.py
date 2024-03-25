import pandas as pd
import pyodbc
import sqlite3
import numpy as np

DB = {'servername': r'MSI\SQLEXPRESS',
    'database': 'johari'}

ssms_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + 
                     ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')
ssms_cursor = ssms_conn.cursor()

# Maak een connectie met de go_staff- en go_sales-databases
go_staff_conn = sqlite3.connect(r"../../week_2/sqlite/go_staff.sqlite")
go_sales_conn = sqlite3.connect(r"../../week_2/sqlite/go_sales.sqlite")


# Lijst met tabelnamen van de go_staff-database
go_staff_table_names = ['course', 'sales_branch', 'sales_staff', 'satisfaction', 'satisfaction_type', 'training']
go_sales_table_names = ['country', 'order_details', 'order_header', 'order_method', 'product', 'product_line', 'product_type', 'retailer_site', 'return_reason', 'returned_item', 'sales_branch', 'sales_staff', 'SALES_TARGETData']

# Dictionary om de dataframes op te slaan
go_staff = {}
go_sales = {}

# Lees de tabellen in de go_staff-database in
for table_name in go_staff_table_names:
    go_staff[table_name] = pd.read_sql_query(f"SELECT * FROM {table_name}", go_staff_conn)

# Lees de tabellen in de go_sales-database in
for table_name in go_sales_table_names:
    go_sales[table_name] = pd.read_sql_query(f"SELECT * FROM {table_name}", go_sales_conn)

def read_source_table(conn, table_name):
    query = f'SELECT * FROM {table_name}'
    df = conn.execute(query)
    result = pd.DataFrame(df.fetchall(), columns=[column[0] for column in df.description])
    return result

def read_source_tables(conn_sales, conn_country, table_names):
    dfs = {}
    for table_name in table_names:
        query = f'SELECT * FROM {table_name}'
        df = pd.read_sql_query(query, conn_sales)
        dfs[table_name] = df

    # Read country table from different database
    query = 'SELECT * FROM country'
    df_country = pd.read_sql_query(query, conn_country)
    dfs['country'] = df_country

    # Merge sales_staff with sales_branch
    result = pd.merge(dfs['sales_staff'], dfs['sales_branch'], how='inner', left_on='SALES_BRANCH_CODE', right_on='SALES_BRANCH_CODE')

    # Merge the result with country
    result = pd.merge(result, dfs['country'], how='inner', left_on='COUNTRY_CODE', right_on='COUNTRY_CODE')

    return result

def clean_target_table(conn, table_name):
    ssms_cursor.execute(f'DELETE FROM {table_name}')
    ssms_conn.commit()

def course_etl():
    # Extract
    course = read_source_table(go_staff_conn, 'course')

    # Clean Target
    clean_target_table(ssms_conn, 'COURSE')
    # Sla de gegevens binnen de course-tabel op in de SQL Server-database
    for index, row in course.iterrows():
        try:
            #Transform
            course_id = row['COURSE_CODE']
            course_description = row['COURSE_DESCRIPTION']   

            #Load
            query = f"INSERT INTO dbo.COURSE (course_id, course_description) VALUES ({course_id}, '{course_description}')"
            ssms_cursor.execute(query)
            ssms_conn.commit()

        except Exception as e:
            print(e)
            break

def satisfaction_type_etl():
    satisfaction_type = read_source_table(go_staff_conn, 'satisfaction_type')

    # Clean Target
    clean_target_table(ssms_conn, 'rsatisfaction_type')

    for index, row in satisfaction_type.iterrows():
        try:
            satisfaction_type_id = row['SATISFACTION_TYPE_CODE']
            satisfaction_description = row['SATISFACTION_TYPE_DESCRIPTION']   

            query = f"INSERT INTO dbo.rsatisfaction_type (satisfaction_type_id, satisfaction_description) VALUES ({satisfaction_type_id}, '{satisfaction_description}')"

            ssms_cursor.execute(query)
            ssms_conn.commit()

        except Exception as e:
            print(e)
            break

def sales_staff_etl():
    table_names = ['sales_staff', 'sales_branch']
    sales_staff = read_source_tables(go_staff_conn, go_sales_conn, table_names)

    # Clean Target
    clean_target_table(ssms_conn, 'rSALES_STAFF')

    for index, row in sales_staff.iterrows():
        try:
            sales_staff_id = row['SALES_STAFF_CODE']
            sales_staff_first_name = row['FIRST_NAME']
            sales_staff_last_name = row['LAST_NAME']
            sales_staff_phone = row['WORK_PHONE']
            sales_staff_email = row['EMAIL']
            sales_staff_fax = row['FAX']
            sales_staff_sales_branch_id = row['SALES_BRANCH_CODE']
            sales_staff_position_en = row['POSITION_EN']
            sales_staff_date_hired = row['DATE_HIRED']
            sales_staff_extension = row['EXTENSION']
            sales_staff_sales_branch_address1 = row['ADDRESS1']
            sales_staff_sales_branch_address2 = row['ADDRESS2']
            sales_staff_sales_branch_city = row['CITY']
            sales_staff_sales_branch_region = row['REGION']
            sales_staff_sales_branch_postal_zone = row['POSTAL_ZONE']
            sales_staff_country_id = row['COUNTRY_CODE']
            sales_staff_country_name = row['COUNTRY']
            sales_staff_country_language = row['LANGUAGE']
            sales_staff_country_currency = row['CURRENCY_NAME']

            query = """
                INSERT INTO rSALES_STAFF (
                    sales_staff_id, 
                    sales_staff_first_name, 
                    sales_staff_last_name, 
                    sales_staff_phone, 
                    sales_staff_email, 
                    sales_staff_fax, 
                    sales_staff_sales_branch_id, 
                    sales_staff_position_en, 
                    sales_staff_date_hired, 
                    sales_staff_extension, 
                    sales_staff_sales_branch_address1, 
                    sales_staff_sales_branch_address2, 
                    sales_staff_sales_branch_city, 
                    sales_staff_sales_branch_region, 
                    sales_staff_sales_branch_postal_zone, 
                    sales_staff_country_id, 
                    sales_staff_country_name, 
                    sales_staff_country_language, 
                    sales_staff_country_currency
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            params = (
                sales_staff_id, 
                sales_staff_first_name, 
                sales_staff_last_name, 
                sales_staff_phone, 
                sales_staff_email, 
                sales_staff_fax, 
                sales_staff_sales_branch_id, 
                sales_staff_position_en, 
                sales_staff_date_hired, 
                sales_staff_extension, 
                sales_staff_sales_branch_address1, 
                sales_staff_sales_branch_address2, 
                sales_staff_sales_branch_city, 
                sales_staff_sales_branch_region, 
                sales_staff_sales_branch_postal_zone, 
                sales_staff_country_id, 
                sales_staff_country_name, 
                sales_staff_country_language, 
                sales_staff_country_currency
            )

            ssms_cursor.execute(query, params)
            ssms_conn.commit()

        except Exception as e:
            print(e)
            break

def country():
    country = read_source_table(go_sales_conn, 'country')

    # Clean Target
    clean_target_table(ssms_conn, 'COUNTRY')

    for index, row in country.iterrows():
        try:
            country_id = row['COUNTRY_CODE']
            country_name = row['COUNTRY']
            country_language = row['LANGUAGE']
            country_currency = row['CURRENCY_NAME']

            query = f"INSERT INTO dbo.COUNTRY VALUES ('{country_id}', '{country_name}', '{country_language}', '{country_currency}')"

            ssms_cursor.execute(query)
            ssms_conn.commit()

        except Exception as e:
            print(e)
            break

def order_method():
    order_method = read_source_table(go_sales_conn, 'order_method')

    # Clean Target
    clean_target_table(ssms_conn, 'ORDER_METHOD')

    for index, row in order_method.iterrows():
        try:
            order_method_id= row['ORDER_METHOD_CODE']
            order_method_en = row['ORDER_METHOD_EN']

            query = f"INSERT INTO dbo.ORDER_METHOD VALUES ('{order_method_id}', '{order_method_en}')"

            ssms_cursor.execute(query)
            ssms_conn.commit()

        except Exception as e:
            print(e)
            break

def orders():
    merged_order = pd.merge(go_sales['order_details'], go_sales['order_header'], on='ORDER_NUMBER')
    merged_order = pd.merge(merged_order, go_sales['product'], on='PRODUCT_NUMBER')

    testdb = sqlite3.connect(r"test.sqlite")
    merged_order.to_sql('ORDER', testdb, if_exists='replace', index=False)

    # Clean Target
    clean_target_table(ssms_conn, 'ORDERS')

    for index, row in merged_order.iterrows():
        try:
            order_id = row['ORDER_DETAIL_CODE']
            product_id = row['PRODUCT_NUMBER']
            staff_id = row['SALES_STAFF_CODE']
            method_id = row['ORDER_METHOD_CODE']
            retailer_id = row['RETAILER_SITE_CODE']
            quantity = row['QUANTITY']
            unit_cost = pd.to_numeric(row['UNIT_COST'])
            unit_sale = pd.to_numeric(row['UNIT_SALE_PRICE'])
            product_margin = row['MARGIN']
            product_cost = pd.to_numeric(row['UNIT_PRICE'])

            # Afgeleide dimensies
            sale_amount = product_cost - unit_sale
            total_profit = sale_amount - unit_cost

            query = "INSERT INTO dbo.ORDERS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            params = (order_id, product_id, staff_id, method_id, retailer_id, quantity, unit_cost, unit_sale, product_margin, product_cost, sale_amount, total_profit)

            ssms_cursor.execute(query, params)
            ssms_conn.commit()
        except Exception as e:
            print(e)
            print(method_id)
            break

course_etl()
satisfaction_type_etl()
sales_staff_etl()
country()
# order_method()
orders()

""" for index, row in go_staff['sales_branch'].iterrows():
    try:
        # Haal de namen van de kolommen op
        values = ', '.join([f"'{row[col]}'" if isinstance(row[col], str) else (str(row[col]) if row[col] is not None else 'NULL') for col in go_staff['sales_branch'].columns])        
        
        # SQL-query
        query = f"INSERT INTO dbo.SALES_BRANCH VALUES ({values})"
        ssms_cursor.execute(query)
        ssms_conn.commit()
    except Exception as e:
        print(e)
        break

for index, row in go_staff['sales_staff'].iterrows():
    try:
        # Haal de namen van de kolommen op
        values = ', '.join([f"'{row[col]}'" if isinstance(row[col], str) else (str(row[col]) if row[col] is not None else 'NULL') for col in go_staff['sales_staff'].columns])        
        
        # Haal de bijbehorende sales_branch op
        sales_branch_code = row['SALES_BRANCH_CODE']
        sales_branch_row = go_staff['sales_branch'][go_staff['sales_branch']['SALES_BRANCH_CODE'] == sales_branch_code].iloc[0]

        # Haal de bijbehorende country op
        country_code = sales_branch_row['COUNTRY_CODE']
        country_row = go_sales['country'][go_sales['country']['COUNTRY_CODE'] == country_code].iloc[0]

        # Voeg de sales_branch en country gegevens toe aan de bestaande values
        values += f", '{sales_branch_row['ADDRESS1']}', '{sales_branch_row['ADDRESS2']}', '{sales_branch_row['CITY']}', '{sales_branch_row['REGION']}', '{sales_branch_row['POSTAL_ZONE']}', '{country_row['COUNTRY_CODE']}', '{country_row['COUNTRY']}', '{country_row['LANGUAGE']}', '{country_row['CURRENCY_NAME']}'"
        values = values.replace('None', 'NULL')
        
        # Voer de INSERT-query uit op de SSMS-database
        query = f"INSERT INTO dbo.rSALES_STAFF VALUES ({values})"
        ssms_cursor.execute(query)
        ssms_conn.commit()
    except Exception as e:
        print(e)
        break """

ssms_conn.close()