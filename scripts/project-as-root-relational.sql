SELECT
    p.Pname, p.Pnumber,
    d.Dname,
    e.Lname, e.Fname,
    w.Hours
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn
ORDER BY
    p.Pname;