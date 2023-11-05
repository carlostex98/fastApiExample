create database library;
use library;



create table books(
    book_id bigint unsigned primary key auto_increment,
    title varchar(220),
    description text,
    date_added datetime
);