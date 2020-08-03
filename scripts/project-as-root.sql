SELECT
    p.Pname, p.Pnumber ,d.Dname,
    JSON_OBJECTAGG(JSON_OBJECT(
        'Fname',e.Fname,
        'Lname', e.Lname,
        'Hours', w.Hours
    ) ) as employee
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn
GROUP BY
    p.Pname, p.Pnumber, d.Dname
ORDER BY 1,3