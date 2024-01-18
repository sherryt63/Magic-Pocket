'''
SELECT SUM(score) AS total_score  
FROM score  
WHERE teamid IN (SELECT id FROM team WHERE teamName = 'ECNU') OR score IS NULL;
'''