show databases;
create database bookshop_database;
use bookshop_database;
show tables;

CREATE TABLE vs_members( emp_id int,username varchar(40),age int,address varchar(50),doj varchar(20), user_password varchar(15), PRIMARY KEY (emp_id));
ALTER TABLE vs_members add Employee_Type varchar(40);

select * from vs_members;
drop table vs_members;

select sysdate();

#employee details
insert into vs_members values( 100, 'Vasu100',19,"Rangareddy, Telangana",date(sysdate()),"Vasu#100","Manager");
insert into vs_members values( 101, 'Sravya101',20,"Prakasham, Andhrapradesh",date(sysdate()),"Sravya#101","Employee");
insert into vs_members values( 102, 'Vinod102',21,"Shamshabad, Telangana",date(sysdate()),"Vinod#102","Sales Clerk");

#manipulation command
delete from vs_members
where emp_id=102;
delete from vs_members
where emp_id=104;
drop table vs_members;


#customer_details
create table customer_details( 
	full_name varchar(40), contact_number varchar(12), address varchar(50), purchased_books varchar(200), paid_amount int,time_date varchar(20),primary key (full_name)
);
select* from customer_details;

delete from customer_details
where contact_number="9121307967";


#inventory
create table Inventory( ISBN varchar(17), title varchar(50), author_name varchar(40),published_year int, quantity int, rack_number int,sell_price float);

alter table inventory add primary key(ISBN) ;

insert into inventory values("978-93-5163-389-1", "Data Structure Using C", "Sharad Kumar Verma",2015,1,1,100);
insert into inventory values("978-93-8067-432-2", "Client Server Computing", "Sharad Kumar Verma",2012,1,1,110);
insert into inventory values("978-93-8067-432-3", "Client Server Computing", "Lalit Kumar",2012,1,1,110);
insert into inventory values("978-93-89474-49-7", "Ordinary Differential Equations", "Dr. Deepjyoti Kalita",2012,1,5,140);

update inventory
set quantity=3
where ISBN="978-93-8067-432-3" ;
 
select * from inventory;

alter table inventory drop date_time;
  #stockist
 create table stockist_details( 
 full_name varchar(40), contact_number varchar(12), address varchar(50), author_books varchar(200), primary key (full_name));
 
 
 
 
 # sales stats
 create table sales_statistics(
 time_date varchar(20), full_name varchar(40), books_sold varchar(100), quantity int,amount float);
 
 
 
 
 # cart
 create table cart( time_date varchar(40), customer_name  varchar(40), isbn_no varchar(17), title varchar(40), author varchar(40), no_of_books int, sell_price float);
 
 select * from cart;
 
 alter table cart ;
 
 alter table cart add rack_number int;
 drop table cart;
 #request field
 create table request_field( serial_number int auto_increment,date_time varchar(40), customer_name varchar(40), contact_number varchar(12),book_title varchar(40), book_author varchar(40),primary key(serial_number));

ALTER TABLE request_field auto_increment=1;

select * from request_field;

delete from request_field
where customer_name="Katarvath Vasu";

drop table request_field;
 