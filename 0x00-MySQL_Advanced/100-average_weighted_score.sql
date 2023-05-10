-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT)
BEGIN
    SELECT c.user_id, c.score * p.weight
    FROM corrections c
    INNER JOIN projects p
    ON p.project_id = c.user_id
    WHERE c.user_id = user_id;
END
$$
DELIMITER ;
