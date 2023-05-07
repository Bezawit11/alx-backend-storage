-- script that creates a trigger that decreases the quantity of an item
CREATE TRIGGER order_item AFTER INSERT ON
ON orders FOR EACH ROW
UPDATE items
SET quantity = 'Alfred Schmidt' WHERE name = NEW.item_names;
