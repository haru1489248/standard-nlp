# 問題1
# 表1.2のランキングを作成するプログラム

# Mecabを使用して形態素解析をする
# 仕組み
# Pythonコード
#    ↓
# mecab-python3（C言語バインディング）
#    ↓
# MeCab本体（C/C++で実装された解析エンジン）
#    ↓
# 辞書ファイル（例：IPA辞書やNEologd）を参照
#    ↓
# 形態素解析の結果を返す

# 表1.2(a)
import MeCab
from collections import Counter

text = ("子供の時の愛読書は「西遊記」が第一である。これ等は今日でも僕の愛読書である。"
    "名高いバンヤンの「天路歴程」なども到底この「西遊記」の敵ではない。"
    "それから「水滸伝」も愛読書の一つである。中学を卒業してから色んな本を読んだけれども、"
    "特に愛読した本というものはないが、概して云うと、絢爛とした小説が好きであった。")

tagger = MeCab.Tagger("-Owakati")  # 「分かち書きモード」で出力
words = tagger.parse(text).strip().split()

counter = Counter(words)

print("===単語の頻出ランキング===")
for word, count in counter.most_common(10):
    print(word, count)

print("=======================")
# 表1.2（b）

tagger = MeCab.Tagger()
# これをしないとUnicodeDecordErrorになる
tagger.parse("")

node = tagger.parseToNode(text)
# 最初は特別なBOS（Beginning of Sentence)が入っているので空白が出力されてしまうのでnextで飛ばす
node = node.next
# print(node.surface)
# print(node.feature.split(","))

nouns = []

while node:
    feature = node.feature.split(",")
    if feature[0] == "名詞":
        nouns.append(node.surface)
    node = node.next

counter = Counter(nouns)

print("===名詞の頻出ランキング===")
for noun, count in counter.most_common():
    print(noun, count)

print("=======================")

