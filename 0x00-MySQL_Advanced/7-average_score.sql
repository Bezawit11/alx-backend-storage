-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE av FLOAT;
    SET av = (SELECT AVG(score) FROM corrections WHERE user_id=user_id);
    UPDATE users SET average_score = av WHERE id=user_id;
END
$$
DELIMITER ;
