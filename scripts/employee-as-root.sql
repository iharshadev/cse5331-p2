SELECT
    JSON_OBJECT(
        'EMP_LNAME', e.Lname,
        'EMP_FNAME', e.Fname,
        'DNAME', d.Dname,
        'PROJECTS', JSON_ARRAYAGG(JSON_OBJECT(
            'PNAME', p.Pname,
            'PNUMBER', p.Pnumber,
            'HOURS', w.Hours
        ))
    ) as employee_document
FROM
    EMPLOYEE e INNER JOIN DEPARTMENT d ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn AND w.Pno = p.Pnumber
GROUP BY e.Lname, e.Fname, d.Dname;