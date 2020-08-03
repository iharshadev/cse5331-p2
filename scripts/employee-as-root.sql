SELECT
    JSON_OBJECT(
        'employee_lname', e.Lname,
        'employee_fname', e.Fname,
        'department_name', d.Dname,
        'projects', JSON_ARRAYAGG(JSON_OBJECT(
            'project_name', p.Pname,
            'project_number', p.Pnumber,
            'project_hours', w.Hours
        ))
    ) as employee_document
FROM
    EMPLOYEE e INNER JOIN DEPARTMENT d ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn
GROUP BY e.Lname, e.Fname, d.Dname;