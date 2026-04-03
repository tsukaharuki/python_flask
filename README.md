# python_flask

Flaskを使ったシンプルなWebアプリケーション

## プロジェクト構成

```
python_flask/
├── README.md
├── demo/
│   ├── demo.py                 # Flaskアプリケーション
│   └── templates/              # HTMLテンプレート（Flaskが自動検出）
│       ├── demo.html           # ベーステンプレート
│       ├── demo2.html          # メニュー画面（demo.htmlを継承）
│       ├── jikosyoukai.html    # 自己紹介ページ（demo2.htmlを継承）
│       └── hobby.html          # 趣味ページ（demo2.htmlを継承）
```

## テンプレートディレクトリについて

**important:** Flaskは `templates/` フォルダ名を自動的に認識します
- デフォルトでは、Flaskアプリがあるディレクトリと同じレベルの `templates/` フォルダを探します
- 別のフォルダ名を使いたい場合は、Flask初期化時に指定：
  ```python
  app = Flask(__name__, template_folder='custom_folder')
  ```

## 起動方法

```bash
cd python_flask
FLASK_APP=demo/demo.py FLASK_ENV=development flask run
```

- トップページ: http://127.0.0.1:5000/
- 自己紹介: http://127.0.0.1:5000/p
- 趣味: http://127.0.0.1:5000/h

## サーバーの停止・再起動

**サーバーを停止する場合：**
- ターミナルで `Ctrl+C` を押す

**ポートが使用中の場合の強制停止：**
```bash
# ポート5000を使用しているプロセスIDを確認
lsof -ti:5000

# プロセスを強制終了（例: PIDが12345の場合）
kill -9 12345

# 再度起動
FLASK_APP=demo/demo.py FLASK_ENV=development flask run
```

## テンプレート継承

このプロジェクトでは、Jinja2のテンプレート継承機能を使用しています：
- `demo.html` がベーステンプレート（ヘッダー、レイアウト定義）
- `demo2.html` は `demo.html` を継承
- `jikosyoukai.html` と `hobby.html` は `demo2.html` を継承

