-- Challenge 3
-- Q5

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: Which customer made the highest purchase?
*/

SELECT
	c.FirstName || ' ' || c.LastName AS Name,
	c.Address || ', ' || c.City || ', ' || c.State as Address,
	c.CustomerId as [Customer ID],
	sum(i.Total) as [Purchase Made]
FROM
	Invoice AS i
INNER JOIN 
	Customer AS c ON i.CustomerId = c.CustomerId 
INNER JOIN 
	Employee AS e ON e.EmployeeId = c.SupportRepId 
WHERE 
	date(i.InvoiceDate) <= '2012-12-31'  AND date(i.InvoiceDate) >= '2011-01-01'  
	AND 
	c.SupportRepId = 3
GROUP BY Name
ORDER BY i.Total DESC

-- John Doeein