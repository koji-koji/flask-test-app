import os

from flask import Flask

# application factory function
def create_app(test_config=None):
  # create and configure the app
  # flaskのインスタンスを作成。
  # __name__は現在のパイソンのモジュール名。チュートリアルに記述あり。
  # instance_realtive_config=Trueは、設定ファイルがインスタンスフォルダーに関連することをアプリに通知。
  # インスタンスフォルダーは、コミットしてはならない情報を保持できる。
  app = Flask(__name__, instance_realtive_config=True)
  # アプリが使用するデフォルト構成を設定する。
  app.config.from_mapping(
    # デプロイ時にはランダムな値でオーバーライドするようにする。
    SECRET_KEY='dev',
    # SQLiteデータベースファイルが保存されるパス。
    DATABASER=os.path.join(app.instance_path, 'flaskr.sqlite')
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    # インスタンスフォルダー内のconfig.pyファイルから取得した値でデフォルト構成をオーバーライドする。
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # ensure the instance forder exists
  try:
    # app.instance_pathが存在することを確認する。
    # インスタンスフォルダーは自動で作成されないが、SQLiteデータベースファイルを作成するために、インスタンスフォルダーが必要になる。
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # a simple page that says hello
  @app.route('/hello')
  def hello():
    return 'Hello, World!'

  return app
