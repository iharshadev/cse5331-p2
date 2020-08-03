import csv
import re

import pymysql

from config import MySQLProps as props


def clear_tables():
    tables_in_order = ["WORKS_ON", "DEPT_LOCATIONS", "PROJECT", "EMPLOYEE", "DEPARTMENT"]
    try:
        with connection.cursor() as cursor:
            [cursor.execute(f"DELETE FROM {table};") for table in tables_in_order]
            connection.commit()
            print("All tables emptied successfully")
    except pymysql.MySQLError:
        print(f"Error while emptying tables")
    finally:
        cursor.close()


def load_data(table):
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


def load_to_mongodb(root):
    document_query = None
    with open(f"scripts/{root}-as-root.sql", "rt") as query_file:
        document_query = query_file.read()
    try:
        with connection.cursor() as cursor:
            cursor.execute(document_query)
            documents = cursor.fetchall()
            for document in documents:
                print(document[0])

    except pymysql.MySQLError:
        print("Error while retrieving project document from MySQL")


connection = pymysql.connect(host=props.host,
                             user=props.user,
                             password=props.password,
                             database=props.dbname)
# empties the tables so data is freshly populated
clear_tables()
load_data("DEPARTMENT")
load_data("DEPT_LOCATIONS")
load_data("EMPLOYEE")
load_data("PROJECT")
load_data("WORKS_ON")

load_to_mongodb("project")
print("//////////////////////")
load_to_mongodb("employee")
