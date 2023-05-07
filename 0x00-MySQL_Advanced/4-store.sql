-- script that creates a trigger that decreases the quantity of an item
CREATE TRIGGER order_item AFTER INSERT
ON orders FOR EACH ROW
UPDATE items
SET quantity = items.quantity - NEW.numbers WHERE name = NEW.item_names;
