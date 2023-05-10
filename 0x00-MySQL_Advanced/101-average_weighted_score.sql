-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    DECLARE avg_score FLOAT;
    UPDATE users SET average_score = (SELECT SUM(c.score * p.weight) / SUM(p.weight)
    FROM corrections c
    INNER JOIN projects p
    ON p.id = c.project_id);
END
$$
DELIMITER ;
