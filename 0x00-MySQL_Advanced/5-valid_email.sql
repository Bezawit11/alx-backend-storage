-- script that creates a trigger that resets the attribute valid_email
CREATE TRIGGER validate_email
AFTER UPDATE ON users
FOR EACH ROW
IF NEW.email <> OLD.email
THEN
    UPDATE users SET valid_email = 1 WHERE = NEW.email;
END IF;
