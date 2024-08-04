# Important code blocks for qt

## Reading from a file
```cpp
#include <QFile>
#include <QDir>

    qDebug() << "Button pressed";
    qDebug() << "Current working directory: " << QDir::currentPath();
    qDebug() << "File exists: " << QFile::exists("/home/sudoerson/Desktop");
    QFile file("/home/sudoerson/qtprojs/fileHandling/in.txt");

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Could not read file";
        qDebug() << file.errorString();
        return;
    }

    while (!file.atEnd()) {
        QByteArray line = file.readLine();
        ui->mainTextEdit->append(line);
        qDebug() << line;

    }
```
