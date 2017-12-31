create database glas collate='utf8_general_ci' character set='utf8'
create table logrows (seq serial, year char(4), month char(3), message varchar(255), cnt int);
grant all privileges on glas.* to glasuser@localhost identified by 'glaspassword' with grant option;
flush privilegs;

