-- Trigger to decrease item quantity when a new order is insterted

DELIMITER $$

CREATE TRIGGER decrease_quanitity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
