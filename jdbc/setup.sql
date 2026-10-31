-- Contoh tambahan. Jalankan pada database latihan MySQL.
CREATE DATABASE IF NOT EXISTS kampus;
USE kampus;
CREATE TABLE IF NOT EXISTS employee (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
INSERT INTO employee (id, name) VALUES
  (101, 'Alya'), (102, 'Bima'), (103, 'Citra');
