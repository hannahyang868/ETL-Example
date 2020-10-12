lo_input = LOAD '/user/ec2-user/lineorder.tbl' USING PigStorage('|')
AS
(lo_orderkey:int,
lo_linenumber:int,
lo_custkey:int,
lo_partkey:int,
lo_suppkey:int,
lo_orderdate:int,
lo_orderpriority:chararray,
lo_shippriority:chararray,
lo_quantity:int,
lo_extendedprice:int,
lo_ordertotalprice:int,
lo_discount:int,
lo_revenue:int,
lo_supplycost:int,
lo_tax:int,
lo_commitdate:int,
lo_shipmode:chararray);

filter_res = FILTER lo_input BY lo_discount<3;
group_res = GROUP filter_res BY lo_quantity;
result = FOREACH group_res generate group as lo_quantity, SUM(filter_res.lo_revenue) as lo_revenue_sum;
DUMP result;
