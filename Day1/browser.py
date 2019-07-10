import webbrowser

idols = ['bts','iu','itzy']

for idol in idols:
    # string interpolation
    # 문자열 보간법 : f-string  / 3.6+
    webbrowser.open(f'https://search.naver.com/search.naver?&query={idol}')