-- frjfn
SELECT COUNT(*) AS number, score
FROM second_table
GROUP BY score
ORDER BY number DESC;
