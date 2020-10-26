# YARN MapReduce2
## 1. Yarn
### 1.2 Wordcount example
- Connect to Hadoop Cluster
```console
cdrault> ssh cdrault@hadoop-edge01.efrei.online
[cdrault@hadoop-edge01 ~] kinit cdrault@EFREI.ONLINE
```

- From the SSH session, use the following command to list the samples:
```console
[cdrault@hadoop-edge01 ~]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar 

An example program must be given as the first argument.
Valid program names are:
  aggregatewordcount: An Aggregate based map/reduce program that counts the words in the input files.
  aggregatewordhist: An Aggregate based map/reduce program that computes the histogram of the words in the input files.
  bbp: A map/reduce program that uses Bailey-Borwein-Plouffe to compute exact digits of Pi.
  dbcount: An example job that count the pageview counts from a database.
  distbbp: A map/reduce program that uses a BBP-type formula to compute exact bits of Pi.
  grep: A map/reduce program that counts the matches of a regex in the input.
  join: A job that effects a join over sorted, equally partitioned datasets
  multifilewc: A job that counts words from several files.
  pentomino: A map/reduce tile laying program to find solutions to pentomino problems.
  pi: A map/reduce program that estimates Pi using a quasi-Monte Carlo method.
  randomtextwriter: A map/reduce program that writes 10GB of random textual data per node.
  randomwriter: A map/reduce program that writes 10GB of random data per node.
  secondarysort: An example defining a secondary sort to the reduce.
  sort: A map/reduce program that sorts the data written by the random writer.
  sudoku: A sudoku solver.
  teragen: Generate data for the terasort
  terasort: Run the terasort
  teravalidate: Checking results of terasort
  wordcount: A map/reduce program that counts the words in the input files.
  wordmean: A map/reduce program that counts the average length of the words in the input files.
  wordmedian: A map/reduce program that counts the median length of the words in the input files.
  wordstandarddeviation: A map/reduce program that counts the standard deviation of the length of the words in the input files.
```

- Use the following command to get help on a specic sample. In this case, the wordcount sample:

```console
[cdrault@hadoop-edge01 ~]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar wordcount
Usage: wordcount <in> [<in>...] <out>
```

- Wordcount for DaVinci.txt

```console
[cdrault@hadoop-edge01 ~]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar wordcount /user/cdrault/davinci.txt /user/cdrault/wordcount
```

### 1.3 - Sudoku
```console
[cdrault@hadoop-edge01 lab-3]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar sudoku sudoku.dta 
Solving sudoku.dta
8 5 1 3 9 2 6 4 7 
4 3 2 6 7 8 1 9 5 
7 9 6 5 1 4 3 8 2 
6 1 4 8 2 3 7 5 9 
5 7 8 9 6 1 4 2 3 
3 2 9 4 5 7 8 1 6 
9 4 7 2 8 6 5 3 1 
1 8 5 7 3 9 2 6 4 
2 6 3 1 4 5 9 7 8 

Found 1 solutions
```

### 1.4 - Pi Example

```console
[cdrault@hadoop-edge01 lab-03]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar pi 16 10000000
...
Job Finished in 26.056 seconds
Estimated value of Pi is 3.14159155000000000000
```

### 1.5 - 10GB
- Generate Data 
```console
[cdrault@hadoop-edge01 lab-03]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar teragen -Dmapred.map.tasks=50 100000000 /user/cdrault/data/10GB-sort-input
```

- Sort data :
```console
[cdrault@hadoop-edge01 lab-03]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar terasort -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=25 /user/cdrault/data/10GB-sort-input /user/cdrault/data/10GB-sort-output
...
20/10/26 17:32:39 INFO terasort.TeraSort: done
```

- Validate data :
```console
[cdrault@hadoop-edge01 lab-03]$ yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar teravalidate -Dmapred.map.tasks=50 -Dmapred.reduce.tasks=25 /user/cdrault/data/10GB-sort-output /user/cdrault/data/10GB-sort-validate
```

- Results :
```console
[cdrault@hadoop-edge01 lab-03]$ hdfs dfs -ls /user/cdrault/data/
Found 3 items
drwxr-xr-x   - cdrault cdrault          0 2020-10-26 17:24 /user/cdrault/data/10GB-sort-input
drwxr-xr-x   - cdrault cdrault          0 2020-10-26 17:32 /user/cdrault/data/10GB-sort-output
drwxr-xr-x   - cdrault cdrault          0 2020-10-26 17:34 /user/cdrault/data/10GB-sort-validate
```

## 2. MapReduce2
TODO