import re

s = 'bananaは¥300です。'
m = re.search(r'¥[1-9][0-9]*', s)
print(m)
if m:
    print(m.group())
    print(m.span())

# 文字列の中の最初に一致したものを取得する
# マッチオブジェクトを返す