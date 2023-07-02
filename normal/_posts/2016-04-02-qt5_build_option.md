---
layout: post
title: QT 5.5 static source build
---

## QT 5.5 소스 빌드 옵션

 - default OpenGL
```bash
configure -release -static -skip qtxmlpatterns -skip qtdeclarative -skip qtquickcontrols -skip qtmultimedia -skip qtactiveqt -skip qtlocation -skip qtsensors -skip qtconnectivity -skip qtwebkit -skip qtwebkit-examples -skip qtimageformats -skip qtgraphicaleffects -skip qtscript -skip qtquick1 -skip qtserialport -skip qtenginio -skip qtwebsockets -skip qtwebchannel -skip qtwebengine -skip qtdoc -qt-sql-sqlite -qt-zlib -qt-libpng -qt-libjpeg -openssl -I D:/dev/int/src/messenger/mumble/00_src/OpenSSL/include -L D:/dev/int/src/messenger/mumble/00_src/OpenSSL/lib -platform win32-msvc2010 -no-dbus -nomake examples -nomake tests -ltcg -mp -opensource -confirm-license
```

 - without OpenGL
```bash
configure -release -static -skip qtxmlpatterns -skip qtdeclarative -skip qtquickcontrols -skip qtmultimedia -skip qtactiveqt -skip qtlocation -skip qtsensors -skip qtconnectivity -skip qtwebkit -skip qtwebkit-examples -skip qtimageformats -skip qtgraphicaleffects -skip qtscript -skip qtquick1 -skip qtserialport -skip qtenginio -skip qtwebsockets -skip qtwebchannel -skip qtwebengine -skip qtdoc -qt-sql-sqlite -qt-zlib -qt-libpng -qt-libjpeg -openssl -I D:/dev/int/src/messenger/mumble/00_src/OpenSSL/include -L D:/dev/int/src/messenger/mumble/00_src/OpenSSL/lib -platform win32-msvc2010 -no-opengl -no-angle -no-dbus -nomake examples -nomake tests -ltcg -mp -opensource -confirm-license
```


 - Ref: [Qt for Windows - Requirements](http://doc.qt.io/qt-5/windows-requirements.html), [StackoverFlow](
http://stackoverflow.com/questions/27759754/qt-5-4-static-build-produces-unresolved-external-symbol-link-error-in-visual-s)

