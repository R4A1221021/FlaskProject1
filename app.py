from flask import Flask, render_template

# Flaskアプリケーションの初期化
app = Flask(__name__)

# --- メインのルート ---
@app.route('/')
def index():
    """
    ルートURL ('/') にアクセスがあった場合、
    templatesフォルダ内の index.html を表示する。
    """
    return render_template('index.html')

# --- （将来的な機能拡張用：例）---
# @app.route('/api/send_message', methods=['POST'])
# def send_message():
#     # ここにチャットメッセージを処理するロジックを書く
#     pass

# @app.route('/api/report_safety', methods=['POST'])
# def report_safety():
#     # ここに安否情報をデータベースに保存するロジックを書く
#     pass

# --- サーバーの起動 ---
if __name__ == '__main__':
    """
    ラズパイのローカルネットワーク内の他のデバイス (スマホなど) から
    アクセスできるように、host='0.0.0.0' で起動します。
    """
    # debug=True は開発中は便利ですが、本番運用ではFalseにします。
    app.run(debug=True, host='0.0.0.0', port=5000)