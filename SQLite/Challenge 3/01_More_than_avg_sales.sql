-- Challenge 3
-- Q1

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: Get a list of employees who exceeded the average transaction amount from sales they generated during 2011 and 2012.
*/


SELECT 
	e.FirstName as [First Name],
	e.LastName as [Last Name],
	e.EmployeeId as [Employee ID],
	sum(i.Total) as [Sales Made]
FROM
	Invoice AS i
INNER JOIN
	Customer AS c
ON
	i.CustomerId = c.CustomerId
INNER JOIN
	Employee AS e
ON
	e.EmployeeId = c.SupportRepId
WHERE
	date(i.InvoiceDate) <= '2012-12-31' 
	AND
	date(i.InvoiceDate) >= '2011-01-01' 
	AND
	i.Total >  (SELECT AVG(Total) FROM Invoice WHERE date(InvoiceDate) <= '2012-12-31'  AND date(InvoiceDate) >= '2011-01-01' ) --11.66
GROUP BY
	e.EmployeeId
ORDER BY
	e.FirstName;