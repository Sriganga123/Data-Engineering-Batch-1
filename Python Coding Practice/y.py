#1) creating RDD from Seq or List (using Parallelize)

# import SparkSession
from pyspark.sql import SparkSession
# Create SparkSession
spark = SparkSession.builder.appName("practice").getOrCreate()
# define data
dataList=[("Java",20000),("Python",10000),("Scala",30000)]
#using parallelize
rdd=spark.sparkContext.parallelize(dataList)
# To print the data
rdd.collect()