-- Challenge 1
-- Q2

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: How much money did WSDA Music make during the same period?
*/

SELECT 
	sum(Total)AS [Total Sales]
FROM
	Invoice
WHERE
	date(InvoiceDate) <= '2012-12-31' 
	AND
	date(InvoiceDate) >= '2011-01-01' 

-- 1947.97