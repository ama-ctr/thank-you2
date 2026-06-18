from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 1. サーバーにあるHTMLファイルを読み込む
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 2. Renderに設定した「秘密の鍵」を取り出す
    api_key = os.environ.get('GEMINI_API_KEY')
    
    if not api_key:
        return "エラー: APIキーが設定されていません。RenderのEnvironment Variablesを確認してください。"

    # 3. HTMLの中の「空っぽの鍵置き場」を「本物の鍵」に書き換える
    # (HTML側の 'const apiKey = "";' という部分を探して置き換えます)
    html_content = html_content.replace('const apiKey = "";', f'const apiKey = "{api_key}";')

    # 4. 完成したHTMLをブラウザに送る
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
