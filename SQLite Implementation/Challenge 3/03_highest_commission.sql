-- Challenge 3
-- Q3

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: Which employee made the highest commission?
*/


SELECT 
	e.FirstName as [First Name],
	e.LastName as [Last Name],
	e.EmployeeId as [Employee ID],
	sum(i.Total) as [Sales Made],
	round(0.15 * sum(i.Total), 2) AS [Commission Payout]
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
GROUP BY
	e.EmployeeId
ORDER BY
	sum(i.Total) DESC,
	e.FirstName
LIMIT 1