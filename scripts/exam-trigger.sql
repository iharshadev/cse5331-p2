create table student(
    ssn integer primary key,
    name varchar(30),
    major varchar(30),
    class varchar(30)
);

create table section(
    section_id integer primary key,
    cno integer,
    semester varchar(30),
    year integer,
    instructor varchar(30)
);
create table grades(
    ssn integer,
    section_id integer,
    grade char(1),
    foreign key (ssn) references student(ssn),
    foreign key (section_id) references section(section_id)
)
INSERT INTO student VALUES (1, 'ABC', 'CSE', 'SUM20');
INSERT INTO section VALUES (1, 5311, 'SUM20', 2020, 'John');
INSERT INTO grades VALUES (1, 1, 'A');

SELECT COUNT(*) from grades where section_id = 1;

CREATE TRIGGER No_students
AFTER INSERT ON grades
FOR EACH ROW
UPDATE section set no_students =(SELECT COUNT(*) from grades where section_id = new.section_id)
where section_id = new.section_id;

select * from section;

INSERT INTO student VALUES (2, 'DEF', 'CSE', 'SUM20');
INSERT INTO grades VALUES (2, 1, 'A');
commit;