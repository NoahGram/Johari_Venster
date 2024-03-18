import pandas as pd
import pyodbc
import sqlite3
import numpy as np
import datetime
from settings import settings, logger

def process():
    try:
        ssms_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + settings.DB['servername'] + 
                            ';DATABASE=' + settings.DB['database'] + ';Trusted_Connection=yes')
        ssms_cursor = ssms_conn.cursor()

        # Voor het geval dat de database nog niet bestaat, maak een nieuwe SQLite-database aan
        sqlite_conn = sqlite3.connect('../data/processed/johari_sqlite.db')
        
        logger.info("Connected to the databases")
    except:
        logger.error("Error connecting to the databases")
        return

    try:
        # Nieuwe dataframes met dummy data
        dbo_product = pd.DataFrame({
            'PRODUCT_id': [1, 2, 3],
            'PRODUCT_name': ['Moondrop Variations', 'Sony IER-Z1R', 'Truthear Nova'],
            'PRODUCT_image': ['moondrop.jpg', 'sony.jpg', 'truthear.jpg'],
            'PRODUCT_LINE_name': ['Moondrop', 'Sony', 'Truthear'],
            'PRODUCT_TYPE_name': ['In-ear monitor', 'In-ear monitor', 'In-ear monitor'],
            'PRODUCT_INTRODUCTION_DATE_date': [datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), datetime.date(2021, 1, 1)],
            'PRODUCT_COST_price': [400, 1100, 180],
            'PRODUCT_MARGIN_dimensions': [0.5, 0.6, 0.7],
            'PRODUCT_LANGUAGE_name': ['English', 'English', 'English'],
        })

        dbo_sales_staff = pd.DataFrame({
            'SALES_STAFF_id': [1, 2, 3],
            'SALES_STAFF_f_name': ['Karel', 'Henk', 'Regen'],
            'SALES_STAFF_l_name': ['Ankerwout', 'Tank', 'Achterstevoren'],
            'SALES_STAFF_phone': ['+316456789', '+316654321', '+316123123'],
            'SALES_STAFF_email': ['k.anker@yandex.ru', 'henk@yahoo.com', 'nee@ger.com'],
            'SALES_STAFF_fax': ['+316456789', '+316654321', '+316123123'],
            'SALES_STAFF_sales_branch_id': [1, 2, 3],
            'SALES_STAFF_POSITION_EN_name': ['Sales Manager', 'Sales Manager', 'Sales Manager'],
            'SALES_STAFF_DATE_HIRED_date': [datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), datetime.date(2021, 1, 1)],
            'SALES_STAFF_EXTENSION_extension': ['+316456789', '+316654321', '+316123123'],
            'SALES_STAFF_SALES_BRANCH_address1': ['Kerkstraat 1', 'Kerkstraat 2', 'Kerkstraat 3'],
            'SALES_STAFF_SALES_BRANCH_address2': ['Kerkstraat 1', 'Kerkstraat 2', 'Kerkstraat 3'],
            'SALES_STAFF_SALES_BRANCH_region': ['Noord', 'Zuid', 'Oost'],
            'SALES_STAFF_SALES_BRANCH_city': ['Amsterdam', 'Rotterdam', 'Utrecht'],
            'SALES_STAFF_SALES_BRANCH_postal_zone': ['1000AA', '2000BB', '3000CC'],
            'SALES_STAFF_COUNTRY_id': [1, 2, 3],
            'SALES_STAFF_COUNTRY_name': ['Netherlands', 'Belgium', 'Germany'],
            'SALES_STAFF_COUNTRY_language': ['Dutch', 'French', 'German'],
            'SALES_STAFF_COUNTRY_currency': ['Euro', 'Euro', 'Euro'],
        })

        dbo_retailer_contact = pd.DataFrame({
            'retailer_contact_contact_id': np.random.randint(1, 100, size=10),
            'retailer_contact_site_id': np.random.randint(1, 100, size=10),
            'retailer_contact_first_name': np.random.choice(['John', 'Jane', 'Jim', 'Jill', 'Joe'], size=10),
            'retailer_contact_last_name': np.random.choice(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown'], size=10),
            'retailer_contact_job_position_en': np.random.choice(['Manager', 'Employee', 'CEO', 'CFO', 'CTO'], size=10),
            'retailer_contact_extension': np.random.randint(1, 100, size=10),
            'retailer_contact_fax': np.random.randint(1, 100, size=10),
            'retailer_contact_email': [f'test{i}@test.com' for i in range(10)],
            'retailer_contact_gender': np.random.choice(['M', 'F'], size=10),
            'retailer_id': np.random.randint(1, 100, size=10),
            'retailer_codemr': np.random.randint(1, 100, size=10),
            'retailer_company_name': [f'Company{i}' for i in range(10)],
            'retailer_age_group_id': np.random.randint(1, 100, size=10),
            'retailer_age_group_upper_age': np.random.randint(30, 60, size=10),
            'retailer_age_group_lower_age': np.random.randint(20, 30, size=10),
            'retailer_sales_demographic_id': np.random.randint(1, 100, size=10),
            'retailer_sales_demographic_codemr': np.random.randint(1, 100, size=10),
            'retailer_sales_demographic_age_group_id': np.random.randint(1, 100, size=10),
            'retailer_sales_demographic_sales_percent': np.random.random(size=10),
            'retailer_sales_territory_id': np.random.randint(1, 100, size=10),
            'retailer_sales_territory_name_en': [f'Territory{i}' for i in range(10)],
            'retailer_country_id': np.random.randint(1, 100, size=10),
            'retailer_country_country_en': [f'Country{i}' for i in range(10)],
            'retailer_country_flag_image': [f'Image{i}' for i in range(10)],
            'retailer_country_sales_territory_id': np.random.randint(1, 100, size=10),
            'retailer_site_id': np.random.randint(1, 100, size=10),
            'retailer_site_retailer_id': np.random.randint(1, 100, size=10),
            'retailer_site_address1': [f'Address{i}' for i in range(10)],
            'retailer_site_address2': [f'Address{i}' for i in range(10)],
            'retailer_site_city': [f'City{i}' for i in range(10)],
            'retailer_site_region': [f'Region{i}' for i in range(10)],
            'retailer_site_postal_zone': [f'Postal{i}' for i in range(10)],
            'retailer_site_country_id': np.random.randint(1, 100, size=10),
            'retailer_site_active_indicator': np.random.randint(0, 1, size=10),
            'retailer_headquarters_codemr': np.random.randint(1, 100, size=10),
            'retailer_headquarters_name': [f'Name{i}' for i in range(10)],
            'retailer_headquarters_address1': [f'Address{i}' for i in range(10)],
            'retailer_headquarters_address2': [f'Address{i}' for i in range(10)],
            'retailer_headquarters_city': [f'City{i}' for i in range(10)],
            'retailer_headquarters_region': [f'Region{i}' for i in range(10)],
            'retailer_headquarters_postal_zone': [f'Postal{i}' for i in range(10)],
            'retailer_headquarters_country_id': np.random.randint(1, 100, size=10),
            'retailer_headquarters_phone': [f'Phone{i}' for i in range(10)],
            'retailer_headquarters_fax': [f'Fax{i}' for i in range(10)],
            'retailer_headquarters_segment_id': np.random.randint(1, 100, size=10),
            'retailer_type_id': np.random.randint(1, 100, size=10),
            'retailer_type_type_en': [f'Type{i}' for i in range(10)],
            'retailer_segment_id': np.random.randint(1, 100, size=10),
            'retailer_segment_language': [f'Language{i}' for i in range(10)],
            'retailer_segment_name': [f'Segment Name{i}' for i in range(10)],
            'retailer_segment_description': [f'Segment Description{i}' for i in range(10)],
        })

        dbo_returned_reason = pd.DataFrame({
            'RETURNED_REASON_id': [1, 2, 3],
            'RETURNED_REASON_DESCRIPTION_name': ['Broken', 'Not satisfied', 'Wrong product'],
        })

        dbo_order_method = pd.DataFrame({
            'ORDER_METHOD_id': [1, 2, 3],
            'ORDER_METHOD_EN_name': ['Online', 'Phone', 'Mail'],
        })

        dbo_course = pd.DataFrame({
            'COURSE_id': [1, 2, 3],
            'COURSE_DESCRIPTION_en': ['Programming', 'Querying', 'Spreadsheets'],
        })

        dbo_satisfaction_type = pd.DataFrame({
            'SATISFACTION_TYPE_id': [1, 2, 3],
            'SATISFACTION_TYPE_DESCRIPTION_name': ['Good', 'Bad', 'Neutral'],
        })

        logger.info("Dataframes created")
    except:
        logger.error("Error creating dataframes")
        return


    # Surrogate keys toevoegen aan de dataframes (plus beredeneringen)

    try:
        # Wanneer deze dataframe samengevoegd wordt met externe bronnen, kan het zijn dat de PK niet meer uniek is of conflicts heeft.
        dbo_product['PRODUCT_SK'] = list(range(1, len(dbo_product['PRODUCT_id']) + 1))

        # Wanneer er herstructurering plaatsvindt in de organisatie, kan het zijn dat de PK niet meer uniek is of conflicts heeft.
        dbo_sales_staff['SALES_STAFF_SK'] = list(range(1, len(dbo_sales_staff['SALES_STAFF_id']) + 1))

        # Een contactpersoon kan van functie veranderen, maar het kan zijn dat je oude data wilt behouden voor bijvoorbeeld trendanalyses.
        dbo_retailer_contact['retailer_contact_SK'] = list(range(1, len(dbo_retailer_contact['retailer_contact_contact_id']) + 1))

        # Je kan in de loop van tijd de beredeneringen willen veranderen. Een voorbeeld hiervan is wanneer je een beschrijving wilt opsplitsen omdat het te vaag is, maar nog steeds de oorspronkelijke PK wilt gebruiken om aan te duiden dat de opgesplitste beschrijvingen bij elkaar horen. Dit mag natuurlijk niet, hierdoor wordt de SK nu gebruikt als de unieke kenmerk.
        dbo_returned_reason['RETURNED_REASON_SK'] = list(range(1, len(dbo_returned_reason['RETURNED_REASON_id']) + 1))

        # Hetzelfde als bij de vorige, maar in plaats van een beschrijving, kan het bijvoorbeeld zijn dat een order methode wordt opgesplitst (zoals Online = Webshop, App, etc.).
        dbo_order_method['ORDER_METHOD_SK'] = list(range(1, len(dbo_order_method['ORDER_METHOD_id']) + 1))

        # Hetzelfde als bij de vorige, maar in plaats van een beschrijving, kan het bijvoorbeeld zijn dat een course wordt opgesplitst (zoals Programming = Python, Java, etc.).
        dbo_course['COURSE_SK'] = list(range(1, len(dbo_course['COURSE_id']) + 1))

        # Hetzelfde als bij de vorige, maar in plaats van een beschrijving, kan het bijvoorbeeld zijn dat een satisfaction type wordt opgesplitst (zoals Good = Very good, Excellent, etc.).
        dbo_satisfaction_type['SATISFACTION_TYPE_SK'] = list(range(1, len(dbo_satisfaction_type['SATISFACTION_TYPE_id']) + 1))

        logger.info("Surrogate keys added to the dataframes")
    except:
        logger.error("Error adding surrogate keys to the dataframes")
        return

    try:
        # Exporteer de dataframes naar de SQLite-database
        dbo_product.to_sql('PRODUCT', sqlite_conn, if_exists='replace', index=False)
        dbo_sales_staff.to_sql('SALES_STAFF', sqlite_conn, if_exists='replace', index=False)
        dbo_retailer_contact.to_sql('RETAILER_CONTACT', sqlite_conn, if_exists='replace', index=False)
        dbo_returned_reason.to_sql('RETURNED_REASON', sqlite_conn, if_exists='replace', index=False)
        dbo_order_method.to_sql('ORDER_METHOD', sqlite_conn, if_exists='replace', index=False)
        dbo_course.to_sql('COURSE', sqlite_conn, if_exists='replace', index=False)
        dbo_satisfaction_type.to_sql('SATISFACTION_TYPE', sqlite_conn, if_exists='replace', index=False)
        
        logger.info("Dataframes exported to the SQLite database")
    except:
        logger.error("Error exporting the dataframes to the SQLite database")
        return


    # %% Zet alle gegevens om van de SQLite .db bestand naar de SSMS database
    # Itereer over de rijen van iedere dataframe en voeg elke record toe aan de SSMS-database

    try:
        for index, row in dbo_product.iterrows():
            try:
                query = f"INSERT INTO dbo.rPRODUCT VALUES ({index}, '{row['PRODUCT_name']}', '{row['PRODUCT_image']}', '{row['PRODUCT_LINE_name']}', '{row['PRODUCT_TYPE_name']}', '{row['PRODUCT_INTRODUCTION_DATE_date']}', {row['PRODUCT_COST_price']}, {row['PRODUCT_MARGIN_dimensions']}, '{row['PRODUCT_LANGUAGE_name']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['PRODUCT_id']} added to rPRODUCT")
            except Exception as e:
                logger.error(f"Error adding record {row['PRODUCT_id']} to rPRODUCT")
                print(e)
                break

        for index, row in dbo_sales_staff.iterrows():
            try:
                query = f"INSERT INTO dbo.rSALES_STAFF VALUES ({row['SALES_STAFF_id']}, '{row['SALES_STAFF_f_name']}', '{row['SALES_STAFF_l_name']}', '{row['SALES_STAFF_phone']}', '{row['SALES_STAFF_email']}', '{row['SALES_STAFF_fax']}', {row['SALES_STAFF_sales_branch_id']}, '{row['SALES_STAFF_POSITION_EN_name']}', '{row['SALES_STAFF_DATE_HIRED_date']}', '{row['SALES_STAFF_EXTENSION_extension']}', '{row['SALES_STAFF_SALES_BRANCH_address1']}', '{row['SALES_STAFF_SALES_BRANCH_address2']}', '{row['SALES_STAFF_SALES_BRANCH_region']}', '{row['SALES_STAFF_SALES_BRANCH_city']}', '{row['SALES_STAFF_SALES_BRANCH_postal_zone']}', {row['SALES_STAFF_COUNTRY_id']}, '{row['SALES_STAFF_COUNTRY_name']}', '{row['SALES_STAFF_COUNTRY_language']}', '{row['SALES_STAFF_COUNTRY_currency']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['SALES_STAFF_id']} added to rSALES_STAFF")
            except Exception as e:
                logger.error(f"Error adding record {row['SALES_STAFF_id']} to rSALES_STAFF")
                print(e)
                break

        for index, row in dbo_retailer_contact.iterrows():
            try:
                query = f"INSERT INTO dbo.RETAILER_CONTACT VALUES ({index}, {row['retailer_contact_site_id']}, '{row['retailer_contact_first_name']}', '{row['retailer_contact_last_name']}', '{row['retailer_contact_job_position_en']}', {row['retailer_contact_extension']}, {row['retailer_contact_fax']}, '{row['retailer_contact_email']}', '{row['retailer_contact_gender']}', {row['retailer_id']}, {row['retailer_codemr']}, '{row['retailer_company_name']}', {row['retailer_age_group_id']}, {row['retailer_age_group_upper_age']}, {row['retailer_age_group_lower_age']}, {row['retailer_sales_demographic_id']}, {row['retailer_sales_demographic_codemr']}, {row['retailer_sales_demographic_age_group_id']}, {row['retailer_sales_demographic_sales_percent']}, {row['retailer_sales_territory_id']}, '{row['retailer_sales_territory_name_en']}', {row['retailer_country_id']}, '{row['retailer_country_country_en']}', '{row['retailer_country_flag_image']}', {row['retailer_country_sales_territory_id']}, {row['retailer_site_id']}, {row['retailer_site_retailer_id']}, '{row['retailer_site_address1']}', '{row['retailer_site_address2']}', '{row['retailer_site_city']}', '{row['retailer_site_region']}', '{row['retailer_site_postal_zone']}', {row['retailer_site_country_id']}, {row['retailer_site_active_indicator']}, {row['retailer_headquarters_codemr']}, '{row['retailer_headquarters_name']}', '{row['retailer_headquarters_address1']}', '{row['retailer_headquarters_address2']}', '{row['retailer_headquarters_city']}', '{row['retailer_headquarters_region']}', '{row['retailer_headquarters_postal_zone']}', {row['retailer_headquarters_country_id']}, '{row['retailer_headquarters_phone']}', '{row['retailer_headquarters_fax']}', {row['retailer_headquarters_segment_id']}, {row['retailer_type_id']}, '{row['retailer_type_type_en']}', {row['retailer_segment_id']}, '{row['retailer_segment_language']}', '{row['retailer_segment_name']}', '{row['retailer_segment_description']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['retailer_contact_contact_id']} added to RETAILER_CONTACT")
            except Exception as e:
                logger.error(f"Error adding record {row['retailer_contact_contact_id']} to RETAILER_CONTACT")
                print(e)
                break

        for index, row in dbo_returned_reason.iterrows():
            try:
                query = f"INSERT INTO dbo.RETURN_REASON VALUES ({row['RETURNED_REASON_id']}, '{row['RETURNED_REASON_DESCRIPTION_name']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['RETURNED_REASON_id']} added to RETURN_REASON")
            except Exception as e:
                logger.error(f"Error adding record {row['RETURNED_REASON_id']} to RETURN_REASON")
                print(e)
                break

        for index, row in dbo_order_method.iterrows():
            try:
                query = f"INSERT INTO dbo.ORDER_METHOD VALUES ({row['ORDER_METHOD_id']}, '{row['ORDER_METHOD_EN_name']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['ORDER_METHOD_id']} added to ORDER_METHOD")
            except Exception as e:
                logger.error(f"Error adding record {row['ORDER_METHOD_id']} to ORDER_METHOD")
                print(e)
                break

        for index, row in dbo_course.iterrows():
            try:
                query = f"INSERT INTO dbo.COURSE VALUES ({row['COURSE_id']}, '{row['COURSE_DESCRIPTION_en']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['COURSE_id']} added to COURSE")
            except Exception as e:
                logger.error(f"Error adding record {row['COURSE_id']} to COURSE")
                print(e)
                break

        for index, row in dbo_satisfaction_type.iterrows():
            try:
                query = f"INSERT INTO dbo.SATISFACTION_TYPE VALUES ({row['SATISFACTION_TYPE_id']}, '{row['SATISFACTION_TYPE_DESCRIPTION_name']}')"
                ssms_cursor.execute(query)
                ssms_conn.commit()
                logger.info(f"Record id:{row['SATISFACTION_TYPE_id']} added to SATISFACTION_TYPE")
            except Exception as e:
                logger.error(f"Error adding record {row['SATISFACTION_TYPE_id']} to SATISFACTION_TYPE")
                print(e)
                break
        
        logger.info("Dataframes exported to the SSMS database")
    except:
        logger.error("Error exporting the dataframes to the SSMS database")
        return

    # %% Sluit connecties met alle databases
        
    sqlite_conn.close()
    ssms_conn.close()


