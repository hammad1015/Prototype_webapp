show databases;
create database build_guild;
USE build_guild;
SHOW TABLES;

-- Insert SQL
INSERT INTO user VALUES (1, "faisal@example.com", "Faisal Rasool", "pop" , 0);
INSERT INTO user VALUES (2, "rafey@example.com", "Abdul Rafey", "pop", 0);
INSERT INTO user VALUES (3, "manager@example.com", "Manager 1", "pop", 1);

INSERT INTO buyer VALUES (1, "Hadi Ali", 12345,  null);
INSERT INTO buyer VALUES (2, "Haider Ali", 12346,  null);

INSERT INTO plot VALUES (1, "first", 2000000, "7 marla",  "not sold", "nothing");
INSERT INTO plot VALUES (2, "second", 100000, "2 marla",  "not sold", "nothing");
INSERT INTO plot VALUES (3, "third", 300000, "5 marla",  "not sold", "nothing");
INSERT INTO plot VALUES (4, "fourth", 500000, "5 marla",  "not sold", "nothing");
INSERT INTO plot VALUES (5, "fifth", 2000000, "7 marla",  "not sold", "nothing");

-- Deleting SQL
DELETE FROM user WHERE id=2;

-- Droping Tables
DROP TABLE transaction;
DROP TABLE deal;
DROP TABLE notes;
DROP TABLE commissionagent;
DROP TABLE buyer;
DROP TABLE plot;
DROP TABLE user;


-- Selecting
SELECT * FROM user;