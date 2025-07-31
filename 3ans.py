import requests
import time
import MeCab
import re
from collections import Counter

def get_wikipedia_text(title):
    """Wikipediaからテキストを取得（エラーハンドリング付き）"""
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "titles": title,
        "format": "json",
        "explaintext": ""
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # HTTPエラーをチェック

        # JSONデコードエラーをチェック
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print(f"'{title}' のレスポンスがJSON形式ではありません")
            return None
        
        pages = data['query']['pages']
        for page_id in pages:
            page = pages[page_id]
            if 'extract' in page:
                return page['extract']
            else:
                print(f"ページ '{title}' の内容を取得できませんでした")
                return None
                
    except requests.RequestException as e:
        print(f"'{title}' の取得でエラー: {e}")
        return None
    except Exception as e:
        print(f"'{title}' で予期しないエラー: {e}")
        return None

# 存在するページのみを使用
japan_articles = [
    "日本", "日本の政治", "日本の経済", "日本の地理",
    "日本の歴史", "日本の文化", "日本の社会", "日本の教育"
]

all_japan_texts = []
for article in japan_articles:
    print(f"==={article}を取得中===")
    text = get_wikipedia_text(article)
    if text:
        all_japan_texts.append(text)
        print(f"成功!{len(text)}文字")
    else:
        print(f"失敗")
    print("-" * 30)

    # API制限を避けるため3秒待機
    time.sleep(20)

tagger = MeCab.Tagger()
tagger.parse('')

def tokenize_with_mecab(text):
    """Mecabを使用してテキストをトークン化"""
    text_words = tagger.parseToNode(text)
    text_words = text_words.next
    wakati_text = []
    while text_words:
        surface = text_words.surface
        feature = text_words.feature.split(",")
        if feature[0] == '名詞':
            if re.fullmatch(r'[0-9]+', surface):
                pass
            else:
                wakati_text.append(surface)
        text_words = text_words.next
    return wakati_text

if all_japan_texts:
    combined_text = ' '.join(all_japan_texts)
    result = tokenize_with_mecab(combined_text)
    print("トークン化結果:", result)
else:
    print("テキストを取得できませんでした")
