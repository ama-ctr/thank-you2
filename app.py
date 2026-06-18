from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # 1. サーバーにあるHTMLファイルを読み込む
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # 2. Renderに設定した「秘密の鍵」を取り出す
        api_key = os.environ.get('API_KEY')
        
        if not api_key:
            return "エラー: APIキーが設定されていません。RenderのEnvironment Variablesを確認してください。"

        # 3. HTMLの中の「空っぽの鍵置き場」を「本物の鍵」に書き換える
        html_content = html_content.replace('const API_KEY = "";', f'const API_KEY = "{api_key}";')

        # 4. 完成したHTMLをそのままブラウザに送る（一番安全な方法）
        return html_content

    except Exception as e:
        # 万が一パニックになったら、その理由を画面に表示する
        return f"サーバーエラーが発生しました: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
