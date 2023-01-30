
DROP DATABASE IF EXISTS muhely;
CREATE DATABASE muhely;
USE kuyamenhely;
  
DROP TABLE IF EXISTS kutya,;
  
CREATE TABLE szgk(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    tipus VARCHAR(20) DEFAULT 'Toyota', 
    modell VARCHAR(20) NOT NULL, 
    rendszam VARCHAR(15) UNIQUE, 
    ajtok_szama INT CHECK (ajtok_szama < 6),
    gyartas_eve DATE
);
  
INSERT INTO szgk (tipus, modell, rendszam, ajtok_szama, gyartas_eve)
VALUES('Opel', 'Corsa C', 'AAA123', 14, '2002-10-03'); 
  