-- PostgreSQL: jalankan pada database latihan kampus yang sudah dibuat.
-- psql -h localhost -U nama_akun -d kampus -f setup.sql
BEGIN;
CREATE TABLE IF NOT EXISTS employee (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
INSERT INTO employee (id, name) VALUES
  (101, 'Alya'), (102, 'Bima'), (103, 'Citra')
ON CONFLICT (id) DO NOTHING;
COMMIT;
