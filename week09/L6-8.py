'''
CREATE TABLE team (  
    id INT PRIMARY KEY AUTO_INCREMENT,  
    teamName VARCHAR(50) NOT NULL  
);

CREATE TABLE score (  
    id INT PRIMARY KEY AUTO_INCREMENT,  
    teamid INT,  
    userid INT,  
    score INT,  
    FOREIGN KEY (teamid) REFERENCES team(id),  
    FOREIGN KEY (userid) REFERENCES user(id)  -- 注意：这里假设user表已经存在并且有id字段作为主键  
);
'''