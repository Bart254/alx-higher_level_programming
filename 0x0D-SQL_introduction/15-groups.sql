-- Returns the scores and number of occurences in the table
SELECT score, COUNT(*) AS number
  FROM second_table
  GROUP BY score
  ORDER BY number DESC;