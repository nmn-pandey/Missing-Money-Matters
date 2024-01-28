-- Challenge 2
-- Q4

/*
CREATED BY: NAMAN PANDEY
DATE: 28/01/2024
DESCRIPTION: What is the average transaction amount for each year that WSDA Music has been in business?
*/

SELECT 
	strftime('%Y', InvoiceDate) AS Year,
	round(AVG(Total), 2) as [Average Transaction Amount]
FROM
	Invoice
GROUP BY
	strftime('%Y', InvoiceDate) 
