# Connecting to mysql database from CPP using connectors

Debian package.  Debian packages are available for Linux (as of Connector/C++ 8.0.14). The packages are distinguished by their base names (the full names include the Connector/C++ version and suffixes):

Debian package.  Debian packages are available for Linux (as of Connector/C++ 8.0.14). The packages are distinguished by their base names (the full names include the Connector/C++ version and suffixes):

libmysqlcppconn8-1: This package provides the shared connector library implementing X DevAPI and X DevAPI for C.

libmysqlcppconn7: This package provides the shared legacy connector library implementing the JDBC API.

libmysqlcppconn-dev: This package installs development files required for building applications that use Connector/C++ libraries provided by the other packages, and static connector libraries. This package depends on the shared libraries provided by the other packages. It cannot be installed by itself without the other two packages.
```bash
sudo apt install libmysqlcppconn-dev
```
Go through the boooring sign up process to download these drivers
### Download Connector Drivers for cpp from here
[Download connector drivers](https://dev.mysql.com/downloads/connector/cpp/)
[Download directly from here](https://dev.mysql.com/get/Downloads/Connector-C++/mysql-connector-c++-9.0.0-linux-glibc2.28-x86-64bit.tar.gz)

```bash
sudo cp -r /home/user/mysql-connector/include/* /usr/local/include/
sudo cp -r /home/user/mysql-connector/lib64/* /usr/local/lib/
sudo ldconfig
g++ -I/usr/local/include/jdbc -L/usr/local/lib simple_connection.cpp -lmysqlcppconn -o simple_connection
```
```cmake
CC = g++
CFLAGS = -I/usr/local/include/jdbc
LDFLAGS = -L/usr/local/lib
LIBS = -lmysqlcppconn

# Target executable
TARGET = simple_connection

# Source file
SRC = simple_connection.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(LDFLAGS) $(SRC) $(LIBS) -o $(TARGET)

clean:
	rm -f $(TARGET)

```

```cpp
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/statement.h>
#include <cppconn/resultset.h>
#include <iostream>
#include <iomanip> // For setw

int main() {
    sql::mysql::MySQL_Driver *driver;
    sql::Connection *con;
    sql::Statement *stmt;
    sql::ResultSet *res;

    try {
        // Establish connection to MySQL server
        driver = sql::mysql::get_mysql_driver_instance();
        con = driver->connect("tcp://127.0.0.1:3306", "shudarsan", "shudarsan@localhost");
        con->setSchema("hackerrank");

        // Create SQL statement
        stmt = con->createStatement();
        res = stmt->executeQuery("SELECT * FROM STATION");

        // Print column names
        sql::ResultSetMetaData *metaData = res->getMetaData();
        int numColumns = metaData->getColumnCount();
        std::cout << "Fetching all columns from STATION table:" << std::endl;
        for (int i = 1; i <= numColumns; ++i) {
            std::cout << std::setw(15) << metaData->getColumnName(i) << " | ";
        }
        std::cout << std::endl;

        // Iterate through the result set
        while (res->next()) {
            for (int i = 1; i <= numColumns; ++i) {
                std::cout << std::setw(15) << res->getString(i) << " | ";
            }
            std::cout << std::endl;
        }

        // Clean up
        delete res;
        delete stmt;
        delete con;
    } catch (sql::SQLException &e) {
        std::cerr << "# ERR: SQLException in " << __FILE__;
        std::cerr << "(" << __FUNCTION__ << ") on line " << __LINE__ << std::endl;
        std::cerr << "# ERR: " << e.what();
        std::cerr << " (MySQL error code: " << e.getErrorCode();
        std::cerr << ", SQLState: " << e.getSQLState() << " )" << std::endl;
    }

    return 0;
}

```
	



