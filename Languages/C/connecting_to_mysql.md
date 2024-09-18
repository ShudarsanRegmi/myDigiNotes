```
 gcc -I"C:/Program Files/MySQL/MySQL Server 8.0/include" -L"C:/Program Files/MySQL/MySQL Server 8.0/lib" -o out.exe main.c -lmysql
```

### Connection Code

```c
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>


/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char  *argv[]) {
 
 printf("Hello, World\n");
 MYSQL *mysql = NULL;
 
 if (mysql_library_init(argc, argv, NULL)) {
  fprintf(stderr, "could not MYSQL client library");
  exit(1);
 }
// 
 mysql = mysql_init(mysql);
// 
 if (!mysql) {
  printf("Initialization failed....");
  return EXIT_FAILURE;
 }
 
 if (!mysql_real_connect(
       mysql,
       "localhost",
       "shudarsan",
       "shudarsan@localhost",
       "testdb",
       0,
       NULL,
       0
 )) {
  printf("Failed to connect to the database\n");
 }else {
  printf("Connection to the database was successful\n");
 }
  
 mysql_close(mysql);
 mysql_library_end();
 
 return EXIT_SUCCESS;
 
 return 0;
}

```

### Connection and insertion

```C
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>


/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char  *argv[]) {
 
 printf("Hello, World\n");
 MYSQL *mysql = NULL;
 
 if (mysql_library_init(argc, argv, NULL)) {
  fprintf(stderr, "could not MYSQL client library");
  exit(1);
 }
// 
 mysql = mysql_init(mysql);
// 
 if (!mysql) {
  printf("Initialization failed....");
  return EXIT_FAILURE;
 }
 
 if (!mysql_real_connect(
       mysql,
       "localhost",
       "shudarsan",
       "shudarsan@localhost",
       "testdb",
       0,
       NULL,
       0
 )) {
  printf("Failed to connect to the database\n");
 }else {
  printf("Connection to the database was successful\n");
 }
 
 printf("Choose 1 of the options below: \n 1) Create user \n Otherwise) Exit \n Enter your choice: ");
 
 int c;
 scanf("%d",&c);
 
 if (c!=1) {
  return 0;
 }
 
 
 if(mysql_query(mysql, "insert into users values ('hari','ram',50)")) {
  printf("Insertion was successful");
 }else{
  printf("Failed to insert data");
 }
 
 
 
 mysql_close(mysql);
 mysql_library_end();
 
 return EXIT_SUCCESS;
 
 return 0;
}
```
