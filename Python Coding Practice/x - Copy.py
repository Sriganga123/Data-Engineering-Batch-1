from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Simple PySpark Program") \
    .getOrCreate()

# Read data from a CSV file into a DataFrame
df = spark.read.csv("Example-1.csv", header=True, inferSchema=True)

# Show the DataFrame
print("Original DataFrame:")
df.show()

# Perform some basic data manipulation
# For example, let's filter the DataFrame to only include rows where the 'age' column is greater than 30
filtered_df = df.filter(df["age"] > 30)

# Show the filtered DataFrame
print("Filtered DataFrame (age > 30):")
filtered_df.show()

# Stop the SparkSession
spark.stop()
