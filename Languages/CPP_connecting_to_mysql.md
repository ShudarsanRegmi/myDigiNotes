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



