-- script that creates a stored procedure AddBonus
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score FLOAT
)
BEGIN
    DECLARE p_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SET pid = (SELECT id FROM projects WHERE name = project_name LIMIT 1); 
    INSERT INTO corrections (user_id, project_id, score) values (user_id, p_id, score);
END
