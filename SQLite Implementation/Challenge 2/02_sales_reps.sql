-- Challenge 2
-- Q2

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: Get a list of customers, sales reps, and total transaction amounts for each customer between 2011 and 2012.
*/

SELECT 
	c.FirstName ||' '|| c.LastName as Name,
	c.Email as Email,
	c.Address ||', '|| c.City ||', '|| c.State as Address,
	e.FirstName ||' '||e.LastName as [Sales Rep],
	sum(i.Total) as [Purchases Made]
FROM
	Invoice AS i
INNER JOIN
	Customer AS c
ON
	i.CustomerId = c.CustomerId
INNER JOIN
	Employee AS e
ON
	c.SupportRepId = e.EmployeeId
WHERE
	date(i.InvoiceDate) <= '2012-12-31' 
	AND
	date(i.InvoiceDate) >= '2011-01-01' 
GROUP BY
	c.City, c.State, c.FirstName, c.LastName
ORDER BY
	c.FirstName
