Download spark-3.5.5-bin-hadoop3.tgz and move to host. Set the spark home and path variables accordingly.
Install pyspark using: $ pip3 install pyspark
Install cassandra driver using: $ pip3 install cassandra-driver
Run the script to unload the data of the table in CSV: $ python3 <script_name.py>
It will generate a folder with .csv naming convention. Go into the directory to get multipart CSVs.

Logs:
----------------------------------------------------------------------
|                  |            modules            ||   artifacts   |
|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
----------------------------------------------------------------------
|      default     |   16  |   16  |   16  |   0   ||   16  |   16  |
----------------------------------------------------------------------

:: retrieving :: org.apache.spark#spark-submit-parent-ccf1bfaa-b467-4944-ac8b-6e63352b3f83
	confs: [default]
	16 artifacts copied, 0 already retrieved (17388kB/31ms)
25/03/20 06:34:23 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
/home/automaton/.local/lib/python3.6/site-packages/pyspark/context.py:238: FutureWarning: Python 3.6 support is deprecated in Spark 3.2.
  FutureWarning

Output:
[spark-vikas:0] automaton@ip-10-166-84-60:~/primary_keys.csv$ ls
_SUCCESS                                                  part-00003-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00000-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv  part-00004-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00001-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv  part-00005-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
part-00002-7fd41794-83d5-435b-8032-13bcbafa70c8-c000.csv
