SELECT
    d.Dname, d.Dnumber,
    mgr.Lname, mgr.Fname,
    e.Lname, e.Fname, e.Salary
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE mgr ON d.Mgrssn = mgr.Ssn
    INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
ORDER BY
    d.Dname, mgr.Lname, mgr.Fname, e.Lname, e.Fname;