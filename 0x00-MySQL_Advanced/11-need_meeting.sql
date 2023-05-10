-- creates a view that lists all students that have a score under 80
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS SELECT * students WHERE
score < 80 AND 
(last_meeting IS NULL OR last_meeting > 1 MONTH);
