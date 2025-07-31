import re
s = 'aa000'
m = re.match(r'aa[0-9]{3}', s)
print(m)
if m:
    print(m.group())
    print(m.span())

# 文字列の始まりをフィルターする
# マッチオブジェクトを返す