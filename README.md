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

ADD FILE /home/ec2-user/hive_udf.py;
INSERT OVERWRITE TABLE customer_new
SELECT TRANSFORM (c_custkey,c_name,c_address,c_city,c_nation,c_region,c_phone,c_mktsegment) USING 'python hive_udf.py'
AS (c_custkey,c_address,c_city)
FROM customer;

**Step 4: Check Result on Hive CLI**

Select * from customer_new limit 5;

## Pig

This example shows how to perform querying using Pig Script. The query is shown below:

SELECT lo_quantity, SUM(lo_revenue)

FROM lineorder

WHERE lo_discount < 3

GROUP BY lo_quantity;

**Step 1: Write pig script (Codes provided)**

**Step 2: Run Command on Grunt**

bin/pig -f pig_script.pig

## Hadoop Streaming

This example shows how to run Hadoop Streaming performing the following query:

SELECT lo_quantity, SUM(lo_revenue)

FROM lineorder

WHERE lo_discount BETWEEN 3 AND 5

GROUP BY lo_quantity;

**Step 1: Write Mapper and Reducer File (Codes provided)**

**Step 2: Run Hadoop Streaming Command on Hadoop CLI**

hadoop jar hadoop-streaming-2.6.4.jar -input /user/ec2-user/lineorder.tbl -output /data/output -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

**Step 3: Check Results on Hadoop CLI**

hadoop fs -ls /data/output

Hadoop fs -cat /data/output/part-00000

**Credits to Prof. Rasin for Input Data**
