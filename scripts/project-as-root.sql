SELECT
    JSON_OBJECT(
        'PNAME', p.Pname,
        'PNUMBER', p.Pnumber,
        'DNAME', d.Dname,
        'EMPLOYEES', JSON_ARRAYAGG(JSON_OBJECT(
            'EMP_LNAME', e.Lname,
            'EMP_FNAME',e.Fname,
            'HOURS', w.Hours
        ))
    ) as project_document
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn AND w.Pno = p.Pnumber
GROUP BY
    p.Pname, p.Pnumber, d.Dname;