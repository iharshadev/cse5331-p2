import csv
import json
import re

import pymongo
import pymysql

from config import MongoProps as mp
from config import MySQLProps as sql_props


def clear_tables():
    tables_in_order = ["WORKS_ON", "DEPT_LOCATIONS", "PROJECT", "EMPLOYEE", "DEPARTMENT"]
    try:
        with mysql_client.cursor() as cursor:
            [cursor.execute(f"DELETE FROM {table};") for table in tables_in_order]
            mysql_client.commit()
            print("All tables in MySQL emptied successfully")
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
            with mysql_client.cursor() as cursor:
                cursor.execute(insert_query)
                mysql_client.commit()
                print(f"MySQL table - {table} populated successfully")
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


def fetch_as_document(root):
    document_query = None
    with open(f"scripts/{root}-as-root.sql", "rt") as query_file:
        document_query = query_file.read()
    try:
        with mysql_client.cursor() as cursor:
            cursor.execute(document_query)
            return [json.loads(row[0]) for row in cursor.fetchall()]
    except pymysql.MySQLError as e:
        print(f"Error while fetching data from MySQL in document format {root} as root", e)
    finally:
        cursor.close()


def load_to_mongodb(documents, collection_name):
    # collection names : [projects, employees]
    collection = mongo_client.db2[f"{collection_name}s"]
    collection.delete_many({})
    print(f"MongoDB collection {collection_name}s emptied for fresh insertion")
    [collection.insert_one(document) for document in documents]
    print(f"{len(documents)} documents inserted to the collection: {collection_name}s in MongoDB successfully")


mysql_client = pymysql.connect(host=sql_props.host,
                               user=sql_props.user,
                               password=sql_props.password,
                               database=sql_props.dbname)

mongo_client = pymongo.MongoClient(f"mongodb+srv://{mp.user}:{mp.password}@{mp.host}/{mp.dbname}")

# empties the tables so data is freshly populated
clear_tables()

# Load data to MySQL tables. ORDER IS IMPORTANT
load_data("DEPARTMENT")
load_data("DEPT_LOCATIONS")
load_data("EMPLOYEE")
load_data("PROJECT")
load_data("WORKS_ON")

project_documents = fetch_as_document("project")
load_to_mongodb(project_documents, "project")

employee_documents = fetch_as_document("employee")
load_to_mongodb(employee_documents, "employee")
