--This File contains the definitions of the tables used in the application

--User
create table usr(usr_id serial primary key, usr_fname varchar(20), usr_lname varchar(20), usr_email varchar(20));

--System Administrator
create table sys_admin(sa_id serial primary key, sa_user varchar(20), sa_password varchar(20), usr_id integer references usr(usr_id));

--User`s Phone
create table phone(phone_id serial primary key, usr_id integer references usr(usr_id), usr_phone char(10));

--Client
create table client(c_id serial primary key, c_usr varchar(20), c_password varchar(20), usr_id integer references usr(usr_id));

--Supplier
create table supplier(s_id serial primary key, s_usr varchar(20), s_password varchar(20),s_location varchar(20), s_resources varchar(20), usr_id integer references usr(usr_id));

--Credit Card
create table creditcard(cc_id serial primary key, cc_nameOnCard varchar(20), cc_expdate varchar(20), cc_cvc integer, c_id integer references client(c_id));

create table CreditCardNumber( cc_number_id serial primary key, cc_id integer references creditcard(cc_id), cc_number varchar(30));

--Request
create table request(rq_id serial primary key, rq_date varchar(20));

--Reservation
create table reservation(rs_id serial primary key, rs_date varchar(20));

--Resources
create table resources(resr_id serial primary key, resr_price float, resr_location varchar(20), resr_category varchar(20), stock integer);

--Water
create table water(h2O_id serial primary key, h2O_volume float, resr_id integer references resources(resr_id));

--Medicine
create table medicine(med_id serial primary key, med_name varchar(20), resr_id integer references resources(resr_id));

--Baby Food
create table babyfood(bb_id serial primary key, bb_expdate varchar(20), bb_flavor varchar(20), resr_id integer references resources(resr_id));

--Canned Food
create table cannedfood(cf_id serial primary key, cf_expdate varchar(20), cf_name varchar(20), resr_id integer references resources(resr_id));

--Dry Food
create table dryfood(df_id serial primary key, df_expdate varchar(20), df_name varchar(20), resr_id integer references resources(resr_id));

--ICE
create table ice(ice_id serial primary key, ice_bagSize varchar(20), resr_id integer references resources(resr_id));

--Fuel
create table fuel(fuel_id serial primary key, fuel_type varchar(20), resr_id integer references resources(resr_id));

--Medical Devices
create table medicaldevices(mdev_id serial primary key, mdev_name varchar(20), mdev_description varchar(50), resr_id integer references resources(resr_id));

--Heavy Equip
create table heavyequip(heq_id serial primary key, heq_type varchar(20), resr_id integer references resources(resr_id));

--Tools
create table tools(tool_id serial primary key, tool_name varchar(20), resr_id integer references resources(resr_id));

--Clothing
create table clothing(cl_id serial primary key, cl_size varchar(20), cl_color varchar(20), cl_material varchar(20), resr_id integer references resources(resr_id));

--Power Generator
create table powergenerator(pg_id serial primary key, pg_wattage float, pg_fuelType varchar(20), resr_id integer references resources(resr_id));

--Batteries
create table batteries(batt_id serial primary key, batt_type varchar(20), resr_id integer references resources(resr_id));

------------------------------------Relationships

--Administrate
create table Administrate(sa_id integer references sys_admin(sa_id), usr_id integer references usr(usr_id), primary key (sa_id, usr_id));

--Places
create table Places(c_id integer references client(c_id), rq_id integer references request(rq_id), primary key(c_id,rq_id));

--Makes
create table Makes(c_id integer references client(c_id), rs_id integer references reservation(rs_id), primary key (c_id, rs_id));

--Transaction
create table Transaction(cc_id integer references creditcard(cc_id), rq_id integer references request(rq_id), transaction_num integer,primary key (cc_id,rq_id));

--Purchases
create table Purchases(rq_id integer references request(rq_id),  resr_id integer references resources(resr_id), purchase_price float, quantity integer, primary key (rq_id,resr_id));

--Confirmation
create table Confirmation(rs_id integer references reservation(rs_id), resr_id integer references resources(resr_id), confirmation_status varchar(20), primary key (rs_id,resr_id));

--Provides
create table Provides(s_id integer references supplier(s_id), resr_id integer references resources(resr_id), primary key (s_id,resr_id));