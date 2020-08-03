SELECT
    JSON_OBJECT(
        'project_name', p.Pname,
        'project_number', p.Pnumber,
        'department_name', d.Dname,
        'employees', JSON_ARRAYAGG(JSON_OBJECT(
            'Fname',e.Fname,
            'Lname', e.Lname,
            'Hours', w.Hours
        ))
    ) as project_document
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn
GROUP BY
    p.Pname, p.Pnumber, d.Dname;