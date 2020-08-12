import csv
import json
import re
from pprint import pprint

import pymongo
import pymysql
from tabulate import tabulate

from config import MongoProps as mp
from config import MySQLProps as sql_props


def clear_tables():
    tables_in_order = ["WORKS_ON", "DEPT_LOCATIONS", "PROJECT", "EMPLOYEE", "DEPARTMENT"]
    try:
        with mysql_client.cursor() as cursor:
            [cursor.execute(f"DELETE FROM {table};") for table in tables_in_order]
            mysql_client.commit()
            print("All tables in MySQL emptied for fresh insertion of data")
    except pymysql.MySQLError as e:
        print(f"Error while emptying tables", e)
    finally:
        cursor.close()


def load_mysql_table(table):
    with open(f"data/{table}.txt", "rt") as file:
        reader = csv.reader(file)
        records = [format_insert_query(record, table) for record in reader]
        insert_query = f"INSERT INTO {table} VALUES {','.join(records)};"
        try:
            with mysql_client.cursor() as cursor:
                num_rows_inserted = cursor.execute(insert_query)
                mysql_client.commit()
                print(f"\t{num_rows_inserted} rows inserted to {table} table in MySQL")
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


def fetch_as_relational(relational_root):
    document_query = None
    with open(f"scripts/{relational_root}-as-root-relational.sql", "rt") as query_file:
        document_query = query_file.read()
    try:
        with mysql_client.cursor() as cursor:
            cursor.execute(document_query)
            return cursor.fetchall()
    except pymysql.MySQLError as e:
        print(f"Error while fetching data from MySQL in relational format {relational_root} as root", e)
    finally:
        cursor.close()


def load_to_mongodb(documents, collection_name):
    # collection names : [projects, employees]
    collection = mongo_client.db2[f"{collection_name}s"]
    collection.delete_many({})
    print(f"MongoDB collection {collection_name}s emptied for fresh insertion")
    [collection.insert_one(document) for document in documents]
    print(f"{len(documents)} documents inserted to the {collection_name}s collection in MongoDB successfully")


def fetch_from_mongodb(collection_name):
    collection = mongo_client.db2[f"{collection_name}s"]
    documents = collection.find({})
    print(f"Documents retrieved from the collection {collection_name}s in MongoDB:")
    res = []
    for doc in documents:
        pprint(doc)
        res.append(doc)
    return res


def format_as_xml(documents, root):
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n'
    if root == "project":
        children = []
        xml += "<ALL_PROJECTS>"
        for project in documents:
            pnumber = project["PNUMBER"]
            pname = project["PNAME"]
            p = f'\n\t<PROJECT PNUMBER={pnumber} PNAME="{pname}">\n'
            p += f"\t\t<EMPLOYEES>\n"
            for emp in project["EMPLOYEES"]:
                emp_lname = emp["EMP_LNAME"]
                emp_fname = emp["EMP_FNAME"]
                hours = emp["HOURS"]
                p += f'\t\t\t<EMPLOYEE EMP_LNAME="{emp_lname}" EMP_FNAME="{emp_fname}" HOURS={hours} />\n'
            p += f"\t\t</EMPLOYEES>"
            p += f"\n\t</PROJECT>"
            children.append(p)
        xml += "\n".join(children)
        xml += "\n</ALL_PROJECTS>"
        return xml

    elif root == "employee":
        children = []
        xml += "\n<ALL_EMPLOYEES>"
        for employee in documents:
            emp_lname = employee["EMP_LNAME"]
            emp_fname = employee["EMP_FNAME"]
            dname = employee["DNAME"]
            e = f'\n\t<EMPLOYEE EMP_LNAME="{emp_lname}" EMP_FNAME="{emp_fname}" DNAME="{dname}">\n'
            e += f'\t\t<PROJECTS>\n'
            for project in employee["PROJECTS"]:
                pname = project["PNAME"]
                pnum = project["PNUMBER"]
                hours = project["HOURS"]
                e += f'\t\t\t<PROJECT PNAME="{pname}" PNUMBER={pnum} HOURS={hours} />\n'
            e += "\t\t</PROJECTS>"
            e += "\n\t</EMPLOYEE>"
            children.append(e)
        xml += "\n".join(children)
        xml += "\n</ALL_EMPLOYEES>"
        return xml

    elif root == "department":
        children = []
        xml += "\n<ALL_DEPARTMENTS>"
        for dept in documents:
            dname = dept["DNAME"]
            dnumber = dept["DNUMBER"]
            mgr_lname = dept["MGR_LNAME"]
            mgr_fname = dept["MGR_FNAME"]
            d = f'\n\t<DEPARTMENT DNAME="{dname}" DNUMBER="{dnumber}" MGR_LNAME="{mgr_lname}" MGR_FNAME="{mgr_fname}">\n'
            d += f"\t\t<EMPLOYEES>\n"
            for emp in dept["EMPLOYEES"]:
                emp_lname = emp["EMP_LNAME"]
                emp_fname = emp["EMP_FNAME"]
                salary = emp["EMP_SALARY"]
                d += f'\t\t\t<EMPLOYEE EMP_LNAME="{emp_lname}" EMP_FNAME="{emp_fname}" EMP_SALARY={salary} />\n'
            d += "\t\t</EMPLOYEES>"
            d += "\n\t</DEPARTMENT>"
            children.append(d)
        xml += "\n".join(children)
        xml += "\n</ALL_DEPARTMENTS>"
        return xml
    print("Unknown document root")
    return None


header_lookup = {
    "department": [
        "Dept. Name", "Dept. Number", "Manager Lname",
        "Manager Fname", "Emp Lname", "Emp Fname", "Emp Salary"
    ],
    "employee": [
        "Emp Lname", "Emp Fname", "Dept. Name",
        "Project Name", "Project Number", "Hours"
    ],
    "project": [
        "Project Name", "Project Number", "Dept. Name",
        "Emp Lname", "Emp Fname", "Hours"
    ]

}
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

print(f"Data loaded to MySQL successfully. Query the above tables in {sql_props.dbname} database in MySQL to verify.")

for root in ["project", "employee", "department"]:
    input(f"\nPress ENTER key to display data in relational format for {root}")
    print(tabulate(fetch_as_relational(root), headers=header_lookup[root], tablefmt="psql"))
    input(f"\nPress ENTER key to load data to MongoDB in document format for {root}")
    documents = fetch_as_document(root)
    load_to_mongodb(documents, root)
    input(f"\nPress ENTER key to display data in JSON format for {root}")
    documents = fetch_from_mongodb(root)
    print(f"{'-' * 30} FOR EXTRA CREDIT : XML document format {'-' * 30}")
    input(f"\nPress ENTER key to display data in XML format for {root}")
    print(format_as_xml(documents, root))

mysql_client.close()
mongo_client.close()
