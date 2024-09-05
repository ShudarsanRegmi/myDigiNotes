# Learning Path for MySql C API

- [Chapter 0](https://dev.mysql.com/doc/c-api/8.0/en/)
- [Overview of Basic C API: Very Important Material for getting started working with C API Client Library](https://dev.mysql.com/doc/c-api/8.0/en/c-api-basic-interface-usage.html)


## Important Links
- [MySQL C API function reference](https://dev.mysql.com/doc/c-api/8.0/en/c-api-function-reference.html)
- [C API Basic Data Structures](https://dev.mysql.com/doc/c-api/8.0/en/c-api-data-structures.html)
- [C API Prepared Statements Data Structures](https://dev.mysql.com/doc/c-api/8.0/en/c-api-prepared-statement-data-structures.html)
- 

## Most Important Data structure for creating a connection object

-MYSQL

This structure represents the handler for one database connection. It is used for almost all MySQL functions. Do not try to make a copy of a MYSQL structure. There is no guarantee that such a copy will be usable.

## Guides for Building C API Clients Program
 - [Building Guide for both Linux and Windows](https://dev.mysql.com/doc/c-api/8.0/en/c-api-building-clients.html)






--- 

# Notes

## Important Points
- The C API provides low-level access to the MySQL client/server protocol and enables C programs to access database contents. The C API code is distributed with MySQL and implemented in the libmysqlclient library.


## Important Points from Chapter 2
- The MySQL C API is a C-based API that client applications written in C can use to communicate with MySQL Server. Client programs refer to C API header files at compile time and link to a C API library file, libmysqlclient, at link time.
- On Unix (and Unix-like) systems, the static library is libmysqlclient.a. The dynamic library is libmysqlclient.so on most Unix systems and libmysqlclient.dylib on macOS.
- On Windows, the static library is mysqlclient.lib and the dynamic library is libmysql.dll. Windows distributions also include libmysql.lib, a static import library needed for using the dynamic library.



## Important functions signature

```C
MYSQL *
mysql_connect(MYSQL *mysql,
              const char *host,
              const char *user,
              const char *passwd)
```


## Snippets picked from mysql offcial docs.

```C
MYSQL mysql;

mysql_init(&mysql);
mysql_options(&mysql,MYSQL_READ_DEFAULT_GROUP,"your_prog_name");
if (!mysql_real_connect(&mysql,"host","user","passwd","database",0,NULL,0))
{
    fprintf(stderr, "Failed to connect to database: Error: %s\n",
          mysql_error(&mysql));
}
```

```C
MYSQL mysql;

mysql_init(&mysql);
mysql_options(&mysql,MYSQL_READ_DEFAULT_GROUP,"your_prog_name");
if (!mysql_real_connect(&mysql,"host","user","passwd","database",0,NULL,0))
{
    fprintf(stderr, "Failed to connect to database: Error: %s\n",
          mysql_error(&mysql));
}
```


