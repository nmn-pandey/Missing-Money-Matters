-- Challenge 1
-- Q1

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: How many transactions took place between the years 2011 and 2012?
*/

SELECT 
	count(*) AS [Number of Transactions]
FROM
	Invoice
WHERE
	date(InvoiceDate) <= '2012-12-31' 
	AND
	date(InvoiceDate) >= '2011-01-01' 
	
-- 167
