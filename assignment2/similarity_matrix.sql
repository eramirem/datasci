create view c as select * from frequency where docid='10080_txt_crude';
create view d as select * from frequency where docid='17035_txt_earn';
select sum(c.count*d.count) from c, d where c.term=d.term;