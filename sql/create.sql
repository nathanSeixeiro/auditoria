CREATE DATABASE auditoria;

CREATE TABLE auditoria (
    checklist_id INT PRIMARY KEY,
    pattern int NOT NULL,
    section varchar(255) NOT NULL,
    sub_section varchar(255) NOT NULL,
    question varchar(255) NOT NULL,
    aswer char(3) NOT NULL,
    compliance varchar(255) NOT NULL
    );