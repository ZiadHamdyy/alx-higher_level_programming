-- creates the table unique_id on your MySQL server.
SELECT 1 FROM tables 
  WHERE table_schema = DATABASE() 
  AND table_name = 'unique_id' 
  LIMIT 1;

CREATE TABLE IF NOT EXISTS (
  id INT DEFAULT 1,
  name VARCHAR(256)
  UNIQUE (id)
);