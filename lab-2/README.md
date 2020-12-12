# LAB 2 : Before starting Hadoop

## 1.2
To connect use SSH :
```console
cdrault> ssh tp2user@hadoop-edge01.efrei.online
```

Now i have to create my folder, create my file and write in it : 
```console
tp2user> mkdir corentin_drault
tp2user> cd corentin_drault
tp2user> vi bonjour.txt
```
At this point, i can write all i want in the file bonjour.txt, for this example i gonna write "Hello world!". I used `esc` and the shortcut `:wq` to save and quit.

I can show the content of my file 'bonjour.txt' by using the command `cat bonjour.txt`.

```console
tp2user> cat bonjour.txt
Hello worl!
```

## 1.3.1

I need tobe connect to Kerberos. For that, i need to use the `tp2user.keypass` who is at the root of the user.

```console
tp2user> kinit ambari-qa-efrei@EFREI.ONLINE -k -t ../tp2user.keytab
```

No output, i am connect to the Kerberos account well.

## 1.3.2
```console
tp2user> hdfs dfs -put bonjour.txt corentin_drault
tp2user> hdfs dfs -ls -R
display all the file system and we can show bonjour.txt in corentin_drault

tp2user> hdfs dfs -cat corentin_drault/bonjour.txt
Hello world!

tp2user> hdfs dfs -tail corentin_drault/bonjour.txt
Hello world!

tp2user> hdfs dfs -rm corentin_drault/bonjour.txt
20/10/15 16:50:23 INFO fs.TrashPolicyDefault: Moved: 'hdfs://efrei/user/ambari-qa/corentin_drault/bonjour.txt' to trash at: hdfs://efrei/user/ambari-qa/.Trash/Current/user/ambari-qa/corentin_drault/bonjour.txt1602773423706

tp2user> hdfs dfs -copyFromLocal bonjour.txt corentin_drault
tp2user> hdfs dfs -ls -R
display all the file system and we can show bonjour.txt in corentin_drault

tp2user> hdfs dfs -chmod go+w bonjour.txt
tp2user> hdfs dfs -ls corentin_drault
-rw-r--r--   3 ambari-qa hdfs         13 2020-10-15 16:55 corentin_drault/bonjour.txt

tp2user> hdfs dfs -chmod go-r corentin_drault/bonjour.txt
tp2user> hdfs dfs -ls corentin_drault
-rw--w--w-   3 ambari-qa hdfs         13 2020-10-15 16:55 corentin_drault/bonjour.txt

tp2user> hdfs dfs -get corentin_drault/bonjour.txt demat.txt
```

## 1.3.3

```console
tp2user> wget http://www.gutenberg.org/files/1342/1342-0.txt 
--2020-10-15 17:18:40--  http://www.gutenberg.org/files/1342/1342-0.txt
Résolution de www.gutenberg.org (www.gutenberg.org)... 152.19.134.47, 2610:28:3090:3000:0:bad:cafe:47
Connexion vers www.gutenberg.org (www.gutenberg.org)|152.19.134.47|:80...connecté.
requête HTTP transmise, en attente de la réponse...200 OK
Longueur: 799738 (781K) [text/plain]
Sauvegarde en : «1342-0.txt»

100%[==============================================================================================================>] 799 738      452KB/s   ds 1,7s   

2020-10-15 17:18:41 (452 KB/s) - «1342-0.txt» sauvegardé [799738/799738]

tp2user> hdfs dfs -mkdir corentin_drault/raw

tp2user> hdfs dfs -put 1342-0.txt corentin_drault/raw

tp2user> hdfs dfs -cp corentin_drault/raw/1342-0.txt corentin_drault/input.txt

tp2user> hdfs dfs -cat corentin_drault/input.txt

tp2user> hdfs dfs -rm corentin_drault/input.txt

tp2user> hdfs dfs -ls -R corentin_drault

tp2user> hdfs dfs -get corentin_drault/raw/1342-0.txt local.txt 


```
