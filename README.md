# ETL-Example
Describing some ETL processes on Hadoop using Hive, Pig and Hadoop Streaming

Input data are as follows:

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/dwdate.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/lineorder.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/part.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/supplier.tbl

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/customer.tbl

#### Hive

This examples shows a ETL process on Hive to transform data and put into new table with selected columns (c_custkey, c_address, c_city). For the c_address column, shorten it to 6 characters (i.e., if the value is longer, remove extra characters, but otherwise keep it as-is). For c_city, add a space and a # to indicate the digit at the end (e.g., UNITED KI2 => UNITED KI #2, or INDONESIA4 => INDONESIA #4).

**Step 1: create all relevant tables and load data on Hive CLI.**

create table part (
p_partkey int,
p_name varchar(22),
p_mfgr varchar(6),
p_category varchar(7),
p_brand1 varchar(9),
p_color varchar(11),
p_type varchar(25),
p_size int,
p_container varchar(10))
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '|' STORED AS TEXTFILE;
create table supplier (
s_suppkey int,
s_name varchar(25),
s_address varchar(25),
s_city varchar(10),
s_nation varchar(15),
s_region varchar(12),
s_phone varchar(15))
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '|' STORED AS TEXTFILE;
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
create table dwdate (
d_datekey int,
d_date varchar(19),
d_dayofweek varchar(10),
d_month varchar(10),
d_year int,
d_yearmonthnum int,
d_yearmonth varchar(8),
d_daynuminweek int,
d_daynuminmonth int,
d_daynuminyear int,
d_monthnuminyear int,
d_weeknuminyear int,
d_sellingseason varchar(13),
d_lastdayinweekfl varchar(1),
d_lastdayinmonthfl varchar(1),
d_holidayfl varchar(1),
d_weekdayfl varchar(1))
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '|' STORED AS TEXTFILE;
create table lineorder (
lo_orderkey int,
lo_linenumber int,
lo_custkey int,
lo_partkey int,
lo_suppkey int,
lo_orderdate int,
lo_orderpriority varchar(15),
lo_shippriority varchar(1),
lo_quantity int,
lo_extendedprice int,
lo_ordertotalprice int,
lo_discount int,
lo_revenue int,
lo_supplycost int,
lo_tax int,
lo_commitdate int,
lo_shipmode varchar(10))
ROW FORMAT DELIMITED FIELDS
TERMINATED BY '|' STORED AS TEXTFILE;
LOAD DATA LOCAL INPATH '/home/ec2-user/part.tbl' OVERWRITE INTO TABLE part;
LOAD DATA LOCAL INPATH '/home/ec2-user/supplier.tbl' OVERWRITE INTO TABLE supplier;
LOAD DATA LOCAL INPATH '/home/ec2-user/customer.tbl' OVERWRITE INTO TABLE customer;
LOAD DATA LOCAL INPATH '/home/ec2-user/dwdate.tbl' OVERWRITE INTO TABLE dwdate;
LOAD DATA LOCAL INPATH '/home/ec2-user/lineorder.tbl' OVERWRITE INTO TABLE lineorder;

**Credits to Prof. Rasin for Input Data**
