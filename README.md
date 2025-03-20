Here's a sample README file for your GitHub project based on the details you provided:

---

# Spark Data Unloading to CSV

This repository provides a script to unload data from a Cassandra table into CSV format using Apache Spark. The script uses PySpark to retrieve data and save it into multiple CSV files.

## Prerequisites

Before running the script, ensure that the following dependencies are installed and configured:

### 1. Apache Spark
- Download the Spark 3.5.5 binary for Hadoop 3:
  - Download: [spark-3.5.5-bin-hadoop3.tgz](https://spark.apache.org/downloads.html)
- Move the downloaded file to your host and set the `SPARK_HOME` and `PATH` variables accordingly. Example:
  ```bash
  export SPARK_HOME=/path/to/spark-3.5.5-bin-hadoop3
  export PATH=$SPARK_HOME/bin:$PATH
  ```

### 2. Install PySpark
Install PySpark using pip:
```bash
pip3 install pyspark
```

### 3. Install Cassandra Driver
Install the Cassandra driver for Python:
```bash
pip3 install cassandra-driver
```

## Usage

### Step 1: Script Execution
Once the dependencies are installed, run the script using the following command:

```bash
python3 <script_name.py>
```

This will trigger the data unloading process from the Cassandra table to CSV files.

### Step 2: Output Directory
The script will generate a folder with CSV files. The CSV files will follow the naming convention `part-00000-<UUID>-c000.csv`, and so on.

Example directory listing:
```bash
$ ls
_SUCCESS
part-00000-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00001-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00002-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00003-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00004-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00005-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
```

### Step 3: Retrieving Logs
The Spark logs will provide useful information about the process. You can view the logs during or after the execution. Example logs:
```
---------------------------------------------------------------------
|                  |            modules            ||   artifacts   |
|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
---------------------------------------------------------------------
|      default     |   16  |   16  |   16  |   0   ||   16  |   16  |
---------------------------------------------------------------------
:: retrieving :: org.apache.spark#spark-submit-parent-ccf1bfaa-b467-4944-ac8b-6e63352b3f83
confs: [default]
16 artifacts copied, 0 already retrieved (17388kB/31ms)
25/03/20 06:34:23 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
/home/automaton/.local/lib/python3.6/site-packages/pyspark/context.py:238: FutureWarning: Python 3.6 support is deprecated in Spark 3.2.
  FutureWarning
```

### Code explanation

Import SparkSession: The first step is to import the SparkSession class, which is used to initialize and manage Spark operations.
Create Spark Session: The SparkSession is configured to connect to Cassandra using specific configurations like host, port, and necessary packages.
Reading from Cassandra: The script reads data from the specified Cassandra keyspace and table.
Selecting Columns: It selects only the num and uuid columns from the retrieved data using the col() function.
Save to CSV: It writes the selected data into a CSV file, with the option to include headers.
Optional Coalescing: The commented-out code would combine all the output into a single CSV file, useful for smaller datasets.
Stop Spark Session: The session is stopped to free up resources after the operation completes.
Notes:
Ensure you replace <hostname>, <port>, <keyspace_name>, and <table_name> with actual values for your Cassandra setup.
The .coalesce(1) option should be used with caution, as it can cause performance issues with large datasets by trying to combine everything into one file.

## Troubleshooting

- **WARN NativeCodeLoader**: This warning can typically be ignored unless you're facing issues related to native Hadoop libraries.
- **Python 3.6 support deprecated**: The script runs on Python 3.6, but it will be deprecated in future Spark releases. It's recommended to upgrade to Python 3.7+ if possible.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the placeholders (like `<script_name.py>`) and any details specific to your project!
