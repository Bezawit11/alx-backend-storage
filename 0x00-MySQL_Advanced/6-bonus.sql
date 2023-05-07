-- script that creates a stored procedure AddBonus
CREATE PROCEDURE AddBonus(user_id, project_name, score)
BEGIN
  DECLARE project_id INT;
  IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
  THEN
      INSERT INTO projects (name) values (project_name);
  END IF;
  SET project_id = (SELECT id FROM projects WHERE name = project_name); 
  INSERT INTO Corrections (user_id, project_id, score) values (user_id, project_id, score);
END
