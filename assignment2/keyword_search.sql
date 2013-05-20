create view q as 
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION 
SELECT 'q' as docid, 'taxes' as term, 1 as count 
UNION
SELECT 'q' as docid, 'treasury' as term, 1 as count;

select frequency.docid, sum(frequency.count*q.count) as score from frequency, q where frequency.term = q.term group by frequency.docid order by score asc;