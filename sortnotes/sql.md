https://www.linkedin.com/feed/update/urn:li:activity:7246853664441544704?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7246853664441544704%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/feed/update/urn:li:activity:7226821074863210496?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7226821074863210496%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/feed/update/urn:li:activity:7232286722280017920?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7232286722280017920%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/feed/update/urn:li:activity:7228648691316744192?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7228648691316744192%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/feed/update/urn:li:activity:7228077803739435008?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7228077803739435008%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/feed/update/urn:li:activity:7227941594962833409?updateEntityUrn=urn%3Ali%3Afs_updateV2%3A%28urn%3Ali%3Aactivity%3A7227941594962833409%2CFEED_DETAIL%2CEMPTY%2CDEFAULT%2Cfalse%29

https://www.linkedin.com/posts/oshein-vishwakarma_20-most-commonly-asked-interview-questions-activity-7226821874171674624-R1x_?utm_source=share&utm_medium=member_desktop

https://www.linkedin.com/posts/premmandal_interview-sql-activity-7247451685139165185-5KyA?utm_source=share&utm_medium=member_desktop

Sql query optimization technique:

  1. Indexing
  2. Use limit to fetch limited records(Limit Data Retrieval)
  3. Query Optimization
    - Use EXPLAIN to see how the database engine executes your queries
  4. De-normalization
  5. Use Stored Procedures
    -Move complex tasks to stored procedures. They improve performance by avoiding re-compilation for every execution.
  6. Partition Large Tables
  🔹 Break down large tables into smaller partitions.
  🔹 Ensure each partition is indexed for faster query performance.
  7. Leverage Temporary Tables
  🔹 Use temporary tables to store intermediate results, breaking down complex
  8. Avoid SELECT *
  9. Efficient Joins
  10. Use WHERE Instead of HAVING
  11. Use EXISTS Instead of IN
  12. Optimize Aggregations
  13. Avoid Using Functions on Indexed Columns
  14. Caching
  15. Parallel Execution
  16. Optimize Data Types
  17. Batch Processing
  https://medium.com/art-of-data-engineering/sql-query-optimization-tips-i-regret-not-knowing-earlier-a6de8323c04b



  SQL Query Optimization Tips I Regret Not Knowing Earlier


1. Indexing
Explanation:  Indexes act like a roadmap that helps the database find data faster. Without an index, the database must scan the entire table to locate the relevant rows.

2. Query Refactoring
Explanation: Complex queries can often be split into simpler, more manageable parts. This makes them easier to optimize and debug.

3. Avoid SELECT *
Explanation: Selecting all columns (SELECT *) can retrieve more data than necessary, slowing down the query. Specifying only the required columns reduces the workload on the database.

4. Efficient Joins
Explanation: The way tables are joined can significantly impact performance, especially with large datasets. The order of joins and the type of join used matter.

5. Use WHERE Instead of HAVING
Explanation: The “WHERE” clause filters rows before grouping them, while “HAVING” filters rows after grouping. Filtering early with “WHERE” is more efficient.

6. Limit Data Retrieval
Explanation: Fetching fewer rows or processing only a subset of the data can greatly improve query performance.

7. Use EXISTS Instead of IN
Explanation: “EXISTS” can be more efficient than “IN” when checking for the existence of rows in a subquery, especially when the subquery returns a large result set.

8. Optimize Aggregations
Explanation: Aggregating data (SUM, COUNT, etc.) can be slow, especially on large tables. Indexing the columns used in aggregations can speed up these operations.

9. Consider Query Execution Plans
Explanation: Execution plans show how the database intends to execute your query. Understanding this can help identify bottlenecks like full table scans.

10. Avoid Using Functions on Indexed Columns
Explanation: Applying a function to an indexed column in the “WHERE” clause can prevent the index from being used, leading to slower queries.

11. Caching
Explanation: Query caching can store the results of expensive queries, so they don’t have to be recalculated each time.

12. Use Temporary Tables
Explanation: Storing intermediate results in temporary tables can make complex queries more efficient, especially when those results are reused multiple times.

13. Parallel Execution
Explanation: Some databases support parallel execution, which splits the work across multiple CPU cores to process queries faster.

14. Optimize Data Types
Explanation: Using the most appropriate data types for your columns can save space and speed up queries.

15. Batch Processing
Explanation: When performing updates or deletes, processing them in batches instead of one at a time reduces transaction overhead.