-- Challenge 2
-- Q3

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: How many transactions are above the average transaction amount during the same time period?
*/

SELECT 
	count(*) AS [Transactions above Average]
FROM
	Invoice
WHERE
	total > ( SELECT AVG(total) FROM INVOICE WHERE date(InvoiceDate) <= '2012-12-31'  AND date(InvoiceDate) >= '2011-01-01' )
