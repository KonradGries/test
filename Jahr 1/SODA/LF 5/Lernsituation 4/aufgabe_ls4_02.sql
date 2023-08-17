insert into suppliers (`SupplierName`) 
VALUES ("Lieferant1"),("Lieferant2"),("Lieferant3");

insert into shippers (`ShipperName`) 
VALUES ("Spediteure1"),("Spediteure2"),("Spediteure3");

insert into employees (`LastName`) 
VALUES ("Mitarbeiter1"),("Mitarbeiter2"),("Mitarbeiter3");

SELECT SupplierName from suppliers;
SELECT ShipperName from shippers;
SELECT LastName from employees;

select * from products;

select * from shippers;

Select suppliers.SupplierName, products.ProductName from suppliers 
inner join products;

Select suppliers.SupplierName, products.ProductName from suppliers
left join products on suppliers.SupplierID = products.SupplierID;

Select suppliers.SupplierName, products.ProductName from products
right join suppliers on products.SupplierID = suppliers.SupplierID;

Select shippers.ShipperName, orders.orderID from shippers
left join orders on  shippers.ShipperID = orders.ShipperID;