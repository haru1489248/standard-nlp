import MeCab
from collections import Counter
import re

# 表1.3（a）
text_wiki_japan = ("日本は東アジアの島国であり、北海道・本州・四国・九州の主要4島をはじめとする約1万4125の島嶼群から構成される。"
                   "国土面積は世界63位であり、ほかに世界第6位の広大な排他的経済水域を持つ。起伏に富んだ地形であり、"
                   "国土の75%は山地・丘陵地で、平地は比較的少ない。最高峰の富士山（3776 m〈メートル〉）をはじめ、"
                   "3000 mを超える高山は国土の中央部にあたる中部地方に集中する。気候は温暖湿潤気候が中心で[8]、四季が明瞭である[9]。"
                   "一方で外国に比べ自然災害が多く、地震や津波の被害を受けやすい[10]。国土の67%が森林で[11][12]、"
                   "固有種6342種を含む多様な生物相を有する。")

tagger = MeCab.Tagger()
tagger.parse("")

japan_words = tagger.parseToNode(text_wiki_japan)
japan_words = japan_words.next

result_A = []
skip_words = {'[', ']', '%', 'm', '][', ']。', ']、'}
while japan_words:
    surface = japan_words.surface
    feature = japan_words.feature.split(",")
    if feature[0] == '名詞':
        if re.fullmatch(r'[0-9]+', surface):
            pass
        elif surface in skip_words:
            pass
        else:
            result_A.append(surface)
    japan_words = japan_words.next

counter = Counter(result_A)

print('=======日本の名詞ランキング=======')
for japan_word, count in counter.most_common():
    print(japan_word, count)

# 表1.3(b)

text_america = ("コロンビア特別区および50州から構成される[9][10]。"
                "うち大陸本土の48州は北のカナダと南のメキシコとの間の北アメリカ大陸中央に位置する。"
                "アラスカ州は北アメリカ大陸北西部の角に位置し、東ではカナダと、"
                "西ではベーリング海峡を挟んでロシアと国境を接している。ハワイ州は太平洋中部に位置する島嶼群である。"
                "アメリカは太平洋およびカリブ海に5つの有人の海外領土を有する。")

tagger = MeCab.Tagger()
tagger.parse("")

america_words = tagger.parseToNode(text_america)
america_words = america_words.next

result_B = []
skip_words = {'50', '[', '9', '][', '10', ']。', '48', '5'}

while america_words:
    surface = america_words.surface
    feature = america_words.feature.split(",")
    if feature[0] == '名詞':
        if re.fullmatch(r'[0-9]+', surface):
            pass
        elif surface in skip_words:
            pass
        else:
         result_B.append(surface)

    america_words = america_words.next

counter = Counter(result_B)

print('=======アメリカの名詞ランキング=======')
for america_word, count in counter.most_common():
    print(america_word, count)