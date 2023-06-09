-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT SUM(c.score * p.weight) / SUM(p.weight)
    FROM corrections c
    INNER JOIN projects p
    ON p.id = c.project_id
    WHERE c.user_id = user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END
$$
DELIMITER ;
