<h1 align="center">
    CSE-5331 | PROJECT 2
</h1>
## Description

In this project, we learn how to export data from SQL to a JSON, import this JSON to MongoDB. The objective of this project is to understand the differences of storing data in a RDBMS vs Document-based NOSQL System. Additionally, we look at parsing the JSON from MongoDB into an XML which is often useful in while building APIs and even migrating to another RDBMS.

> Add description about how we are converting the tabular data to the JSON and the JSON to XML

## Contributors

Student ID | Student Name | Contribution
---|---|---
1001767678 | Harshavardhan Ramamurthy | MySQL setup, MongoDB setup, create-table script, clear_data(), load_mysql_table(), fetch_as_document(), load_to_mongodb(), fetch_as_relational(), format_as_xml(), main driver
1001767677 | Karan Rajpal |  



## Environment

1. Python - 3.7

2. Libraries
    
    * pymysql~=0.9.3
    * dnspython~=1.16.0
    * pymongo~=3.9.0
    * tabulate~=0.8.3
    
3. MySQL - 8

    **MySQL (5.7.22 or higher) is required since the support for `JSON_OBJECTAGG` function was added after v5.7.22 and is used in this project**

4. MongoDB - ?

    

## Instructions

**The data required by the `DEPARTMENT`, `DEPT_LOCATIONS`, `EMPLOYEE`, `PROJECT`, and `WORKS_ON ` tables are present in the respective text files under the `data/` directory**

**The SQL scripts required to create the necessary tables, Insert the necessary data and to convert the query results to JSON objects are present in the `scripts/` directory**

1. Install the necessary dependencies by executing `pip install -r requirements.txt` in the console

2. Add the database credentials for MySQL and MongoDB in `config.py`

3. Execute the program by running `python main.py` in the console and follow the instructions on the screen

