/*
 Beispiele für den Umgang mit SQL (I) - CRUD-Operationen
 
 Einordnung:			FISI-LF5-LS4-Beispiel-02
 Datenbank: 			w3schools
 
 Name:				Markus Breuer
 Organisaion:		BK-GuT
 
 Erstellt:			19.03.2021
 Letzte Änderung:	12.04.2021
 
 */
/* Datenbank auswählen */
USE w3schools;

/* Für alle Kunden die KundenID und den Kundennamen ausgeben */
SELECT
    CustomerID,
    CustomerName
FROM
    customers;

/* Alle Attribute aller Kunden ausgeben */
SELECT
    *
FROM
    customers;

/* ID, Name und Land aller Kunden aus Deutschland ausgeben */
SELECT
    CustomerID,
    CustomerName,
    Country
FROM
    customers
WHERE
    Country = "Germany";

/* Alle Attribute des Kunden mit der ID 1 ausgeben */
SELECT
    *
FROM
    customers
WHERE
    CustomerID = 1;

/* Alle Attribute aller Kunden aus Deutschland ausgeben, deren ID kleiner 50 ist */
SELECT
    *
FROM
    customers
WHERE
    Country = "Germany"
    AND CustomerID < 50;

/* Alle Länder ausgeben, in denen es Kunden gibt */
SELECT
    Country
FROM
    customers;

/* Alle Länder ausgeben, in denen es Kunden gibt, doppelte vermeiden */
SELECT
    DISTINCT Country
FROM
    customers
ORDER BY
    Country;

/* Einen neuen Kunden einfügen */
INSERT INTO
    customers (
        CustomerID,
        CustomerName,
        ContactName,
        Address,
        City,
        PostalCode,
        Country
    )
VALUES
    (
        100,
        "Alberts Ahr Haus",
        "Albert Ahrhaus",
        "Obere Str. 57",
        "Blankenheim",
        "11111",
        "Germany"
    );

/* Drei neuen Kunden einfügen */
INSERT INTO
    customers (
        CustomerID,
        CustomerName,
        ContactName,
        Country
    )
VALUES
    (
        101,
        "Bertas Bastelstube",
        "Berta Braun",
        "Germany"
    ),
    (102, "Zauberbude", "Carlo Clown", "Germany"),
    (
        103,
        "Maker Space Düsentrieb",
        "Daniel Düsentrieb",
        "Germany"
    );

/* Postleitzahl bei dem Kunden mit dem Namen Altert Ahrhaus auf 53945 korrigieren */
UPDATE
    customers
SET
    postalcode = "53945"
WHERE
    ContactName = "Albert Ahrhaus";

/* Kundenname bei allen Kunden auf "Rate Mal" setzen */
UPDATE
    customers
SET
    ContactName = "Rate Mal?";

/* Kunde mit der ID 100 löschen */
DELETE FROM
    customers
WHERE
    CustomerID = 100;