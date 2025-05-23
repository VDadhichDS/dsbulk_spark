from pyspark.sql import SparkSession
# Create a Spark session with Cassandra configuration
spark = SparkSession.builder \
    .appName("CassandraDataLoader") \
    .config("spark.cassandra.connection.host", "<hostname>") \
    .config("spark.cassandra.connection.port", "<port>") \
    .config('spark.jars.packages', 'com.datastax.spark:spark-cassandra-connector_2.12:3.5.1') \
    .config('spark.sql.extensions', 'com.datastax.spark.connector.CassandraSparkExtensions') \
    .getOrCreate()

# You can then load data from Cassandra as shown below:
source_data = spark.read \
    .format("org.apache.spark.sql.cassandra") \
    .options(keyspace="<keyspace_name>", table="<table_name>") \
    .load()

# Example of selecting specific columns, In this example I created below table in cassandra
# CREATE TABLE customer (
#    num text,
#    uuid text,
#    document blob,
#    PRIMARY KEY (num, uuid)
#    ) 
from pyspark.sql.functions import col
rearranged_data = source_data.select(
    col("num"),
    col("uuid")
)

# Save to a CSV file
rearranged_data.write \
    .option("header", "true") \
    .csv("primary_keys.csv")
#Below line help you to get small data in one CSV please don't use if data size is large 
#rearranged_data.coalesce(1).write.option("header", "true").csv("test_primary_keys.csv")
# Stop the Spark session
spark.stop()
