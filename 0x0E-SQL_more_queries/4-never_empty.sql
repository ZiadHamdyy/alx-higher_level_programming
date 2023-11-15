-- creates the table id_not_null on your MySQL server.
SELECT 1 FROM tables 
  WHERE table_schema = 'hbtn_0d_2' 
  AND table_name = 'id_not_null' 
  LIMIT 1;

CREATE TABLE IF NOT EXISTS id_not_null (
  id INT NOT NULL DEFAULT 1,
  name VARCHAR(256)
);
