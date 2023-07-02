---
layout: post
title: 정적 파일 Hosting(Node.js + Windows 서비스)
---

## Connect, ServerStatic

html 문서 몇 개를 간단히 호스팅 하고 싶을 때는 [serve](https://www.npmjs.com/package/serve)나,
[connect](https://www.npmjs.com/package/connect)/[serve-static](https://www.npmjs.com/package/serve-static)을 쓰면 편하다.

여기서는 `connect + serve-static` 조합을 윈도우 서비스로 등록해서 사용하는 방법을 정리한다.

### http_server.js

호스팅 하려는 폴더가 `D:\work\public`이라고 하면, 해당 폴더에 아래와 같이 `http_server.js` 파일을 만든다.

```js
var finalhandler = require('finalhandler')
var http = require('http')
var serveStatic = require('serve-static')

// Serve up public folder
var serve = serveStatic('D:\\work\\public\\', { 'index': ['index.html', 'index.html']})

// Create server
var server = http.createServer(function onRequest (req, res) {
    serve(req, res, finalhandler(req, res))
})

// Listen
server.listen(3000)
console.log('Server running on 3000 ...');
```

### node-windows
다음으로 node.js를 윈도우 서비스로 등록해 주는 [node-windows](https://github.com/coreybutler/node-windows)를 설치한다.


```js
npm install -g node-windows
npm link node-windows
```

### setup_win_service.js

윈도우 서비스로 등록하기 위해 아래 스크립트를 만든다.

```js
var Service = require('node-windows').Service;

// Create a new service object
var svc = new Service({
    name:'YourServiceName',
    description: 'YourServiceDesc',
    script: 'D:\\work\\public\\http_server.js'
});

// Listen for the "install" event, which indicates the
// process is available as a service.
svc.on('install', function() {
    svc.start();
});

svc.install();
```

실행한다.
```js
node setup_win_service.js
```

윈도우 서비스 관리자에 `YourServiceName` 서비스가 등록되고 자동 실행된다.
브라우저에서 `http://localhost:3000/your.html`로 열 수 있다.

#### 참고:  
[StackOverFlow 1](https://stackoverflow.com/questions/10547974/how-to-install-node-js-as-windows-service)  
[StackOverFlow 2](https://stackoverflow.com/questions/6084360/using-node-js-as-a-simple-web-server)


