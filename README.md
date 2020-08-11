<h1 align="center">
    CSE-5331 | PROJECT 2
</h1>

## Description

In this project, we learn how to export data from a Flat/Relational to a Document-oriented format (JSON and XML), 
and import this to MongoDB. The objective of this project is to understand the differences of storing data in a RDBMS vs Document-based NOSQL System. Additionally, we look at parsing the JSON from MongoDB into an XML which is often useful in while building APIs and even migrating to another RDBMS.

> Add description about how we are converting the tabular data to the JSON and the JSON to XML

## Contributors

Student ID | Student Name | Contribution
---|---|---
1001767678 | Harshavardhan Ramamurthy | MySQL setup, MongoDB setup, create-table script, clear_data(), load_mysql_table(), Project as root, load_to_mongodb(), fetch_as_relational(), Department as root
1001767677 | Karan Rajpal | Documentation, format_as_xml(), Main-driver, Employee-as-root

## Environment

1. Python - 3.7

2. Libraries
    
    * pymysql~=0.9.3
    * dnspython~=1.16.0
    * pymongo~=3.9.0
    * tabulate~=0.8.3
    
3. MySQL - 8

    **MySQL (5.7.22 or higher) is required since the support for `JSON_OBJECTAGG` function was added after v5.7.22 and is used in this project**

4. MongoDB - 4.2.8

    
## Project Workflow

1. Data from text-files are loaded to their respective tables in MySQL
2. Data is retrieved from MySQL using `JOIN`s
3. Data retrieved in Document format(JSON) with `PROJECT` and `EMPLOYEE` respectively as root
4. Data in document format is loaded to MongoDB and retrieved

### `PROJECT` as root
In relational format, the project name, number & department name are redundant for every employee that works on it. 
Therefore the employee details are nested in the `project` document using `JSON_ARRAYAGG` function in 
SQL by `GROUP`ing `BY` project name, number & department name. 

### `EMPLOYEE` as root
In relational format, the employee lname, fname, department name are redundant for every project that the employee works on. 
Therefore the project details are nested in the `employee` document using `JSON_ARRAYAGG` function in 
SQL by `GROUP`ing `BY` employee lname, fname, department name.

Reference: [`JSON_ARRAYAGG`]()

## Instructions

> IMPORTANT NOTICE: The project relies heavily on file-names. Please DO NOT change any filenames in the project.  

**The data required by the `DEPARTMENT`, `DEPT_LOCATIONS`, `EMPLOYEE`, `PROJECT`, and `WORKS_ON ` tables are present in the respective text files under the `data/` directory**

**The SQL scripts required to create the necessary tables, Insert the necessary data and to convert the query results to JSON objects are present in the `scripts/` directory**

> We've set-up MySQL and MongoDB on cloud with all the necessary tables created and with sufficient privileges for the user.
 
1. Install the necessary dependencies by executing `pip install -r requirements.txt` in the console

2. Execute the program by running `python main.py` in the console and follow the instructions on the screen

#### If you want to test/run the project with your own instance of MySQL and MongoDB, then

1. Create a dedicated database in MySQL and MongoDB for this project

2. Create the `DEPARTMENT`, `DEPT_LOCATIONS`, `EMPLOYEE`, `PROJECT`, and `WORKS_ON ` tables using `scripts/create-tables.sql`

3. Ensure that the `user` has sufficient privileges(`INSERT` and `DELETE`) on the database in both MySQL and MongoDB.

4. Add the credentials for MySQL and MongoDB in `config.py`.

5. Execute the program by running `python main.py` in the console and follow the instructions on the screen

