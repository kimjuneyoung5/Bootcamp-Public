-- add 3 dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Shawn Converse", NOW(), NOW()),
	("Edward Im", NOW(), NOW()),
    ("Christian L", NOW(), NOW());

-- read dojos
SELECT * FROM dojos;
SELECT name FROM dojos;

-- delete 3 dojos
DELETE FROM dojos WHERE id < 4;

-- add 3 more dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ("Shawn Converse", NOW(), NOW()),
	("Edward Im", NOW(), NOW()),
    ("Christian L", NOW(), NOW());
    
-- add 3 ninjas to first dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("June", "Kim", 25, NOW(), NOW(), 4),
	("Brendan", "Stanton", 24, NOW(), NOW(), 4),
    ("Jim", "Reeder", 26, NOW(), NOW(), 4);
 
 -- add 3 ninjas to second dojo
 INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Mike", "Kim", 23, NOW(), NOW(), 5),
	("Tony", "Stark", 22, NOW(), NOW(), 5),
    ("Michael", "Jackson", 19, NOW(), NOW(), 5);

-- add 3 ninjas to third dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
VALUES ("Robert", "Downey Jr.", 20, NOW(), NOW(), 6),
	("Chris", "Evans", 21, NOW(), NOW(), 6),
    ("Chris", "Hemsworth", 27, NOW(), NOW(), 6);
    
-- retrieve all ninjas 
SELECT * from ninjas WHERE dojo_id = 6;
SELECT * from ninjas WHERE dojo_id = 5;
SELECT * from ninjas WHERE dojo_id = 4;
SELECT * from dojos JOIN ninjas ON dojo_id = ninjas.dojo_id WHERE dojo_id = 4;