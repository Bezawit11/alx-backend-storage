-- script that creates a trigger that decreases the quantity of an item
CREATE TRIGGER order_item AFTER UPDATE
ON items FOR EACH ROW
BEGIN
