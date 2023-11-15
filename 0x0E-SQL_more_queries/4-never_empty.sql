-- creates the table id_not_null on your MySQL server.
SELECT 1 FROM tables 
  WHERE table_schema = DATABASE() 
  AND table_name = 'id_not_null' 
  LIMIT 1;

CREATE TABLE IF NOT EXISTS (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);