### Output
   ```
   ❯ python main.py
   Data loaded to MySQL successfully. Query the above tables in project2 database in MySQL to verify.
   Press ENTER key to display data in relational format for project
   +-----------------+------------------+----------------+-------------+-------------+---------+
   | Project Name    |   Project Number | Dept. Name     | Emp Lname   | Emp Fname   |   Hours |
   |-----------------+------------------+----------------+-------------+-------------+---------|
   | Advertizing     |               70 | HR             | Liang       | Percy       |      10 |
   | Computerization |               10 | Administration | Koelbel     | Richard     |      35 |
   | Computerization |               10 | Administration | Jabbar      | Ahmad       |      35 |
   | Computerization |               10 | Administration | Zelaya      | Alicia      |      10 |
   | ConfigMgmt      |               11 | Software       | Hall        | Debra       |      20 |
   .............................................................................................
                                             ....
   .............................................................................................
   | ProductZ        |                3 | Research       | Wong        | Franklin    |      10 |
   | ProductZ        |                3 | Research       | Narayan     | Ramesh      |      40 |
   | Reorganization  |               20 | Headquarters   | Borg        | James       |       5 |
   | SearchEngine    |               22 | Software       | Geller      | Zach        |      30 |
   | SearchEngine    |               22 | Software       | Wolowitz    | Penny       |       4 |
   +-----------------+------------------+----------------+-------------+-------------+---------+
   Press ENTER key to load data to MongoDB in document format for project
   MongoDB collection projects emptied for fresh insertion
   17 documents inserted to the projects collection in MongoDB successfully
   Press ENTER key to display data in JSON format for project
   Documents retrieved from the collection projects in MongoDB:
   {'DNAME': 'HR',
    'EMPLOYEES': [{'EMP_FNAME': 'Percy', 'EMP_LNAME': 'Liang', 'HOURS': 10}],
    'PNAME': 'Advertizing',
    'PNUMBER': 70,
    '_id': ObjectId('5f31c694c2210e84ef83adc8')}
   {'DNAME': 'Administration',
    'EMPLOYEES': [{'EMP_FNAME': 'Richard', 'EMP_LNAME': 'Koelbel', 'HOURS': 35},
                  {'EMP_FNAME': 'Ahmad', 'EMP_LNAME': 'Jabbar', 'HOURS': 35},
                  {'EMP_FNAME': 'Alicia', 'EMP_LNAME': 'Zelaya', 'HOURS': 10}],
    'PNAME': 'Computerization',
    'PNUMBER': 10,
    '_id': ObjectId('5f31c694c2210e84ef83adc9')}
   ..........
   ..........
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Zach', 'EMP_LNAME': 'Geller', 'HOURS': 30},
                  {'EMP_FNAME': 'Penny', 'EMP_LNAME': 'Wolowitz', 'HOURS': 4}],
    'PNAME': 'SearchEngine',
    'PNUMBER': 22,
    '_id': ObjectId('5f31c695c2210e84ef83add8')}
   ------------------------------ FOR EXTRA CREDIT : XML document format ------------------------------
   Press ENTER key to display data in XML format for project
   <?xml version="1.0" encoding="UTF-8"?>
   <ALL_PROJECTS>
   	<PROJECT PNUMBER=70 PNAME="Advertizing">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Liang" EMP_FNAME="Percy" HOURS=10 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=10 PNAME="Computerization">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Koelbel" EMP_FNAME="Richard" HOURS=35 />
   			<EMPLOYEE EMP_LNAME="Jabbar" EMP_FNAME="Ahmad" HOURS=35 />
   			<EMPLOYEE EMP_LNAME="Zelaya" EMP_FNAME="Alicia" HOURS=10 />
   		</EMPLOYEES>
   	</PROJECT>
   	........
      	........
   	<PROJECT PNUMBER=22 PNAME="SearchEngine">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Geller" EMP_FNAME="Zach" HOURS=30 />
   			<EMPLOYEE EMP_LNAME="Wolowitz" EMP_FNAME="Penny" HOURS=4 />
   		</EMPLOYEES>
   	</PROJECT>
   </ALL_PROJECTS>
   Press ENTER key to display data in relational format for employee
   +-------------+-------------+----------------+-----------------+------------------+---------+
   | Emp Lname   | Emp Fname   | Dept. Name     | Project Name    |   Project Number |   Hours |
   |-------------+-------------+----------------+-----------------+------------------+---------|
   | Barbara     | Jose        | Software       | Middleware      |               63 |      40 |
   | Bays        | Bonnie      | Hardware       | InkjetPrinters  |               91 |      40 |
   | Best        | Alec        | Hardware       | InkjetPrinters  |               91 |      40 |
   | Borg        | James       | Headquarters   | Reorganization  |               20 |       5 |
   | Burklow     | Cindy       | Software       | Middleware      |               63 |      25 |
   | Chase       | Jeff        | Software       | Middleware      |               63 |      46 |
   | English     | Joyce       | Research       | ProductX        |                1 |      20 |
   .............................................................................................
                                    ..................
                                    ..................
   .............................................................................................
   | Wallace     | Jennifer    | Administration | Newbenefits     |               30 |      20 |
   | Wolowitz    | Penny       | Software       | SearchEngine    |               22 |       4 |
   | Wong        | Franklin    | Research       | ProductY        |                2 |      10 |
   | Wong        | Franklin    | Research       | ProductZ        |                3 |      10 |
   | Yu          | Alex        | Software       | DataMining      |               13 |      18 |
   | Zelaya      | Alicia      | Administration | Newbenefits     |               30 |      30 |
   | Zelaya      | Alicia      | Administration | Computerization |               10 |      10 |
   +-------------+-------------+----------------+-----------------+------------------+---------+
   Press ENTER key to load data to MongoDB in document format for employee
   MongoDB collection employees emptied for fresh insertion
   35 documents inserted to the employees collection in MongoDB successfully
   Press ENTER key to display data in JSON format for employee
   Documents retrieved from the collection employees in MongoDB:
   
   {'DNAME': 'Software',
    'EMP_FNAME': 'Jose',
    'EMP_LNAME': 'Barbara',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'Middleware', 'PNUMBER': 63}],
    '_id': ObjectId('5f31c698c2210e84ef83add9')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Bonnie',
    'EMP_LNAME': 'Bays',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'InkjetPrinters', 'PNUMBER': 91}],
    '_id': ObjectId('5f31c698c2210e84ef83adda')}
   .........
   .........
   {'DNAME': 'Software',
    'EMP_FNAME': 'Alex',
    'EMP_LNAME': 'Yu',
    'PROJECTS': [{'HOURS': 18, 'PNAME': 'DataMining', 'PNUMBER': 13}],
    '_id': ObjectId('5f31c699c2210e84ef83adfa')}
   {'DNAME': 'Administration',
    'EMP_FNAME': 'Alicia',
    'EMP_LNAME': 'Zelaya',
    'PROJECTS': [{'HOURS': 30, 'PNAME': 'Newbenefits', 'PNUMBER': 30},
                 {'HOURS': 10, 'PNAME': 'Computerization', 'PNUMBER': 10}],
    '_id': ObjectId('5f31c699c2210e84ef83adfb')}
   
   ------------------------------ FOR EXTRA CREDIT : XML document format ------------------------------
   Press ENTER key to display data in XML format for employee
   
   <?xml version="1.0" encoding="UTF-8"?>
   <ALL_EMPLOYEES>
   	<EMPLOYEE EMP_LNAME="Barbara" EMP_FNAME="Jose" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="Middleware" PNUMBER=63 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	.........
   	.........
   	<EMPLOYEE EMP_LNAME="Zelaya" EMP_FNAME="Alicia" DNAME="Administration">
   		<PROJECTS>
   			<PROJECT PNAME="Newbenefits" PNUMBER=30 HOURS=30 />
   			<PROJECT PNAME="Computerization" PNUMBER=10 HOURS=10 />
   		</PROJECTS>
   	</EMPLOYEE>
   </ALL_EMPLOYEES>
   
   Press ENTER key to display data in relational format for department
   +----------------+----------------+-----------------+-----------------+-------------+-------------+--------------+
   | Dept. Name     |   Dept. Number | Manager Lname   | Manager Fname   | Emp Lname   | Emp Fname   |   Emp Salary |
   |----------------+----------------+-----------------+-----------------+-------------+-------------+--------------|
   | Administration |              4 | Wallace         | Jennifer        | Holmes      | Wilson      |        72500 |
   | Administration |              4 | Wallace         | Jennifer        | Jabbar      | Ahmad       |        25000 |
   ..................................................................................................................
                                            ..................
                                            ..................
   ..................................................................................................................
   | Software       |              6 | James           | Jared           | Sheen       | Jake        |        52000 |
   | Software       |              6 | James           | Jared           | Wolowitz    | Penny       |        17000 |
   | Software       |              6 | James           | Jared           | Yu          | Alex        |        50000 |
   +----------------+----------------+-----------------+-----------------+-------------+-------------+--------------+
   
   Press ENTER key to load data to MongoDB in document format for department
   MongoDB collection departments emptied for fresh insertion
   8 documents inserted to the departments collection in MongoDB successfully
   Press ENTER key to display data in JSON format for department
   
   Documents retrieved from the collection departments in MongoDB:
   
   {'DNAME': 'Administration',
    'DNUMBER': 4,
    'EMPLOYEES': [{'EMP_FNAME': 'Cameron',
                   'EMP_LNAME': 'Thirteen',
                   'EMP_SALARY': 80000},
                  {'EMP_FNAME': 'Richard',
                   .............
                   .............
                   'EMP_SALARY': 25000},
                  {'EMP_FNAME': 'Alicia',
                   'EMP_LNAME': 'Zelaya',
                   'EMP_SALARY': 25000}],
    'MGR_FNAME': 'Jennifer',
    'MGR_LNAME': 'Wallace',
    '_id': ObjectId('5f31c69ec2210e84ef83adfc')}
   .........
   .........
   {'DNAME': 'Software',
    'DNUMBER': 6,
    'EMPLOYEES': [{'EMP_FNAME': 'John', 'EMP_LNAME': 'Ed', 'EMP_SALARY': 30000},
                  {'EMP_FNAME': 'Christina',
                   'EMP_LNAME': 'Hisel',
                   'EMP_SALARY': 45000},
                  ............
                  ............
                  {'EMP_FNAME': 'Alex', 'EMP_LNAME': 'Yu', 'EMP_SALARY': 50000},
                  {'EMP_FNAME': 'Debra',
                   'EMP_LNAME': 'Hall',
                   'EMP_SALARY': 30000}],
    'MGR_FNAME': 'Jared',
    'MGR_LNAME': 'James',
    '_id': ObjectId('5f31c69ec2210e84ef83ae03')}
   ------------------------------ FOR EXTRA CREDIT : XML document format ------------------------------
   Press ENTER key to display data in XML format for department
   <?xml version="1.0" encoding="UTF-8"?>
   <ALL_DEPARTMENTS>
   	<DEPARTMENT DNAME="Administration" DNUMBER="4" MGR_LNAME="Wallace" MGR_FNAME="Jennifer">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Thirteen" EMP_FNAME="Cameron" EMP_SALARY=80000 />
   			<EMPLOYEE EMP_LNAME="Koelbel" EMP_FNAME="Richard" EMP_SALARY=85000 />
   			<EMPLOYEE EMP_LNAME="Holmes" EMP_FNAME="Wilson" EMP_SALARY=72500 />
   			<EMPLOYEE EMP_LNAME="Wallace" EMP_FNAME="Jennifer" EMP_SALARY=43000 />
   			<EMPLOYEE EMP_LNAME="Jabbar" EMP_FNAME="Ahmad" EMP_SALARY=25000 />
   			<EMPLOYEE EMP_LNAME="Zelaya" EMP_FNAME="Alicia" EMP_SALARY=25000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
           ........
           ........
           ........
   	<DEPARTMENT DNAME="Software" DNUMBER="6" MGR_LNAME="James" MGR_FNAME="Jared">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Ed" EMP_FNAME="John" EMP_SALARY=30000 />
   			<EMPLOYEE EMP_LNAME="Hisel" EMP_FNAME="Christina" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="Sheen" EMP_FNAME="Jake" EMP_SALARY=52000 />
   			................
   			................
   			................
   			<EMPLOYEE EMP_LNAME="Yu" EMP_FNAME="Alex" EMP_SALARY=50000 />
   			<EMPLOYEE EMP_LNAME="Hall" EMP_FNAME="Debra" EMP_SALARY=30000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   </ALL_DEPARTMENTS>
   ```

## TODO

- Fix XML export
- Uncomment load data code in main.py
- Update contributions
- Add description about how we are converting the tabular data to the JSON and the JSON to XML