import csv
import re

import pymysql


def clear_tables():
    connection = pymysql.connect(host="34.86.150.93", user="root", password="DB2@SUM2020", database="project2")
    tables_in_order = ["WORKS_ON", "DEPT_LOCATIONS", "PROJECT", "EMPLOYEE", "DEPARTMENT"]
    try:
        with connection.cursor() as cursor:
            [cursor.execute(f"DELETE FROM {table};") for table in tables_in_order]
            connection.commit()
            print("All tables emptied successfully")
    except pymysql.MySQLError:
        print(f"Error while emptying tables")


def load_data(table):
    connection = pymysql.connect(host="34.86.150.93", user="root", password="DB2@SUM2020", database="project2")
    with open(f"data/{table}.txt", "rt") as file:
        reader = csv.reader(file)
        records = [format_insert_query(record, table) for record in reader]
        insert_query = f"INSERT INTO {table} VALUES {','.join(records)};"
        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_query)
                connection.commit()
                print(f"Table: {table} populated successfully")
        except pymysql.MySQLError as e:
            print("Error while establishing connection", e)
        finally:
            cursor.close()


def format_as_sql_date(record):
    return f"STR_TO_DATE({record}, '%d-%M-%Y')"


def format_insert_query(record, tablename):
    record = [re.sub("[\"]", "", item) for item in record]
    if tablename == "EMPLOYEE":
        record[4] = format_as_sql_date(record[4])
        return f"({','.join(record)})"
    elif tablename == "DEPARTMENT":
        record[3] = format_as_sql_date(record[3])
        return f"({','.join(record)})"
    else:
        return f"({','.join(record)})"


clear_tables()
load_data("DEPARTMENT")
load_data("DEPT_LOCATIONS")
load_data("EMPLOYEE")
load_data("PROJECT")
load_data("WORKS_ON")
