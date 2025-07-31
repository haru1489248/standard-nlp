from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import MeCab
import re


tagger = MeCab.Tagger()
tagger.parse('')

def tokenize_with_mecab(text):
    text_words = tagger.parseToNode(text)
    text_words = text_words.next
    wakati_text = []
    while text_words:
        surface = text_words.surface
        feature = text_words.feature.split(",")
        if feature[0] == '名詞':
            if re.fullmatch(r'[0-9]+', surface):
                pass
            # if surface in skip_words:
            #     pass
            else:
                wakati_text.append(surface)
        text_words = text_words.next
    return wakati_text

docs = [("日本は東アジアの島国であり、北海道・本州・四国・九州の主要4島をはじめとする約1万4125の島嶼群から構成される。"
                   "国土面積は世界63位であり、ほかに世界第6位の広大な排他的経済水域を持つ。起伏に富んだ地形であり、"
                   "国土の75%は山地・丘陵地で、平地は比較的少ない。最高峰の富士山（3776 m〈メートル〉）をはじめ、"
                   "3000 mを超える高山は国土の中央部にあたる中部地方に集中する。気候は温暖湿潤気候が中心で[8]、四季が明瞭である[9]。"
                   "一方で外国に比べ自然災害が多く、地震や津波の被害を受けやすい[10]。国土の67%が森林で[11][12]、"
                   "固有種6342種を含む多様な生物相を有する。"),
        ("コロンビア特別区および50州から構成される[9][10]。"
         "うち大陸本土の48州は北のカナダと南のメキシコとの間の北アメリカ大陸中央に位置する。"
         "アラスカ州は北アメリカ大陸北西部の角に位置し、東ではカナダと、"
         "西ではベーリング海峡を挟んでロシアと国境を接している。ハワイ州は太平洋中部に位置する島嶼群である。"
         "アメリカは太平洋およびカリブ海に5つの有人の海外領土を有する。")
        ]

wakati_docs = []
for doc in docs:
    result = tokenize_with_mecab(doc)
    wakati_docs.append(' '.join(result))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(wakati_docs)

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

for i, row in df.iterrows():
    print(f"\n-----Document {i + 1} 上位重要単語 ---")
    top_words = row.sort_values(ascending=False).head(10)
    print(top_words)
