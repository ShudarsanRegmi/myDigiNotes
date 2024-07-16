# Qfile in qt
>It is used to perform file operations in qt framework

QFile is an I/O device for reading and writing text and binary files and resources. A QFile may be used by itself or, more conveniently, with a QTextStream or QDataStream.

The file name is usually passed in the constructor, but it can be set at any time using setFileName(). QFile expects the file separator to be '/' regardless of operating system. The use of other separators (e.g., '\') is not supported.

You can check for a file's existence using exists(), and remove a file using remove(). (More advanced file system related operations are provided by QFileInfo and QDir.)

The file is opened with open(), closed with close(), and flushed with flush(). Data is usually read and written using QDataStream or QTextStream, but you can also call the QIODevice-inherited functions read(), readLine(), readAll(), write(). QFile also inherits getChar(), putChar(), and ungetChar(), which work one character at a time.

