-- Selects cities which are in california
-- cities table is connected to state via state_id
SELECT id, name
  FROM cities
 WHERE state_id = (
	SELECT id
	  FROM states
	WHERE name = 'California'
)
 ORDER BY id ASC;
