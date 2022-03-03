show databases;
use bookshop_database;
show tables;

create table customer_details( 
	full_name varchar(40), contact_number varchar(12), address varchar(50), purchased_books varchar(200), paid_amount int,time_date timestamp,primary key (full_name)
);

create table Inventory( ISBN varchar(17), title varchar(50), author_name varchar(40),published_year int, quantity int, rack_number int,sell_price float);

alter table inventory add primary key(ISBN) ;
 insert into inventory values( "978-93-5163-389-1", "Data Structure Using C", "Sharad Kumar Verma",2015,1,1,100);
 
 insert into inventory values( "978-93-8067-432-2", "Client Server Computing", "Sharad Kumar Verma",2012,1,1,110);
 
insert into inventory values( "978-93-8067-432-3", "Client Server Computing", "Lalit Kumar",2012,1,1,110);

insert into inventory values( "978-93-89474-49-7", "Ordinary Differential Equations", "Dr. Deepjyoti Kalita",2012,1,5,140);

update inventory
set quantity=3
where ISBN="978-93-8067-432-3" ;
 
 create table stockist_details( 
 full_name varchar(40), contact_number varchar(12), address varchar(50), author_books varchar(200), primary key (full_name));
 
 create table sales_statistics(
 time_date timestamp, full_name varchar(40), books_sold varchar(100), quantity int,amount float);
 
 create table cart( time_date timestamp, customer_name  varchar(40) PRIMARY KEY, isbn_no varchar(17) , title varchar(40), author varchar(40), no_of_books int, sell_price float);
 
 create table request_field( time_date timestamp, customer_name varchar(40), contact_number varchar(12),book_title varchar(40), book_author varchar(40));
 
 drop table cart;
 
 describe inventory;
 
 select * from inventory;
 
 select * from cart;
 