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

## デプロイ（公開）方法

現在のFlaskアプリは**開発サーバー**のため、ローカル環境でのみ動作します。公開されているWebサイトのように24時間アクセス可能にするには、**本番環境へのデプロイ**が必要です。

### なぜ開発サーバーでは公開できないのか？

- 開発サーバー（`flask run`）はローカル開発専用
- サーバーを停止するとアクセスできなくなる
- セキュリティやパフォーマンスが本番用ではない

### 公開方法の例

**1. クラウドサービス（おすすめ）**
- **Heroku**: 無料枠あり、GitHub連携で自動デプロイ
- **Vercel/Netlify**: 静的サイト向けだがFlaskも可能
- **Render**: 無料枠あり、Docker対応

**2. VPS（仮想専用サーバー）**
- AWS EC2, DigitalOcean, Linodeなど
- 自分でサーバーを管理

### Herokuでのデプロイ例

1. **requirements.txtを作成**
```txt
Flask==2.3.3
```

2. **Procfileを作成**
```
web: gunicorn demo.demo:app
```

3. **Heroku CLIでデプロイ**
```bash
heroku create your-app-name
git push heroku main
```

これで `https://your-app-name.herokuapp.com` で24時間アクセス可能になります！

### 本番用WSGIサーバー

開発時は `flask run` を使いますが、本番では **Gunicorn** などのWSGIサーバーを使用：
```bash
pip install gunicorn
gunicorn demo.demo:app
```

