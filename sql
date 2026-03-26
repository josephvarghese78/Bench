select test_name, count(distinct thread_name) as users from performance  
group by test_name

select * from performance

select test_name, count(1) as samples from performance group by test_name

select max(datetime(end_time)),min(datetime(start_time)) from performance



SELECT test_name, SQRT(AVG(response_time * response_time) - AVG(response_time) * AVG(response_time)) AS stddev_pop FROM performance
group by test_name



WITH ordered AS (
    SELECT test_name, response_time,
           ROW_NUMBER() OVER (PARTITION BY test_name ORDER BY response_time) AS rn,
           COUNT(*) OVER (PARTITION BY test_name) AS cnt
    FROM performance
)
SELECT test_name,
       MIN(response_time) AS min_response_time,
       MAX(response_time) AS max_response_time,
       AVG(response_time) AS avg_response_time,
       (SELECT response_time FROM ordered o2 
        WHERE o2.test_name = o1.test_name AND rn = (cnt + 1)/2) AS median_response_time,
       (SELECT response_time FROM ordered o2 
        WHERE o2.test_name = o1.test_name AND rn = CAST(0.9 * cnt AS INT)) AS percentile_90,
       (SELECT response_time FROM ordered o2 
        WHERE o2.test_name = o1.test_name AND rn = CAST(0.95 * cnt AS INT)) AS percentile_95,
       (SELECT response_time FROM ordered o2 
        WHERE o2.test_name = o1.test_name AND rn = CAST(0.99 * cnt AS INT)) AS percentile_99
FROM ordered o1
GROUP BY test_name;



WITH ordered AS (
    SELECT suite_name, test_name, response_time, max_threads,
           ROW_NUMBER() OVER (PARTITION BY suite_name, test_name ORDER BY response_time) AS rn,
           COUNT(*) OVER (PARTITION BY suite_name, test_name) AS cnt
    FROM performance
), dusers as (select suite_name, test_name, count(distinct thread_name) as users from performance  
group by suite_name, test_name),
stddev as (SELECT suite_name, test_name, SQRT(AVG(response_time * response_time) - AVG(response_time) * AVG(response_time))/1000 AS stddev FROM performance
group by suite_name, test_name),
tpm as (select suite_name, test_name, 
((strftime('%s', max(datetime(end_time)))-strftime('%s',min(datetime(start_time))))/60) as ttime, count(1) as samples from performance
group by suite_name, test_name),
performance_metrics as (SELECT o1.suite_name, o1.test_name,u.users, o1.max_threads, t.samples, t.ttime as test_duration,
		t.samples/t.ttime as tpm,
       MIN(response_time)/1000 AS min_response_time,
       MAX(response_time)/1000 AS max_response_time,
       AVG(response_time)/1000 AS avg_response_time,
       s.stddev as std_dev,
       (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = (cnt + 1)/2)/1000 AS median_response_time,
        (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.1 * cnt AS INT))/1000 AS percentile_10,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.15 * cnt AS INT))/1000 AS percentile_15,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.2 * cnt AS INT))/1000 AS percentile_20,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.25 * cnt AS INT))/1000 AS percentile_25,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.3 * cnt AS INT))/1000 AS percentile_30,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.35 * cnt AS INT))/1000 AS percentile_35,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.4 * cnt AS INT))/1000 AS percentile_40,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.45 * cnt AS INT))/1000 AS percentile_45,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.5 * cnt AS INT))/1000 AS percentile_50,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.55 * cnt AS INT))/1000 AS percentile_55,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.6 * cnt AS INT))/1000 AS percentile_60,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.65 * cnt AS INT))/1000 AS percentile_65,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.7 * cnt AS INT))/1000 AS percentile_70,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.75 * cnt AS INT))/1000 AS percentile_75,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.8 * cnt AS INT))/1000 AS percentile_80,
                (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.85 * cnt AS INT))/1000 AS percentile_85,
        (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.9 * cnt AS INT))/1000 AS percentile_90,
       (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.95 * cnt AS INT))/1000 AS percentile_95,
       (SELECT response_time FROM ordered o2 
        WHERE o2.suite_name = o1.suite_name AND o2.test_name = o1.test_name AND rn = CAST(0.99 * cnt AS INT))/1000 AS percentile_99
FROM ordered o1, dusers u, stddev s, tpm t
where o1.suite_name =u.suite_name and o1.suite_name=s.suite_name and o1.suite_name= t.suite_name
and o1.test_name =u.test_name and o1.test_name=s.test_name and o1.test_name= t.test_name
GROUP BY o1.suite_name, o1.test_name, max_threads)
select * from performance_metrics



all

WITH ordered AS (
    SELECT response_time,
           ROW_NUMBER() OVER (ORDER BY response_time) AS rn,
           COUNT(*) OVER () AS cnt
    FROM performance
)
SELECT
    MIN(response_time) AS min_response_time,
    MAX(response_time) AS max_response_time,
    AVG(response_time) AS avg_response_time,
    (SELECT response_time FROM ordered WHERE rn = (cnt + 1)/2) AS median_response_time,
    (SELECT response_time FROM ordered WHERE rn = CAST(0.9 * cnt AS INT)) AS percentile_90,
    (SELECT response_time FROM ordered WHERE rn = CAST(0.95 * cnt AS INT)) AS percentile_95,
    (SELECT response_time FROM ordered WHERE rn = CAST(0.99 * cnt AS INT)) AS percentile_99
FROM performance;
