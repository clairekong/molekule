use tami_dev;
set hive.execution.engine=tez;

DROP TABLE IF EXISTS covid_table;

CREATE EXTERNAL TABLE covid_table (
    thedate  date,
    country  string,
    province  string,
    confirmed  int,
    recovered  int,
    deaths  int
    )

ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0001'
STORED AS TEXTFILE
LOCATION 's3://data-labs/databases/tami_dev/covid_table'
;