4. The output should be as shown below

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
   | ConfigMgmt      |               11 | Software       | Sheen       | Jake        |      25 |
   | DataMining      |               13 | Software       | Yu          | Alex        |      18 |
   | EntityAnnot     |                4 | Research       | Morgan      | Michael     |      11 |
   | Human1          |               95 | HR             | Linda       | Juan        |      40 |
   | Human1          |               95 | HR             | Mary        | willie      |      35 |
   | InkjetPrinters  |               91 | Hardware       | Snedden     | Sam         |      40 |
   | InkjetPrinters  |               91 | Hardware       | Best        | Alec        |      40 |
   | InkjetPrinters  |               91 | Hardware       | Bays        | Bonnie      |      40 |
   | InkjetPrinters  |               91 | Hardware       | Freed       | Alex        |      40 |
   | LaserPrinters   |               92 | Hardware       | Kirkish     | Joseph      |      33 |
   | Middleware      |               63 | Software       | Barbara     | Jose        |      40 |
   | Middleware      |               63 | Software       | Chase       | Jeff        |      46 |
   | Middleware      |               63 | Software       | Grace       | Kim         |      40 |
   | Middleware      |               63 | Software       | Burklow     | Cindy       |      25 |
   | MotherBoard     |               29 | Hardware       | Moody       | Leonard     |      15 |
   | MotherBoard     |               29 | Hardware       | House       | Lisa        |      10 |
   | Newbenefits     |               30 | Administration | Wallace     | Jennifer    |      20 |
   | Newbenefits     |               30 | Administration | Jabbar      | Ahmad       |       5 |
   | Newbenefits     |               30 | Administration | Zelaya      | Alicia      |      30 |
   | OperatingSystem |               61 | Software       | Hisel       | Christina   |       4 |
   | OperatingSystem |               61 | Software       | Knight      | Brad        |      40 |
   | OperatingSystem |               61 | Software       | Mark        | Justin      |      40 |
   | OperatingSystem |               61 | Software       | Jones       | Jon         |      40 |
   | OperatingSystem |               61 | Software       | James       | Jared       |      40 |
   | ProductX        |                1 | Research       | English     | Joyce       |      20 |
   | ProductX        |                1 | Research       | Smith       | John        |      33 |
   | ProductY        |                2 | Research       | Wong        | Franklin    |      10 |
   | ProductY        |                2 | Research       | English     | Joyce       |      20 |
   | ProductY        |                2 | Research       | Smith       | John        |       8 |
   | ProductZ        |                3 | Research       | Sondrini    | Andrea      |      45 |
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
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Debra', 'EMP_LNAME': 'Hall', 'HOURS': 20},
                  {'EMP_FNAME': 'Jake', 'EMP_LNAME': 'Sheen', 'HOURS': 25}],
    'PNAME': 'ConfigMgmt',
    'PNUMBER': 11,
    '_id': ObjectId('5f31c694c2210e84ef83adca')}
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Alex', 'EMP_LNAME': 'Yu', 'HOURS': 18}],
    'PNAME': 'DataMining',
    'PNUMBER': 13,
    '_id': ObjectId('5f31c694c2210e84ef83adcb')}
   {'DNAME': 'Research',
    'EMPLOYEES': [{'EMP_FNAME': 'Michael', 'EMP_LNAME': 'Morgan', 'HOURS': 11}],
    'PNAME': 'EntityAnnot',
    'PNUMBER': 4,
    '_id': ObjectId('5f31c694c2210e84ef83adcc')}
   {'DNAME': 'HR',
    'EMPLOYEES': [{'EMP_FNAME': 'Juan', 'EMP_LNAME': 'Linda', 'HOURS': 40},
                  {'EMP_FNAME': 'willie', 'EMP_LNAME': 'Mary', 'HOURS': 35}],
    'PNAME': 'Human1',
    'PNUMBER': 95,
    '_id': ObjectId('5f31c695c2210e84ef83adcd')}
   {'DNAME': 'Hardware',
    'EMPLOYEES': [{'EMP_FNAME': 'Sam', 'EMP_LNAME': 'Snedden', 'HOURS': 40},
                  {'EMP_FNAME': 'Alec', 'EMP_LNAME': 'Best', 'HOURS': 40},
                  {'EMP_FNAME': 'Bonnie', 'EMP_LNAME': 'Bays', 'HOURS': 40},
                  {'EMP_FNAME': 'Alex', 'EMP_LNAME': 'Freed', 'HOURS': 40}],
    'PNAME': 'InkjetPrinters',
    'PNUMBER': 91,
    '_id': ObjectId('5f31c695c2210e84ef83adce')}
   {'DNAME': 'Hardware',
    'EMPLOYEES': [{'EMP_FNAME': 'Joseph', 'EMP_LNAME': 'Kirkish', 'HOURS': 33}],
    'PNAME': 'LaserPrinters',
    'PNUMBER': 92,
    '_id': ObjectId('5f31c695c2210e84ef83adcf')}
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Jose', 'EMP_LNAME': 'Barbara', 'HOURS': 40},
                  {'EMP_FNAME': 'Jeff', 'EMP_LNAME': 'Chase', 'HOURS': 46},
                  {'EMP_FNAME': 'Kim', 'EMP_LNAME': 'Grace', 'HOURS': 40},
                  {'EMP_FNAME': 'Cindy', 'EMP_LNAME': 'Burklow', 'HOURS': 25}],
    'PNAME': 'Middleware',
    'PNUMBER': 63,
    '_id': ObjectId('5f31c695c2210e84ef83add0')}
   {'DNAME': 'Hardware',
    'EMPLOYEES': [{'EMP_FNAME': 'Leonard', 'EMP_LNAME': 'Moody', 'HOURS': 15},
                  {'EMP_FNAME': 'Lisa', 'EMP_LNAME': 'House', 'HOURS': 10}],
    'PNAME': 'MotherBoard',
    'PNUMBER': 29,
    '_id': ObjectId('5f31c695c2210e84ef83add1')}
   {'DNAME': 'Administration',
    'EMPLOYEES': [{'EMP_FNAME': 'Jennifer', 'EMP_LNAME': 'Wallace', 'HOURS': 20},
                  {'EMP_FNAME': 'Ahmad', 'EMP_LNAME': 'Jabbar', 'HOURS': 5},
                  {'EMP_FNAME': 'Alicia', 'EMP_LNAME': 'Zelaya', 'HOURS': 30}],
    'PNAME': 'Newbenefits',
    'PNUMBER': 30,
    '_id': ObjectId('5f31c695c2210e84ef83add2')}
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Christina', 'EMP_LNAME': 'Hisel', 'HOURS': 4},
                  {'EMP_FNAME': 'Brad', 'EMP_LNAME': 'Knight', 'HOURS': 40},
                  {'EMP_FNAME': 'Justin', 'EMP_LNAME': 'Mark', 'HOURS': 40},
                  {'EMP_FNAME': 'Jon', 'EMP_LNAME': 'Jones', 'HOURS': 40},
                  {'EMP_FNAME': 'Jared', 'EMP_LNAME': 'James', 'HOURS': 40}],
    'PNAME': 'OperatingSystem',
    'PNUMBER': 61,
    '_id': ObjectId('5f31c695c2210e84ef83add3')}
   {'DNAME': 'Research',
    'EMPLOYEES': [{'EMP_FNAME': 'Joyce', 'EMP_LNAME': 'English', 'HOURS': 20},
                  {'EMP_FNAME': 'John', 'EMP_LNAME': 'Smith', 'HOURS': 33}],
    'PNAME': 'ProductX',
    'PNUMBER': 1,
    '_id': ObjectId('5f31c695c2210e84ef83add4')}
   {'DNAME': 'Research',
    'EMPLOYEES': [{'EMP_FNAME': 'Franklin', 'EMP_LNAME': 'Wong', 'HOURS': 10},
                  {'EMP_FNAME': 'Joyce', 'EMP_LNAME': 'English', 'HOURS': 20},
                  {'EMP_FNAME': 'John', 'EMP_LNAME': 'Smith', 'HOURS': 8}],
    'PNAME': 'ProductY',
    'PNUMBER': 2,
    '_id': ObjectId('5f31c695c2210e84ef83add5')}
   {'DNAME': 'Research',
    'EMPLOYEES': [{'EMP_FNAME': 'Andrea', 'EMP_LNAME': 'Sondrini', 'HOURS': 45},
                  {'EMP_FNAME': 'Franklin', 'EMP_LNAME': 'Wong', 'HOURS': 10},
                  {'EMP_FNAME': 'Ramesh', 'EMP_LNAME': 'Narayan', 'HOURS': 40}],
    'PNAME': 'ProductZ',
    'PNUMBER': 3,
    '_id': ObjectId('5f31c695c2210e84ef83add6')}
   {'DNAME': 'Headquarters',
    'EMPLOYEES': [{'EMP_FNAME': 'James', 'EMP_LNAME': 'Borg', 'HOURS': 5}],
    'PNAME': 'Reorganization',
    'PNUMBER': 20,
    '_id': ObjectId('5f31c695c2210e84ef83add7')}
   {'DNAME': 'Software',
    'EMPLOYEES': [{'EMP_FNAME': 'Zach', 'EMP_LNAME': 'Geller', 'HOURS': 30},
                  {'EMP_FNAME': 'Penny', 'EMP_LNAME': 'Wolowitz', 'HOURS': 4}],
    'PNAME': 'SearchEngine',
    'PNUMBER': 22,
    '_id': ObjectId('5f31c695c2210e84ef83add8')}
   ------------------------------ FOR EXTRA CREDIT : XML document format ------------------------------
   Press ENTER key to display data in XML format for project
   <?xml version="1.0" encoding="UTF-8"?>
   <ALL_PROJECTS>	<PROJECT PNUMBER=70 PNAME="Advertizing">
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
   	<PROJECT PNUMBER=11 PNAME="ConfigMgmt">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Hall" EMP_FNAME="Debra" HOURS=20 />
   			<EMPLOYEE EMP_LNAME="Sheen" EMP_FNAME="Jake" HOURS=25 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=13 PNAME="DataMining">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Yu" EMP_FNAME="Alex" HOURS=18 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=4 PNAME="EntityAnnot">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Morgan" EMP_FNAME="Michael" HOURS=11 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=95 PNAME="Human1">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Linda" EMP_FNAME="Juan" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Mary" EMP_FNAME="willie" HOURS=35 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=91 PNAME="InkjetPrinters">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Snedden" EMP_FNAME="Sam" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Best" EMP_FNAME="Alec" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Bays" EMP_FNAME="Bonnie" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Freed" EMP_FNAME="Alex" HOURS=40 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=92 PNAME="LaserPrinters">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Kirkish" EMP_FNAME="Joseph" HOURS=33 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=63 PNAME="Middleware">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Barbara" EMP_FNAME="Jose" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Chase" EMP_FNAME="Jeff" HOURS=46 />
   			<EMPLOYEE EMP_LNAME="Grace" EMP_FNAME="Kim" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Burklow" EMP_FNAME="Cindy" HOURS=25 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=29 PNAME="MotherBoard">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Moody" EMP_FNAME="Leonard" HOURS=15 />
   			<EMPLOYEE EMP_LNAME="House" EMP_FNAME="Lisa" HOURS=10 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=30 PNAME="Newbenefits">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Wallace" EMP_FNAME="Jennifer" HOURS=20 />
   			<EMPLOYEE EMP_LNAME="Jabbar" EMP_FNAME="Ahmad" HOURS=5 />
   			<EMPLOYEE EMP_LNAME="Zelaya" EMP_FNAME="Alicia" HOURS=30 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=61 PNAME="OperatingSystem">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Hisel" EMP_FNAME="Christina" HOURS=4 />
   			<EMPLOYEE EMP_LNAME="Knight" EMP_FNAME="Brad" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Mark" EMP_FNAME="Justin" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="Jones" EMP_FNAME="Jon" HOURS=40 />
   			<EMPLOYEE EMP_LNAME="James" EMP_FNAME="Jared" HOURS=40 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=1 PNAME="ProductX">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="English" EMP_FNAME="Joyce" HOURS=20 />
   			<EMPLOYEE EMP_LNAME="Smith" EMP_FNAME="John" HOURS=33 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=2 PNAME="ProductY">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Wong" EMP_FNAME="Franklin" HOURS=10 />
   			<EMPLOYEE EMP_LNAME="English" EMP_FNAME="Joyce" HOURS=20 />
   			<EMPLOYEE EMP_LNAME="Smith" EMP_FNAME="John" HOURS=8 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=3 PNAME="ProductZ">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Sondrini" EMP_FNAME="Andrea" HOURS=45 />
   			<EMPLOYEE EMP_LNAME="Wong" EMP_FNAME="Franklin" HOURS=10 />
   			<EMPLOYEE EMP_LNAME="Narayan" EMP_FNAME="Ramesh" HOURS=40 />
   		</EMPLOYEES>
   	</PROJECT>
   	<PROJECT PNUMBER=20 PNAME="Reorganization">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Borg" EMP_FNAME="James" HOURS=5 />
   		</EMPLOYEES>
   	</PROJECT>
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
   | English     | Joyce       | Research       | ProductY        |                2 |      20 |
   | Freed       | Alex        | Hardware       | InkjetPrinters  |               91 |      40 |
   | Geller      | Zach        | Software       | SearchEngine    |               22 |      30 |
   | Grace       | Kim         | Software       | Middleware      |               63 |      40 |
   | Hall        | Debra       | Software       | ConfigMgmt      |               11 |      20 |
   | Hisel       | Christina   | Software       | OperatingSystem |               61 |       4 |
   | House       | Lisa        | Hardware       | MotherBoard     |               29 |      10 |
   | Jabbar      | Ahmad       | Administration | Computerization |               10 |      35 |
   | Jabbar      | Ahmad       | Administration | Newbenefits     |               30 |       5 |
   | James       | Jared       | Software       | OperatingSystem |               61 |      40 |
   | Jones       | Jon         | Software       | OperatingSystem |               61 |      40 |
   | Kirkish     | Joseph      | Hardware       | LaserPrinters   |               92 |      33 |
   | Knight      | Brad        | Software       | OperatingSystem |               61 |      40 |
   | Koelbel     | Richard     | Administration | Computerization |               10 |      35 |
   | Liang       | Percy       | HR             | Advertizing     |               70 |      10 |
   | Linda       | Juan        | HR             | Human1          |               95 |      40 |
   | Mark        | Justin      | Software       | OperatingSystem |               61 |      40 |
   | Mary        | willie      | HR             | Human1          |               95 |      35 |
   | Moody       | Leonard     | Hardware       | MotherBoard     |               29 |      15 |
   | Morgan      | Michael     | Research       | EntityAnnot     |                4 |      11 |
   | Narayan     | Ramesh      | Research       | ProductZ        |                3 |      40 |
   | Sheen       | Jake        | Software       | ConfigMgmt      |               11 |      25 |
   | Smith       | John        | Research       | ProductY        |                2 |       8 |
   | Smith       | John        | Research       | ProductX        |                1 |      33 |
   | Snedden     | Sam         | Hardware       | InkjetPrinters  |               91 |      40 |
   | Sondrini    | Andrea      | Research       | ProductZ        |                3 |      45 |
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
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Alec',
    'EMP_LNAME': 'Best',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'InkjetPrinters', 'PNUMBER': 91}],
    '_id': ObjectId('5f31c698c2210e84ef83addb')}
   {'DNAME': 'Headquarters',
    'EMP_FNAME': 'James',
    'EMP_LNAME': 'Borg',
    'PROJECTS': [{'HOURS': 5, 'PNAME': 'Reorganization', 'PNUMBER': 20}],
    '_id': ObjectId('5f31c698c2210e84ef83addc')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Cindy',
    'EMP_LNAME': 'Burklow',
    'PROJECTS': [{'HOURS': 25, 'PNAME': 'Middleware', 'PNUMBER': 63}],
    '_id': ObjectId('5f31c698c2210e84ef83addd')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Jeff',
    'EMP_LNAME': 'Chase',
    'PROJECTS': [{'HOURS': 46, 'PNAME': 'Middleware', 'PNUMBER': 63}],
    '_id': ObjectId('5f31c698c2210e84ef83adde')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'Joyce',
    'EMP_LNAME': 'English',
    'PROJECTS': [{'HOURS': 20, 'PNAME': 'ProductX', 'PNUMBER': 1},
                 {'HOURS': 20, 'PNAME': 'ProductY', 'PNUMBER': 2}],
    '_id': ObjectId('5f31c698c2210e84ef83addf')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Alex',
    'EMP_LNAME': 'Freed',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'InkjetPrinters', 'PNUMBER': 91}],
    '_id': ObjectId('5f31c698c2210e84ef83ade0')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Zach',
    'EMP_LNAME': 'Geller',
    'PROJECTS': [{'HOURS': 30, 'PNAME': 'SearchEngine', 'PNUMBER': 22}],
    '_id': ObjectId('5f31c698c2210e84ef83ade1')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Kim',
    'EMP_LNAME': 'Grace',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'Middleware', 'PNUMBER': 63}],
    '_id': ObjectId('5f31c698c2210e84ef83ade2')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Debra',
    'EMP_LNAME': 'Hall',
    'PROJECTS': [{'HOURS': 20, 'PNAME': 'ConfigMgmt', 'PNUMBER': 11}],
    '_id': ObjectId('5f31c698c2210e84ef83ade3')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Christina',
    'EMP_LNAME': 'Hisel',
    'PROJECTS': [{'HOURS': 4, 'PNAME': 'OperatingSystem', 'PNUMBER': 61}],
    '_id': ObjectId('5f31c698c2210e84ef83ade4')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Lisa',
    'EMP_LNAME': 'House',
    'PROJECTS': [{'HOURS': 10, 'PNAME': 'MotherBoard', 'PNUMBER': 29}],
    '_id': ObjectId('5f31c698c2210e84ef83ade5')}
   {'DNAME': 'Administration',
    'EMP_FNAME': 'Ahmad',
    'EMP_LNAME': 'Jabbar',
    'PROJECTS': [{'HOURS': 35, 'PNAME': 'Computerization', 'PNUMBER': 10},
                 {'HOURS': 5, 'PNAME': 'Newbenefits', 'PNUMBER': 30}],
    '_id': ObjectId('5f31c698c2210e84ef83ade6')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Jared',
    'EMP_LNAME': 'James',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'OperatingSystem', 'PNUMBER': 61}],
    '_id': ObjectId('5f31c698c2210e84ef83ade7')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Jon',
    'EMP_LNAME': 'Jones',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'OperatingSystem', 'PNUMBER': 61}],
    '_id': ObjectId('5f31c698c2210e84ef83ade8')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Joseph',
    'EMP_LNAME': 'Kirkish',
    'PROJECTS': [{'HOURS': 33, 'PNAME': 'LaserPrinters', 'PNUMBER': 92}],
    '_id': ObjectId('5f31c698c2210e84ef83ade9')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Brad',
    'EMP_LNAME': 'Knight',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'OperatingSystem', 'PNUMBER': 61}],
    '_id': ObjectId('5f31c698c2210e84ef83adea')}
   {'DNAME': 'Administration',
    'EMP_FNAME': 'Richard',
    'EMP_LNAME': 'Koelbel',
    'PROJECTS': [{'HOURS': 35, 'PNAME': 'Computerization', 'PNUMBER': 10}],
    '_id': ObjectId('5f31c699c2210e84ef83adeb')}
   {'DNAME': 'HR',
    'EMP_FNAME': 'Percy',
    'EMP_LNAME': 'Liang',
    'PROJECTS': [{'HOURS': 10, 'PNAME': 'Advertizing', 'PNUMBER': 70}],
    '_id': ObjectId('5f31c699c2210e84ef83adec')}
   {'DNAME': 'HR',
    'EMP_FNAME': 'Juan',
    'EMP_LNAME': 'Linda',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'Human1', 'PNUMBER': 95}],
    '_id': ObjectId('5f31c699c2210e84ef83aded')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Justin',
    'EMP_LNAME': 'Mark',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'OperatingSystem', 'PNUMBER': 61}],
    '_id': ObjectId('5f31c699c2210e84ef83adee')}
   {'DNAME': 'HR',
    'EMP_FNAME': 'willie',
    'EMP_LNAME': 'Mary',
    'PROJECTS': [{'HOURS': 35, 'PNAME': 'Human1', 'PNUMBER': 95}],
    '_id': ObjectId('5f31c699c2210e84ef83adef')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Leonard',
    'EMP_LNAME': 'Moody',
    'PROJECTS': [{'HOURS': 15, 'PNAME': 'MotherBoard', 'PNUMBER': 29}],
    '_id': ObjectId('5f31c699c2210e84ef83adf0')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'Michael',
    'EMP_LNAME': 'Morgan',
    'PROJECTS': [{'HOURS': 11, 'PNAME': 'EntityAnnot', 'PNUMBER': 4}],
    '_id': ObjectId('5f31c699c2210e84ef83adf1')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'Ramesh',
    'EMP_LNAME': 'Narayan',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'ProductZ', 'PNUMBER': 3}],
    '_id': ObjectId('5f31c699c2210e84ef83adf2')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Jake',
    'EMP_LNAME': 'Sheen',
    'PROJECTS': [{'HOURS': 25, 'PNAME': 'ConfigMgmt', 'PNUMBER': 11}],
    '_id': ObjectId('5f31c699c2210e84ef83adf3')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'John',
    'EMP_LNAME': 'Smith',
    'PROJECTS': [{'HOURS': 8, 'PNAME': 'ProductY', 'PNUMBER': 2},
                 {'HOURS': 33, 'PNAME': 'ProductX', 'PNUMBER': 1}],
    '_id': ObjectId('5f31c699c2210e84ef83adf4')}
   {'DNAME': 'Hardware',
    'EMP_FNAME': 'Sam',
    'EMP_LNAME': 'Snedden',
    'PROJECTS': [{'HOURS': 40, 'PNAME': 'InkjetPrinters', 'PNUMBER': 91}],
    '_id': ObjectId('5f31c699c2210e84ef83adf5')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'Andrea',
    'EMP_LNAME': 'Sondrini',
    'PROJECTS': [{'HOURS': 45, 'PNAME': 'ProductZ', 'PNUMBER': 3}],
    '_id': ObjectId('5f31c699c2210e84ef83adf6')}
   {'DNAME': 'Administration',
    'EMP_FNAME': 'Jennifer',
    'EMP_LNAME': 'Wallace',
    'PROJECTS': [{'HOURS': 20, 'PNAME': 'Newbenefits', 'PNUMBER': 30}],
    '_id': ObjectId('5f31c699c2210e84ef83adf7')}
   {'DNAME': 'Software',
    'EMP_FNAME': 'Penny',
    'EMP_LNAME': 'Wolowitz',
    'PROJECTS': [{'HOURS': 4, 'PNAME': 'SearchEngine', 'PNUMBER': 22}],
    '_id': ObjectId('5f31c699c2210e84ef83adf8')}
   {'DNAME': 'Research',
    'EMP_FNAME': 'Franklin',
    'EMP_LNAME': 'Wong',
    'PROJECTS': [{'HOURS': 10, 'PNAME': 'ProductY', 'PNUMBER': 2},
                 {'HOURS': 10, 'PNAME': 'ProductZ', 'PNUMBER': 3}],
    '_id': ObjectId('5f31c699c2210e84ef83adf9')}
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
   <ALL_EMPLOYEES>	<EMPLOYEE EMP_LNAME="Barbara" EMP_FNAME="Jose" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="Middleware" PNUMBER=63 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Bays" EMP_FNAME="Bonnie" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="InkjetPrinters" PNUMBER=91 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Best" EMP_FNAME="Alec" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="InkjetPrinters" PNUMBER=91 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Borg" EMP_FNAME="James" DNAME="Headquarters">
   		<PROJECTS>
   			<PROJECT PNAME="Reorganization" PNUMBER=20 HOURS=5 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Burklow" EMP_FNAME="Cindy" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="Middleware" PNUMBER=63 HOURS=25 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Chase" EMP_FNAME="Jeff" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="Middleware" PNUMBER=63 HOURS=46 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="English" EMP_FNAME="Joyce" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="ProductX" PNUMBER=1 HOURS=20 />
   			<PROJECT PNAME="ProductY" PNUMBER=2 HOURS=20 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Freed" EMP_FNAME="Alex" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="InkjetPrinters" PNUMBER=91 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Geller" EMP_FNAME="Zach" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="SearchEngine" PNUMBER=22 HOURS=30 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Grace" EMP_FNAME="Kim" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="Middleware" PNUMBER=63 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Hall" EMP_FNAME="Debra" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="ConfigMgmt" PNUMBER=11 HOURS=20 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Hisel" EMP_FNAME="Christina" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="OperatingSystem" PNUMBER=61 HOURS=4 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="House" EMP_FNAME="Lisa" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="MotherBoard" PNUMBER=29 HOURS=10 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Jabbar" EMP_FNAME="Ahmad" DNAME="Administration">
   		<PROJECTS>
   			<PROJECT PNAME="Computerization" PNUMBER=10 HOURS=35 />
   			<PROJECT PNAME="Newbenefits" PNUMBER=30 HOURS=5 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="James" EMP_FNAME="Jared" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="OperatingSystem" PNUMBER=61 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Jones" EMP_FNAME="Jon" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="OperatingSystem" PNUMBER=61 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Kirkish" EMP_FNAME="Joseph" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="LaserPrinters" PNUMBER=92 HOURS=33 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Knight" EMP_FNAME="Brad" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="OperatingSystem" PNUMBER=61 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Koelbel" EMP_FNAME="Richard" DNAME="Administration">
   		<PROJECTS>
   			<PROJECT PNAME="Computerization" PNUMBER=10 HOURS=35 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Liang" EMP_FNAME="Percy" DNAME="HR">
   		<PROJECTS>
   			<PROJECT PNAME="Advertizing" PNUMBER=70 HOURS=10 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Linda" EMP_FNAME="Juan" DNAME="HR">
   		<PROJECTS>
   			<PROJECT PNAME="Human1" PNUMBER=95 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Mark" EMP_FNAME="Justin" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="OperatingSystem" PNUMBER=61 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Mary" EMP_FNAME="willie" DNAME="HR">
   		<PROJECTS>
   			<PROJECT PNAME="Human1" PNUMBER=95 HOURS=35 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Moody" EMP_FNAME="Leonard" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="MotherBoard" PNUMBER=29 HOURS=15 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Morgan" EMP_FNAME="Michael" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="EntityAnnot" PNUMBER=4 HOURS=11 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Narayan" EMP_FNAME="Ramesh" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="ProductZ" PNUMBER=3 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Sheen" EMP_FNAME="Jake" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="ConfigMgmt" PNUMBER=11 HOURS=25 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Smith" EMP_FNAME="John" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="ProductY" PNUMBER=2 HOURS=8 />
   			<PROJECT PNAME="ProductX" PNUMBER=1 HOURS=33 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Snedden" EMP_FNAME="Sam" DNAME="Hardware">
   		<PROJECTS>
   			<PROJECT PNAME="InkjetPrinters" PNUMBER=91 HOURS=40 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Sondrini" EMP_FNAME="Andrea" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="ProductZ" PNUMBER=3 HOURS=45 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Wallace" EMP_FNAME="Jennifer" DNAME="Administration">
   		<PROJECTS>
   			<PROJECT PNAME="Newbenefits" PNUMBER=30 HOURS=20 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Wolowitz" EMP_FNAME="Penny" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="SearchEngine" PNUMBER=22 HOURS=4 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Wong" EMP_FNAME="Franklin" DNAME="Research">
   		<PROJECTS>
   			<PROJECT PNAME="ProductY" PNUMBER=2 HOURS=10 />
   			<PROJECT PNAME="ProductZ" PNUMBER=3 HOURS=10 />
   		</PROJECTS>
   	</EMPLOYEE>
   	<EMPLOYEE EMP_LNAME="Yu" EMP_FNAME="Alex" DNAME="Software">
   		<PROJECTS>
   			<PROJECT PNAME="DataMining" PNUMBER=13 HOURS=18 />
   		</PROJECTS>
   	</EMPLOYEE>
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
   | Administration |              4 | Wallace         | Jennifer        | Koelbel     | Richard     |        85000 |
   | Administration |              4 | Wallace         | Jennifer        | Thirteen    | Cameron     |        80000 |
   | Administration |              4 | Wallace         | Jennifer        | Wallace     | Jennifer    |        43000 |
   | Administration |              4 | Wallace         | Jennifer        | Zelaya      | Alicia      |        25000 |
   | Hardware       |              7 | Freed           | Alex            | Bays        | Bonnie      |        70000 |
   | Hardware       |              7 | Freed           | Alex            | Best        | Alec        |        60000 |
   | Hardware       |              7 | Freed           | Alex            | Brand       | Tom         |        62500 |
   | Hardware       |              7 | Freed           | Alex            | Carter      | Chris       |        43000 |
   | Hardware       |              7 | Freed           | Alex            | Freed       | Alex        |        89000 |
   | Hardware       |              7 | Freed           | Alex            | House       | Lisa        |        85000 |
   | Hardware       |              7 | Freed           | Alex            | Kirkish     | Joseph      |        95000 |
   | Hardware       |              7 | Freed           | Alex            | Laurie      | Gregory     |        90000 |
   | Hardware       |              7 | Freed           | Alex            | Moody       | Leonard     |        45000 |
   | Hardware       |              7 | Freed           | Alex            | Snedden     | Sam         |        48000 |
   | Hardware       |              7 | Freed           | Alex            | Vile        | Andy        |        53000 |
   | Hardware       |              7 | Freed           | Alex            | Vos         | Jenny       |        61000 |
   | Hardware       |              7 | Freed           | Alex            | Wallis      | Evan        |        92000 |
   | Hardware       |              7 | Freed           | Alex            | Zell        | Josh        |        56000 |
   | Headquarters   |              1 | Borg            | James           | Borg        | James       |        55000 |
   | Headquarters   |              1 | Borg            | James           | Carpenter   | Jisha       |        15000 |
   | HR             |              9 | Linda           | Juan            | Jarvis      | Jill        |        36000 |
   | HR             |              9 | Linda           | Juan            | King        | Ray         |        44500 |
   | HR             |              9 | Linda           | Juan            | Liang       | Percy       |        55000 |
   | HR             |              9 | Linda           | Juan            | Linda       | Juan        |        55000 |
   | HR             |              9 | Linda           | Juan            | Mary        | willie      |        12000 |
   | HR             |              9 | Linda           | Juan            | Smith       | Johny       |        65000 |
   | HR             |              9 | Linda           | Juan            | Ted         | Kim         |        50000 |
   | Networking     |              3 | Gupta           | Sunil           | Gupta       | Sunil       |        80000 |
   | Research       |              5 | Wong            | Franklin        | English     | Joyce       |        25000 |
   | Research       |              5 | Wong            | Franklin        | Miller      | James       |        75000 |
   | Research       |              5 | Wong            | Franklin        | Morgan      | Michael     |        73500 |
   | Research       |              5 | Wong            | Franklin        | Narayan     | Ramesh      |        38000 |
   | Research       |              5 | Wong            | Franklin        | Smith       | John        |        30000 |
   | Research       |              5 | Wong            | Franklin        | Sondrini    | Andrea      |        65000 |
   | Research       |              5 | Wong            | Franklin        | Wong        | Franklin    |        40000 |
   | Sales          |              8 | James           | John            | Bacher      | Red         |        33500 |
   | Sales          |              8 | James           | John            | Bender      | Bob         |        96000 |
   | Sales          |              8 | James           | John            | Cucuou      | Sheldon     |        35500 |
   | Sales          |              8 | James           | John            | Drew        | Naveen      |        34000 |
   | Sales          |              8 | James           | John            | Hall        | Sammy       |        37000 |
   | Sales          |              8 | James           | John            | Head        | Arnold      |        33000 |
   | Sales          |              8 | James           | John            | James       | John        |        81000 |
   | Sales          |              8 | James           | John            | Jones       | Megan       |        62000 |
   | Sales          |              8 | James           | John            | Joy         | Jennifer    |        45000 |
   | Sales          |              8 | James           | John            | King        | Billie      |        38000 |
   | Sales          |              8 | James           | John            | King        | Kate        |        44000 |
   | Sales          |              8 | James           | John            | Kramer      | Jon         |        41500 |
   | Sales          |              8 | James           | John            | Leslie      | Lyle        |        41000 |
   | Sales          |              8 | James           | John            | Lewallen    | Roy         |        75500 |
   | Sales          |              8 | James           | John            | Maxfield    | Erin        |        72000 |
   | Sales          |              8 | James           | John            | Pataki      | Helga       |        32000 |
   | Sales          |              8 | James           | John            | Reedy       | Carl        |        32000 |
   | Sales          |              8 | James           | John            | Small       | Gerald      |        29000 |
   | Software       |              6 | James           | Jared           | Ball        | Nandita     |        62000 |
   | Software       |              6 | James           | Jared           | Barbara     | Jose        |        35000 |
   | Software       |              6 | James           | Jared           | Burklow     | Cindy       |        45000 |
   | Software       |              6 | James           | Jared           | Chase       | Jeff        |        44000 |
   | Software       |              6 | James           | Jared           | Ed          | John        |        30000 |
   | Software       |              6 | James           | Jared           | Geller      | Zach        |        55000 |
   | Software       |              6 | James           | Jared           | Grace       | Kim         |        79000 |
   | Software       |              6 | James           | Jared           | Hall        | Debra       |        30000 |
   | Software       |              6 | James           | Jared           | Hisel       | Christina   |        45000 |
   | Software       |              6 | James           | Jared           | James       | Jared       |        85000 |
   | Software       |              6 | James           | Jared           | Jones       | Jon         |        45000 |
   | Software       |              6 | James           | Jared           | Knight      | Brad        |        44000 |
   | Software       |              6 | James           | Jared           | Mark        | Justin      |        40000 |
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
                   'EMP_LNAME': 'Koelbel',
                   'EMP_SALARY': 85000},
                  {'EMP_FNAME': 'Wilson',
                   'EMP_LNAME': 'Holmes',
                   'EMP_SALARY': 72500},
                  {'EMP_FNAME': 'Jennifer',
                   'EMP_LNAME': 'Wallace',
                   'EMP_SALARY': 43000},
                  {'EMP_FNAME': 'Ahmad',
                   'EMP_LNAME': 'Jabbar',
                   'EMP_SALARY': 25000},
                  {'EMP_FNAME': 'Alicia',
                   'EMP_LNAME': 'Zelaya',
                   'EMP_SALARY': 25000}],
    'MGR_FNAME': 'Jennifer',
    'MGR_LNAME': 'Wallace',
    '_id': ObjectId('5f31c69ec2210e84ef83adfc')}
   {'DNAME': 'Hardware',
    'DNUMBER': 7,
    'EMPLOYEES': [{'EMP_FNAME': 'Bonnie',
                   'EMP_LNAME': 'Bays',
                   'EMP_SALARY': 70000},
                  {'EMP_FNAME': 'Lisa', 'EMP_LNAME': 'House', 'EMP_SALARY': 85000},
                  {'EMP_FNAME': 'Evan',
                   'EMP_LNAME': 'Wallis',
                   'EMP_SALARY': 92000},
                  {'EMP_FNAME': 'Josh', 'EMP_LNAME': 'Zell', 'EMP_SALARY': 56000},
                  {'EMP_FNAME': 'Andy', 'EMP_LNAME': 'Vile', 'EMP_SALARY': 53000},
                  {'EMP_FNAME': 'Tom', 'EMP_LNAME': 'Brand', 'EMP_SALARY': 62500},
                  {'EMP_FNAME': 'Jenny', 'EMP_LNAME': 'Vos', 'EMP_SALARY': 61000},
                  {'EMP_FNAME': 'Chris',
                   'EMP_LNAME': 'Carter',
                   'EMP_SALARY': 43000},
                  {'EMP_FNAME': 'Leonard',
                   'EMP_LNAME': 'Moody',
                   'EMP_SALARY': 45000},
                  {'EMP_FNAME': 'Gregory',
                   'EMP_LNAME': 'Laurie',
                   'EMP_SALARY': 90000},
                  {'EMP_FNAME': 'Alex', 'EMP_LNAME': 'Freed', 'EMP_SALARY': 89000},
                  {'EMP_FNAME': 'Alec', 'EMP_LNAME': 'Best', 'EMP_SALARY': 60000},
                  {'EMP_FNAME': 'Sam',
                   'EMP_LNAME': 'Snedden',
                   'EMP_SALARY': 48000},
                  {'EMP_FNAME': 'Joseph',
                   'EMP_LNAME': 'Kirkish',
                   'EMP_SALARY': 95000}],
    'MGR_FNAME': 'Alex',
    'MGR_LNAME': 'Freed',
    '_id': ObjectId('5f31c69ec2210e84ef83adfd')}
   {'DNAME': 'Headquarters',
    'DNUMBER': 1,
    'EMPLOYEES': [{'EMP_FNAME': 'James', 'EMP_LNAME': 'Borg', 'EMP_SALARY': 55000},
                  {'EMP_FNAME': 'Jisha',
                   'EMP_LNAME': 'Carpenter',
                   'EMP_SALARY': 15000}],
    'MGR_FNAME': 'James',
    'MGR_LNAME': 'Borg',
    '_id': ObjectId('5f31c69ec2210e84ef83adfe')}
   {'DNAME': 'HR',
    'DNUMBER': 9,
    'EMPLOYEES': [{'EMP_FNAME': 'Ray', 'EMP_LNAME': 'King', 'EMP_SALARY': 44500},
                  {'EMP_FNAME': 'Jill',
                   'EMP_LNAME': 'Jarvis',
                   'EMP_SALARY': 36000},
                  {'EMP_FNAME': 'Kim', 'EMP_LNAME': 'Ted', 'EMP_SALARY': 50000},
                  {'EMP_FNAME': 'Percy',
                   'EMP_LNAME': 'Liang',
                   'EMP_SALARY': 55000},
                  {'EMP_FNAME': 'willie',
                   'EMP_LNAME': 'Mary',
                   'EMP_SALARY': 12000},
                  {'EMP_FNAME': 'Johny',
                   'EMP_LNAME': 'Smith',
                   'EMP_SALARY': 65000},
                  {'EMP_FNAME': 'Juan',
                   'EMP_LNAME': 'Linda',
                   'EMP_SALARY': 55000}],
    'MGR_FNAME': 'Juan',
    'MGR_LNAME': 'Linda',
    '_id': ObjectId('5f31c69ec2210e84ef83adff')}
   {'DNAME': 'Networking',
    'DNUMBER': 3,
    'EMPLOYEES': [{'EMP_FNAME': 'Sunil',
                   'EMP_LNAME': 'Gupta',
                   'EMP_SALARY': 80000}],
    'MGR_FNAME': 'Sunil',
    'MGR_LNAME': 'Gupta',
    '_id': ObjectId('5f31c69ec2210e84ef83ae00')}
   {'DNAME': 'Research',
    'DNUMBER': 5,
    'EMPLOYEES': [{'EMP_FNAME': 'Franklin',
                   'EMP_LNAME': 'Wong',
                   'EMP_SALARY': 40000},
                  {'EMP_FNAME': 'Joyce',
                   'EMP_LNAME': 'English',
                   'EMP_SALARY': 25000},
                  {'EMP_FNAME': 'Andrea',
                   'EMP_LNAME': 'Sondrini',
                   'EMP_SALARY': 65000},
                  {'EMP_FNAME': 'Michael',
                   'EMP_LNAME': 'Morgan',
                   'EMP_SALARY': 73500},
                  {'EMP_FNAME': 'Ramesh',
                   'EMP_LNAME': 'Narayan',
                   'EMP_SALARY': 38000},
                  {'EMP_FNAME': 'James',
                   'EMP_LNAME': 'Miller',
                   'EMP_SALARY': 75000},
                  {'EMP_FNAME': 'John',
                   'EMP_LNAME': 'Smith',
                   'EMP_SALARY': 30000}],
    'MGR_FNAME': 'Franklin',
    'MGR_LNAME': 'Wong',
    '_id': ObjectId('5f31c69ec2210e84ef83ae01')}
   {'DNAME': 'Sales',
    'DNUMBER': 8,
    'EMPLOYEES': [{'EMP_FNAME': 'Gerald',
                   'EMP_LNAME': 'Small',
                   'EMP_SALARY': 29000},
                  {'EMP_FNAME': 'Jon', 'EMP_LNAME': 'Kramer', 'EMP_SALARY': 41500},
                  {'EMP_FNAME': 'Billie',
                   'EMP_LNAME': 'King',
                   'EMP_SALARY': 38000},
                  {'EMP_FNAME': 'Lyle',
                   'EMP_LNAME': 'Leslie',
                   'EMP_SALARY': 41000},
                  {'EMP_FNAME': 'Jennifer',
                   'EMP_LNAME': 'Joy',
                   'EMP_SALARY': 45000},
                  {'EMP_FNAME': 'Kate', 'EMP_LNAME': 'King', 'EMP_SALARY': 44000},
                  {'EMP_FNAME': 'Arnold',
                   'EMP_LNAME': 'Head',
                   'EMP_SALARY': 33000},
                  {'EMP_FNAME': 'Helga',
                   'EMP_LNAME': 'Pataki',
                   'EMP_SALARY': 32000},
                  {'EMP_FNAME': 'Naveen',
                   'EMP_LNAME': 'Drew',
                   'EMP_SALARY': 34000},
                  {'EMP_FNAME': 'Carl', 'EMP_LNAME': 'Reedy', 'EMP_SALARY': 32000},
                  {'EMP_FNAME': 'Sammy', 'EMP_LNAME': 'Hall', 'EMP_SALARY': 37000},
                  {'EMP_FNAME': 'Red', 'EMP_LNAME': 'Bacher', 'EMP_SALARY': 33500},
                  {'EMP_FNAME': 'Sheldon',
                   'EMP_LNAME': 'Cucuou',
                   'EMP_SALARY': 35500},
                  {'EMP_FNAME': 'Roy',
                   'EMP_LNAME': 'Lewallen',
                   'EMP_SALARY': 75500},
                  {'EMP_FNAME': 'John', 'EMP_LNAME': 'James', 'EMP_SALARY': 81000},
                  {'EMP_FNAME': 'Megan',
                   'EMP_LNAME': 'Jones',
                   'EMP_SALARY': 62000},
                  {'EMP_FNAME': 'Erin',
                   'EMP_LNAME': 'Maxfield',
                   'EMP_SALARY': 72000},
                  {'EMP_FNAME': 'Bob',
                   'EMP_LNAME': 'Bender',
                   'EMP_SALARY': 96000}],
    'MGR_FNAME': 'John',
    'MGR_LNAME': 'James',
    '_id': ObjectId('5f31c69ec2210e84ef83ae02')}
   {'DNAME': 'Software',
    'DNUMBER': 6,
    'EMPLOYEES': [{'EMP_FNAME': 'John', 'EMP_LNAME': 'Ed', 'EMP_SALARY': 30000},
                  {'EMP_FNAME': 'Christina',
                   'EMP_LNAME': 'Hisel',
                   'EMP_SALARY': 45000},
                  {'EMP_FNAME': 'Jake', 'EMP_LNAME': 'Sheen', 'EMP_SALARY': 52000},
                  {'EMP_FNAME': 'Kim', 'EMP_LNAME': 'Grace', 'EMP_SALARY': 79000},
                  {'EMP_FNAME': 'Jeff', 'EMP_LNAME': 'Chase', 'EMP_SALARY': 44000},
                  {'EMP_FNAME': 'Jose',
                   'EMP_LNAME': 'Barbara',
                   'EMP_SALARY': 35000},
                  {'EMP_FNAME': 'Cindy',
                   'EMP_LNAME': 'Burklow',
                   'EMP_SALARY': 45000},
                  {'EMP_FNAME': 'Nandita',
                   'EMP_LNAME': 'Ball',
                   'EMP_SALARY': 62000},
                  {'EMP_FNAME': 'Penny',
                   'EMP_LNAME': 'Wolowitz',
                   'EMP_SALARY': 17000},
                  {'EMP_FNAME': 'Zach',
                   'EMP_LNAME': 'Geller',
                   'EMP_SALARY': 55000},
                  {'EMP_FNAME': 'Brad',
                   'EMP_LNAME': 'Knight',
                   'EMP_SALARY': 44000},
                  {'EMP_FNAME': 'Justin',
                   'EMP_LNAME': 'Mark',
                   'EMP_SALARY': 40000},
                  {'EMP_FNAME': 'Jon', 'EMP_LNAME': 'Jones', 'EMP_SALARY': 45000},
                  {'EMP_FNAME': 'Jared',
                   'EMP_LNAME': 'James',
                   'EMP_SALARY': 85000},
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
   <ALL_DEPARTMENTS>	<DEPARTMENT DNAME="Administration" DNUMBER="4" MGR_LNAME="Wallace" MGR_FNAME="Jennifer">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Thirteen" EMP_FNAME="Cameron" EMP_SALARY=80000 />
   			<EMPLOYEE EMP_LNAME="Koelbel" EMP_FNAME="Richard" EMP_SALARY=85000 />
   			<EMPLOYEE EMP_LNAME="Holmes" EMP_FNAME="Wilson" EMP_SALARY=72500 />
   			<EMPLOYEE EMP_LNAME="Wallace" EMP_FNAME="Jennifer" EMP_SALARY=43000 />
   			<EMPLOYEE EMP_LNAME="Jabbar" EMP_FNAME="Ahmad" EMP_SALARY=25000 />
   			<EMPLOYEE EMP_LNAME="Zelaya" EMP_FNAME="Alicia" EMP_SALARY=25000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Hardware" DNUMBER="7" MGR_LNAME="Freed" MGR_FNAME="Alex">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Bays" EMP_FNAME="Bonnie" EMP_SALARY=70000 />
   			<EMPLOYEE EMP_LNAME="House" EMP_FNAME="Lisa" EMP_SALARY=85000 />
   			<EMPLOYEE EMP_LNAME="Wallis" EMP_FNAME="Evan" EMP_SALARY=92000 />
   			<EMPLOYEE EMP_LNAME="Zell" EMP_FNAME="Josh" EMP_SALARY=56000 />
   			<EMPLOYEE EMP_LNAME="Vile" EMP_FNAME="Andy" EMP_SALARY=53000 />
   			<EMPLOYEE EMP_LNAME="Brand" EMP_FNAME="Tom" EMP_SALARY=62500 />
   			<EMPLOYEE EMP_LNAME="Vos" EMP_FNAME="Jenny" EMP_SALARY=61000 />
   			<EMPLOYEE EMP_LNAME="Carter" EMP_FNAME="Chris" EMP_SALARY=43000 />
   			<EMPLOYEE EMP_LNAME="Moody" EMP_FNAME="Leonard" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="Laurie" EMP_FNAME="Gregory" EMP_SALARY=90000 />
   			<EMPLOYEE EMP_LNAME="Freed" EMP_FNAME="Alex" EMP_SALARY=89000 />
   			<EMPLOYEE EMP_LNAME="Best" EMP_FNAME="Alec" EMP_SALARY=60000 />
   			<EMPLOYEE EMP_LNAME="Snedden" EMP_FNAME="Sam" EMP_SALARY=48000 />
   			<EMPLOYEE EMP_LNAME="Kirkish" EMP_FNAME="Joseph" EMP_SALARY=95000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Headquarters" DNUMBER="1" MGR_LNAME="Borg" MGR_FNAME="James">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Borg" EMP_FNAME="James" EMP_SALARY=55000 />
   			<EMPLOYEE EMP_LNAME="Carpenter" EMP_FNAME="Jisha" EMP_SALARY=15000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="HR" DNUMBER="9" MGR_LNAME="Linda" MGR_FNAME="Juan">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="King" EMP_FNAME="Ray" EMP_SALARY=44500 />
   			<EMPLOYEE EMP_LNAME="Jarvis" EMP_FNAME="Jill" EMP_SALARY=36000 />
   			<EMPLOYEE EMP_LNAME="Ted" EMP_FNAME="Kim" EMP_SALARY=50000 />
   			<EMPLOYEE EMP_LNAME="Liang" EMP_FNAME="Percy" EMP_SALARY=55000 />
   			<EMPLOYEE EMP_LNAME="Mary" EMP_FNAME="willie" EMP_SALARY=12000 />
   			<EMPLOYEE EMP_LNAME="Smith" EMP_FNAME="Johny" EMP_SALARY=65000 />
   			<EMPLOYEE EMP_LNAME="Linda" EMP_FNAME="Juan" EMP_SALARY=55000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Networking" DNUMBER="3" MGR_LNAME="Gupta" MGR_FNAME="Sunil">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Gupta" EMP_FNAME="Sunil" EMP_SALARY=80000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Research" DNUMBER="5" MGR_LNAME="Wong" MGR_FNAME="Franklin">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Wong" EMP_FNAME="Franklin" EMP_SALARY=40000 />
   			<EMPLOYEE EMP_LNAME="English" EMP_FNAME="Joyce" EMP_SALARY=25000 />
   			<EMPLOYEE EMP_LNAME="Sondrini" EMP_FNAME="Andrea" EMP_SALARY=65000 />
   			<EMPLOYEE EMP_LNAME="Morgan" EMP_FNAME="Michael" EMP_SALARY=73500 />
   			<EMPLOYEE EMP_LNAME="Narayan" EMP_FNAME="Ramesh" EMP_SALARY=38000 />
   			<EMPLOYEE EMP_LNAME="Miller" EMP_FNAME="James" EMP_SALARY=75000 />
   			<EMPLOYEE EMP_LNAME="Smith" EMP_FNAME="John" EMP_SALARY=30000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Sales" DNUMBER="8" MGR_LNAME="James" MGR_FNAME="John">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Small" EMP_FNAME="Gerald" EMP_SALARY=29000 />
   			<EMPLOYEE EMP_LNAME="Kramer" EMP_FNAME="Jon" EMP_SALARY=41500 />
   			<EMPLOYEE EMP_LNAME="King" EMP_FNAME="Billie" EMP_SALARY=38000 />
   			<EMPLOYEE EMP_LNAME="Leslie" EMP_FNAME="Lyle" EMP_SALARY=41000 />
   			<EMPLOYEE EMP_LNAME="Joy" EMP_FNAME="Jennifer" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="King" EMP_FNAME="Kate" EMP_SALARY=44000 />
   			<EMPLOYEE EMP_LNAME="Head" EMP_FNAME="Arnold" EMP_SALARY=33000 />
   			<EMPLOYEE EMP_LNAME="Pataki" EMP_FNAME="Helga" EMP_SALARY=32000 />
   			<EMPLOYEE EMP_LNAME="Drew" EMP_FNAME="Naveen" EMP_SALARY=34000 />
   			<EMPLOYEE EMP_LNAME="Reedy" EMP_FNAME="Carl" EMP_SALARY=32000 />
   			<EMPLOYEE EMP_LNAME="Hall" EMP_FNAME="Sammy" EMP_SALARY=37000 />
   			<EMPLOYEE EMP_LNAME="Bacher" EMP_FNAME="Red" EMP_SALARY=33500 />
   			<EMPLOYEE EMP_LNAME="Cucuou" EMP_FNAME="Sheldon" EMP_SALARY=35500 />
   			<EMPLOYEE EMP_LNAME="Lewallen" EMP_FNAME="Roy" EMP_SALARY=75500 />
   			<EMPLOYEE EMP_LNAME="James" EMP_FNAME="John" EMP_SALARY=81000 />
   			<EMPLOYEE EMP_LNAME="Jones" EMP_FNAME="Megan" EMP_SALARY=62000 />
   			<EMPLOYEE EMP_LNAME="Maxfield" EMP_FNAME="Erin" EMP_SALARY=72000 />
   			<EMPLOYEE EMP_LNAME="Bender" EMP_FNAME="Bob" EMP_SALARY=96000 />
   		</EMPLOYEES>
   	</DEPARTMENT>
   	<DEPARTMENT DNAME="Software" DNUMBER="6" MGR_LNAME="James" MGR_FNAME="Jared">
   		<EMPLOYEES>
   			<EMPLOYEE EMP_LNAME="Ed" EMP_FNAME="John" EMP_SALARY=30000 />
   			<EMPLOYEE EMP_LNAME="Hisel" EMP_FNAME="Christina" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="Sheen" EMP_FNAME="Jake" EMP_SALARY=52000 />
   			<EMPLOYEE EMP_LNAME="Grace" EMP_FNAME="Kim" EMP_SALARY=79000 />
   			<EMPLOYEE EMP_LNAME="Chase" EMP_FNAME="Jeff" EMP_SALARY=44000 />
   			<EMPLOYEE EMP_LNAME="Barbara" EMP_FNAME="Jose" EMP_SALARY=35000 />
   			<EMPLOYEE EMP_LNAME="Burklow" EMP_FNAME="Cindy" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="Ball" EMP_FNAME="Nandita" EMP_SALARY=62000 />
   			<EMPLOYEE EMP_LNAME="Wolowitz" EMP_FNAME="Penny" EMP_SALARY=17000 />
   			<EMPLOYEE EMP_LNAME="Geller" EMP_FNAME="Zach" EMP_SALARY=55000 />
   			<EMPLOYEE EMP_LNAME="Knight" EMP_FNAME="Brad" EMP_SALARY=44000 />
   			<EMPLOYEE EMP_LNAME="Mark" EMP_FNAME="Justin" EMP_SALARY=40000 />
   			<EMPLOYEE EMP_LNAME="Jones" EMP_FNAME="Jon" EMP_SALARY=45000 />
   			<EMPLOYEE EMP_LNAME="James" EMP_FNAME="Jared" EMP_SALARY=85000 />
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
- Update mongodb version