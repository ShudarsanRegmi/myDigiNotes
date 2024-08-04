# Different ways to connect to mysql database from C++
Connecting to MySQL from C++ can be achieved through various methods, each with its own advantages and community trends. Here are some of the common ways:

### 1. MySQL Connector/C++

**Description:**
MySQL Connector/C++ is an official MySQL driver that provides a C++ interface for connecting to MySQL databases. It offers a modern, object-oriented API as well as a legacy API for compatibility with older codebases.

**Features:**
- Modern C++11/14 support.
- Object-oriented interface.
- Supports both synchronous and asynchronous operations.
- Full support for MySQL features such as transactions, stored procedures, and prepared statements.

**Usage:**
```cpp
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/statement.h>
#include <cppconn/resultset.h>

sql::mysql::MySQL_Driver *driver;
sql::Connection *con;
sql::Statement *stmt;
sql::ResultSet *res;

driver = sql::mysql::get_mysql_driver_instance();
con = driver->connect("tcp://127.0.0.1:3306", "user", "password");
con->setSchema("test");

stmt = con->createStatement();
res = stmt->executeQuery("SELECT 'Hello World!' AS _message");
while (res->next()) {
    std::cout << res->getString("_message") << std::endl;
}
delete res;
delete stmt;
delete con;
```

### 2. MySQL C API (libmysqlclient)

**Description:**
The MySQL C API is a low-level interface provided by MySQL for C programs. It can also be used in C++ applications, offering a more granular control over the database operations.

**Features:**
- Direct access to MySQL functionality.
- Fine-grained control over database operations.
- Lightweight and fast.

**Usage:**
```cpp
#include <mysql/mysql.h>

MYSQL *conn;
MYSQL_RES *res;
MYSQL_ROW row;

conn = mysql_init(NULL);
mysql_real_connect(conn, "localhost", "user", "password", "database", 0, NULL, 0);

mysql_query(conn, "SELECT 'Hello World!' AS _message");
res = mysql_store_result(conn);

while ((row = mysql_fetch_row(res))) {
    printf("%s\n", row[0]);
}

mysql_free_result(res);
mysql_close(conn);
```

### 3. ODBC (Open Database Connectivity)

**Description:**
ODBC is a standard API for accessing database management systems. Using ODBC, applications can connect to MySQL through an ODBC driver.

**Features:**
- Database agnostic.
- Standardized API.
- Can connect to multiple database systems using the same codebase.

**Usage:**
```cpp
#include <sql.h>
#include <sqlext.h>

SQLHENV henv;
SQLHDBC hdbc;
SQLHSTMT hstmt;
SQLRETURN ret;
SQLCHAR outstr[1024];
SQLSMALLINT outstrlen;

SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);
SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (void *)SQL_OV_ODBC3, 0);
SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);

SQLDriverConnect(hdbc, NULL, (SQLCHAR*)"DSN=MySQL;UID=user;PWD=password;", SQL_NTS,
                 outstr, sizeof(outstr), &outstrlen, SQL_DRIVER_COMPLETE);

SQLAllocHandle(SQL_HANDLE_STMT, hdbc, &hstmt);
SQLExecDirect(hstmt, (SQLCHAR*)"SELECT 'Hello World!' AS _message", SQL_NTS);

while ((ret = SQLFetch(hstmt)) != SQL_NO_DATA) {
    SQLGetData(hstmt, 1, SQL_C_CHAR, outstr, sizeof(outstr), &outstrlen);
    printf("%s\n", outstr);
}

SQLFreeHandle(SQL_HANDLE_STMT, hstmt);
SQLDisconnect(hdbc);
SQLFreeHandle(SQL_HANDLE_DBC, hdbc);
SQLFreeHandle(SQL_HANDLE_ENV, henv);
```

### Community Trends and Preferred Methods

1. **MySQL Connector/C++:** This is the most preferred method for modern C++ applications due to its object-oriented design, ease of use, and full feature support. It's actively maintained by MySQL, ensuring compatibility with the latest MySQL versions and features.

2. **MySQL C API (libmysqlclient):** This method is preferred for applications that require high performance and fine-grained control over MySQL operations. It is also suitable for legacy systems and applications with minimal dependencies.

3. **ODBC:** This method is preferred for applications that need to support multiple database systems or require a standardized API for database connectivity. It's also a good choice for environments where database changes are frequent.

### Conclusion

For most modern C++ applications, **MySQL Connector/C++** is the preferred choice due to its ease of use and feature set. However, for performance-critical applications or those requiring low-level control, the **MySQL C API** is a solid choice. **ODBC** remains a versatile option for applications needing database-agnostic connectivity.
