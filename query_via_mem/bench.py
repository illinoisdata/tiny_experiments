from pyspark.sql import SparkSession
import inspect
import os
import time


SPARK_DUMMY_DATA_FILE = 'mydata.csv'
SPARK_DIRECT_DATA_FILE = 'mydata_direct.csv'
SPARK_VIA_MEM_FILE = 'mydata_via_mem.csv'


def get_current_funcname() -> str:
    return inspect.stack()[1][3]


def test_spark_dummy_op():
    """
    Run only to make the future spark session creation faster.
    """
    spark = SparkSession.builder.getOrCreate()
    table_name = 'dummy_op'
    spark.read.csv(SPARK_DUMMY_DATA_FILE, sep=',', inferSchema=True, header=True) \
        .createOrReplaceTempView(table_name)
    res = spark.sql(f"select count(*) from {table_name} where colname0 like '%hello%'")
    res.show()


def test_spark_direct_from_file():
    print(f'[{get_current_funcname()}]')
    spark = SparkSession.builder.getOrCreate()
    table_name = 'file_direct'
    start_time = time.time()
    spark.read.csv(SPARK_DIRECT_DATA_FILE, sep=',', inferSchema=True, header=True) \
        .createOrReplaceTempView(table_name)
    res = spark.sql(f"select count(*) from {table_name} where colname0 like '%hello%'")
    res.show()
    elapsed_time = time.time() - start_time
    print(f'Elapsed Time: {elapsed_time} secs')
    print()
    print()


def test_spark_via_mem():
    print(f'[{get_current_funcname()}]')
    spark = SparkSession.builder.getOrCreate()
    table_name = 'via_mem'
    start_time = time.time()
    # copy to temp file
    in_mem_file = f'/mnt/ramdisk/{SPARK_VIA_MEM_FILE}'
    os.system(f'cp {SPARK_VIA_MEM_FILE} {in_mem_file}')
    elapsed_time = time.time() - start_time
    print(f'Copying file -> mem took {elapsed_time} secs')
    # spark processing
    spark.read.csv(in_mem_file, sep=',', inferSchema=True, header=True) \
        .createOrReplaceTempView(table_name)
    res = spark.sql(f"select count(*) from {table_name} where colname0 like '%hello%'")
    res.show()
    elapsed_time = time.time() - start_time
    print(f'Elapsed Time: {elapsed_time} secs')
    print()
    print()


def test_all():
    test_spark_dummy_op()
    test_spark_direct_from_file()
    test_spark_via_mem()


if __name__ == "__main__":
    test_all()
