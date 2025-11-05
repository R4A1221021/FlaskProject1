from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# --- ダミーの掲示板投稿データ (グローバル変数として) ---
dummy_posts = [
    {
        'id': 3,
        'author': '管理者',
        'message': '○○小学校の体育館裏で犬（柴犬・オス・赤い首輪）を保護しています。心当たりの方は本部まで。',
        'timestamp': '11:05'
    },
    {
        'id': 2,
        'author': '鈴木 (305号室)',
        'message': 'スマートフォンの充電器（USB-C）を貸していただける方いませんか？',
        'timestamp': '10:45'
    },
    {
        'id': 1,
        'author': '匿名',
        'message': '北側のトイレ、トイレットペーパーが切れそうです。',
        'timestamp': '10:30'
    }
]


# ------------------------------

@app.route('/')
def index():
    """
    templates/index.html をブラウザに返す。
    (リストは 'id' の降順、つまり新しい順で渡す)
    """
    sorted_posts = sorted(dummy_posts, key=lambda x: x['id'], reverse=True)
    return render_template('index.html', posts=sorted_posts)


@app.route('/api/post_message', methods=['POST'])
def post_message():
    # 1. フォームからデータを取得
    author = request.form.get('author')
    message = request.form.get('message')

    # 2. 必須項目チェック (メッセージが空なら何もしないで戻る)
    if not message:
        return redirect(url_for('index') + '#community')  # 失敗時も掲示板へ

    # 3. 名前が空なら「匿名」にする
    if not author:
        author = '匿名'

    # 4. 現在時刻を取得
    now = datetime.datetime.now().strftime('%H:%M')

    # 5. 新しいIDを計算
    if dummy_posts:
        new_id = max(post['id'] for post in dummy_posts) + 1
    else:
        new_id = 1

    # 6. 新しい投稿データを作成
    new_post = {
        'id': new_id,
        'author': author,
        'message': message,
        'timestamp': now
    }

    # 7. ダミーリストに新しい投稿を追加
    dummy_posts.append(new_post)

    # 8. 処理完了後、トップページ ('/') の「#community」ハッシュ付きにリダイレクト
    # ▼▼▼ [修正点] ▼▼▼
    return redirect(url_for('index') + '#community')
    # ▲▲▲ [修正点] ▲▲▲


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)