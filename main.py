import csv
import json
import re
from pprint import pprint

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


def load_mysql_table(table):
    with open(f"data/{table}.txt", "rt") as file:
        reader = csv.reader(file)
        records = [format_insert_query(record, table) for record in reader]
        insert_query = f"INSERT INTO {table} VALUES {','.join(records)};"
        try:
            with mysql_client.cursor() as cursor:
                cursor.execute(insert_query)
                mysql_client.commit()
                print(f"MySQL table - {table} populated successfully. Records inserted: {len(records)}")
        except pymysql.MySQLError as e:
            print("Error while establishing connection", e)
        finally:
            cursor.close()


def format_as_sql_date(record):
    return f"STR_TO_DATE({record}, '%d-%M-%Y')"


def format_insert_query(record, table):
    record = [re.sub("[\"]", "", item) for item in record]
    if table == "EMPLOYEE":
        record[4] = format_as_sql_date(record[4])
        return f"({','.join(record)})"
    elif table == "DEPARTMENT":
        record[3] = format_as_sql_date(record[3])
        return f"({','.join(record)})"
    else:
        return f"({','.join(record)})"


def fetch_as_document(document_root):
    document_query = None
    with open(f"scripts/{document_root}-as-root.sql", "rt") as query_file:
        document_query = query_file.read()
    try:
        with mysql_client.cursor() as cursor:
            cursor.execute(document_query)
            return [json.loads(row[0]) for row in cursor.fetchall()]
    except pymysql.MySQLError as e:
        print(f"Error while fetching data from MySQL in document format {document_root} as root", e)
    finally:
        cursor.close()


def load_to_mongodb(documents, collection_name):
    # collection names : [projects, employees]
    collection = mongo_client.db2[f"{collection_name}s"]
    collection.delete_many({})
    print(f"MongoDB collection {collection_name}s emptied for fresh insertion")
    [collection.insert_one(document) for document in documents]
    print(f"{len(documents)} documents inserted to the collection: {collection_name}s in MongoDB successfully")


def fetch_from_mongodb(collection_name):
    collection = mongo_client.db2[f"{collection_name}s"]
    documents = collection.find({})
    print(f"Documents retrieved from the collection {collection_name}s in MongoDB:")
    for doc in documents:
        pprint(doc)


mysql_client = pymysql.connect(host=sql_props.host,
                               user=sql_props.user,
                               password=sql_props.password,
                               database=sql_props.dbname)

mongo_client = pymongo.MongoClient(f"mongodb+srv://{mp.user}:{mp.password}@{mp.host}/{mp.dbname}")

# empties the tables so data from files in `data/` directory is freshly inserted
clear_tables()

# Load data from files in `data/` directory to MySQL tables. ORDER IS IMPORTANT!
load_mysql_table("DEPARTMENT")
load_mysql_table("DEPT_LOCATIONS")
load_mysql_table("EMPLOYEE")
load_mysql_table("PROJECT")
load_mysql_table("WORKS_ON")

for root in ["project", "employee", "department"]:
    documents = fetch_as_document(root)
    load_to_mongodb(documents, root)
    fetch_from_mongodb(root)
