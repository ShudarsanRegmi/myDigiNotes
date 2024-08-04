# Debugging in Qt C++

### How to write debug mssage
```
#include<QDebug>

//qInfo is qt5.5+ only.
qInfo() << "C++ Style Info Message";
qInfo( "C Style Info Message" );

qDebug() << "C++ Style Debug Message";
qDebug( "C Style Debug Message" );

qWarning() << "C++ Style Warning Message";
qWarning( "C Style Warning Message" );

qCritical() << "C++ Style Critical Error Message";
qCritical( "C Style Critical Error Message" );

// qFatal does not have a C++ style method.
qFatal( "C Style Fatal Error Message" )
```
