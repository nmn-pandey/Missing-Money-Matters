-- Challenge 3
-- Q4

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: List the customers that the employee identified in the last question.
METHOD: Although we identified the Sales Rep as 'Jane Peacock' with EmployeeId 3, we will also maintain the dynamic subquery structure.
*/
SELECT
	c.FirstName || ' ' || c.LastName AS Name,
	c.Address || ', ' || c.City || ', ' || c.State as Address
FROM
	Customer c
WHERE
	c.SupportRepId = 3
	/*(SELECT e.EmployeeId FROM Invoice AS i INNER JOIN Customer AS cu ON i.CustomerId = cu.CustomerId INNER JOIN Employee AS e ON e.EmployeeId = c.SupportRepId 
	WHERE date(i.InvoiceDate) <= '2012-12-31'  AND date(i.InvoiceDate) >= '2011-01-01' 
	GROUP BY e.EmployeeId 
	ORDER BY sum(i.Total) DESC, e.FirstName LIMIT 1)*/
ORDER BY c.FirstName