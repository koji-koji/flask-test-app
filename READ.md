# 目的
flask学習用のサンプルアプリです。
dockerをセットしており、アプリを起動してすぐ触れるようにしています。

flaskチュートリアルのApplication Setupまで完了しています。
https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

上記のドキュメントはversion1.1.xなので、最新のものを参照してください。

# 手順。
```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it flask-test-app_web_flask_1 /bin/bash
$ flask run --host 0.0.0.0 --port 5000
```

以下のURLにアクセス。
http://localhost:5000/

Hello, World!が帰ってきます。
