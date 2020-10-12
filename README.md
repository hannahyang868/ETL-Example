# ETL-Example
Describing some ETL processes on Hadoop using Hive, Pig and Hadoop Streaming

Input data are as follows:

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/dwdate.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/lineorder.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/part.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/supplier.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/customer.tbl

## Hive

This examples shows a ETL process on Hive to transform data and put into new table with selected columns (c_custkey, c_address, c_city). For the c_address column, shorten it to 6 characters (i.e., if the value is longer, remove extra characters, but otherwise keep it as-is). For c_city, add a space and a # to indicate the digit at the end (e.g., UNITED KI2 => UNITED KI #2, or INDONESIA4 => INDONESIA #4).

**Step 1: Create all relevant tables and load data on Hive CLI.**

create table customer (

c_custkey int,

c_name varchar(25),

c_address varchar(25),

c_city varchar(10),

c_nation varchar(15),

c_region varchar(12),

c_phone varchar(15),

c_mktsegment varchar(10))

ROW FORMAT DELIMITED FIELDS

TERMINATED BY '|' STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/ec2-user/customer.tbl' OVERWRITE INTO TABLE customer;

**Step 2: Write Hive UDF Script (Codes provided)**

**Step 3: Create new table and transform data into new table on Hive CLI**

create table customer_new (

c_custkey int,

c_address varchar(6),

c_city varchar(12))

ROW FORMAT DELIMITED FIELDS

TERMINATED BY '|' STORED AS TEXTFILE;

ADD FILE /home/ec2-user/customer_transform.py;

INSERT OVERWRITE TABLE customer_new

SELECT TRANSFORM (c_custkey,c_name,c_address,c_city,c_nation,c_region,c_phone,c_mktsegment) USING 'python customer_transform.py'
AS (c_custkey,c_address,c_city)
FROM customer;

**Step 4: Check Result on Hive CLI**

Select * from customer_new limit 5;

## Pig


**Credits to Prof. Rasin for Input Data**
