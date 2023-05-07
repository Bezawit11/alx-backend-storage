-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE a FLOAT;
    SET a = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    UPDATE users SET average_score = a WHERE id = user_id;
END
$$
DELIMITER ;
