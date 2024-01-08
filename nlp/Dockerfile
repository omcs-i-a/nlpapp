# Pythonランタイムを親イメージとして使用
FROM python:3.9.4

# 作業ディレクトリを/appに設定
WORKDIR /app

# 環境変数を設定
ENV FLASK_APP=nlp_server.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0

# requirements.txtで指定された必要なパッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# ポートの公開
EXPOSE 5000

# 現在のディレクトリの内容をコンテナ内の/appにコピー
COPY . /app

