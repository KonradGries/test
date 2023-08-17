SELECT SupplierID,SupplierName,Country FROM suppliers;

SELECT * from shippers;
+SELECT SupplierID,SupplierName,ContactName FROM suppliers
WHERE SupplierID <= 20;

SELECT SupplierID,SupplierName,ContactName FROM suppliers
WHERE SupplierName like "%y%";

SELECT DISTINCT Country from suppliers
ORDER BY Country;

SELECT EmployeeID,LastName,BirthDate from employees
Where BirthDate  < '1960-01-01'
ORDER BY LastName desc;

SELECT EmployeeID,FirstName,LastName,BirthDate from employees
Where BirthDate  < '1960-01-01'
and LastName like '%u%'
or FirstName like '%u%'
ORDER BY LastName desc;