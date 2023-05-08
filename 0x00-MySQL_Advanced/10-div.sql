-- script that creates a function SafeDiv
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DATE
   DETERMINISTIC
   BEGIN
        IF (b) = 0
    THEN
         return 0;
    END IF;
         return a / b;
   END
