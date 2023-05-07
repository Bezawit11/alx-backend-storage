-- script that creates a trigger that resets the attribute valid_email
CREATE TRIGGER validate_email
AFTER UPDATE ON users
FOR EACH ROW
UPDATE users SET valid_email WHERE = NEW.email;
