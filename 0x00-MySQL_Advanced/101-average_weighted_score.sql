-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    DECLARE RowCnt INT;
    DECLARE avg_score FLOAT;
    DECLARE b INT = 1;
    SET RowCnt = (SELECT COUNT(*) FROM corrections);
    WHILE b <= RowCnt
    BEGIN    
        SET avg_score = (SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        INNER JOIN projects p
        ON p.id = c.project_id)
        WHERE c.user_id = b;
        UPDATE users SET average_score = avg_score WHERE id = b;
        SET b += 1;
    END
END
$$
DELIMITER ;
