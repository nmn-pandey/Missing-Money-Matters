-- Challenge 2
-- Q1

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: Get a list of customers who made purchases between 2011 and 2012.
*/

SELECT 
	c.FirstName as [First Name],
	c.LastName as [Last Name],
	c.Email as Email,
	c.Address as Address,
	c.City as City,
	c.State as State
FROM
	Invoice AS i
INNER JOIN
	Customer AS c
ON
	i.CustomerId = c.CustomerId
WHERE
	date(i.InvoiceDate) <= '2012-12-31' 
	AND
	date(i.InvoiceDate) >= '2011-01-01' 
GROUP BY
	c.City, c.State, c.FirstName, c.LastName
ORDER BY
	c.FirstName
