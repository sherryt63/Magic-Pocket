'''
SELECT u.*   
FROM user u  
JOIN score s ON u.id = s.userid  
JOIN team t ON s.teamid = t.id  
WHERE t.teamName = 'ECNU' AND u.age < 20;
'''