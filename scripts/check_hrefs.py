import re
content = open('pages/mujer.html', encoding='utf-8').read()
print(list(set(re.findall(r'href=[\'\"]([^\'\"]+)[\'\"]', content))))
