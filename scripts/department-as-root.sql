SELECT
    JSON_OBJECT(
        'DNAME', d.Dname,
        'DNUMBER', d.Dnumber,
        'MGR_LNAME',mgr.Lname,
        'MGR_FNAME', mgr.Fname,
        'EMPLOYEES', JSON_ARRAYAGG(JSON_OBJECT(
                'EMP_LNAME',e.Lname,
                'EMP_FNAME', e.Fname,
                'EMP_SALARY', e.Salary
            ))
    ) as department_document
FROM
    DEPARTMENT d INNER JOIN EMPLOYEE mgr ON d.Mgrssn = mgr.Ssn
    INNER JOIN EMPLOYEE e ON e.Dno = d.Dnumber
GROUP BY d.Dname, d.Dnumber, mgr.Lname, mgr.Fname
