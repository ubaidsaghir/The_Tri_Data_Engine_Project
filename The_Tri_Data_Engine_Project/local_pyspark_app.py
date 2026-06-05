from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col, trim, to_date, avg, sum as spark_sum, count, round as spark_round


spark = SparkSession.builder \
    .appName("Tri Data Engine - Local PySpark") \
    .getOrCreate()

file_path = "orders.csv"

schema = StructType([
    StructField("OrderID", StringType(), True),
    StructField("CustomerID", StringType(), True),
    StructField("ItemName", StringType(), True),
    StructField("Quantity", StringType(), True),
    StructField("Price", StringType(), True),
    StructField("Date", StringType(), True),
    StructField("Status", StringType(), True)
])

try:
    orders_df = spark.read.option("header", "true").schema(schema).csv(file_path)
    print("CSV file loaded successfully.")

except Exception as e:
    print("File loading failed.")
    print(e)
    spark.stop()
    exit()


cleaned_df = orders_df \
    .withColumn("OrderID", col("OrderID").cast("int")) \
    .withColumn("CustomerID", col("CustomerID").cast("int")) \
    .withColumn("Quantity", col("Quantity").cast("int")) \
    .withColumn("Price", col("Price").cast("double")) \
    .withColumn("Date", to_date(col("Date"), "yyyy-MM-dd")) \
    .withColumn("ItemName", trim(col("ItemName"))) \
    .withColumn("Status", trim(col("Status")))

cleaned_df = cleaned_df.fillna({
    "ItemName": "Unknown Item",
    "Status": "Unknown",
    "OrderID": 0,
    "CustomerID": 0,
    "Quantity": 0,
    "Price": 0.0
})

print("Cleaned Data Preview:")
cleaned_df.show(10)

cleaned_df.createOrReplaceTempView("staging_orders_local")

summary_df = cleaned_df.select(
    count("*").alias("Total_Orders"),
    spark_round(spark_sum(col("Price") * col("Quantity")), 2).alias("Total_Revenue"),
    spark_round(avg(col("Price") * col("Quantity")), 2).alias("Average_Order_Value")
)

print("Executive Summary:")
summary_df.show()


customer_spend_df = cleaned_df.groupBy("CustomerID") \
    .agg(
        spark_round(spark_sum(col("Price") * col("Quantity")), 2).alias("Total_Spend")
    ).orderBy(col("Total_Spend").desc())

print("Customer Spend:")
customer_spend_df.show(10)

validation_df = spark.sql("""
    SELECT 
        ROUND(AVG(Price * Quantity), 2) AS avg_order_value
    FROM staging_orders_local
""")

print("Local PySpark Average Order Value:")
validation_df.show()

spark.stop()