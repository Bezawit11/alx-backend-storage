-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE av FLOAT;
    SET av = (SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id);
    UPDATE users SET average_score = av WHERE id=user_id;
END
$$
DELIMITER ;
