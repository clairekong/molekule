from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, when, lit
from pyspark.sql.types import BooleanType, StringType, DateType, StructType, StructField, DoubleType, IntegerType, FloatType, DecimalType
from tamicloudvars import COVID_S3
from tamicloudvars import TAMIDB
from tamicloudvars import COVIDT
from pyspark import SparkContext
import datetime

spark = SparkSession.builder.appName('tami_v2').enableHiveSupport().getOrCreate()

from pyspark.sql import SQLContext
sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

'''
COVID_SCHEMA = StructType([ \
  StructField("country", StringType(), False), \
  StructField("province", StringType(), False), \
  StructField("confirmed", IntegerType(), False), \
  StructField("recovered", IntegerType(), False), \
  StructField("death", IntegerType(), False), \
  StructField("active", IntegerType(), False), \
  StructField("latitude", DecimalType(12,9), False), \
  StructField("longitude", DecimalType(12,9), False), \
  StructField("date", DateType(), False)])
'''

covid = sqlContext.read.format('com.databricks.spark.csv').options(header='true', delimiter='\u0001').load(COVID_S3)
covid = covid.select("date", "country", "province", "confirmed", "recovered", "deaths")

def convert_date(date):
    mm, dd, yyyy = date.split("/")
    thedate = datetime.date(int(yyyy), int(mm), int(dd))
    return thedate

udf_convert_date = udf(convert_date, DateType())

covid = covid.withColumn("date", udf_convert_date(col("date")))

covid = covid.withColumn('recovered', col('recovered').cast(IntegerType())).withColumn('deaths', col('deaths').cast(IntegerType())).withColumn('date', col('date').cast(DateType())).withColumn('confirmed', col('confirmed').cast(IntegerType()))

covid.show(100)
covid.printSchema()

covid.write.saveAsTable("{}.{}".format(TAMIDB,COVIDT), mode="overwrite")