SELECT
    e.Lname, e.Fname,
    d.Dname,
    p.Pname, p.Pnumber,
    w.Hours
FROM
    EMPLOYEE e INNER JOIN DEPARTMENT d ON e.Dno = d.Dnumber
    INNER JOIN PROJECT p ON p.Dnum = d.Dnumber
    INNER JOIN WORKS_ON w ON w.Essn = e.Ssn
ORDER BY
    e.Lname, e.Fname;