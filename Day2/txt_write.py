# option 1
# 파일을 연다.
# open('파일명', '옵션')
# w : write (덮어쓰기)
# a : append(이어쓰기)
f = open('ssafy.txt','a')

# 글을 작성한다.
for i in range(10):
    # \n : 개행문자 (엔터 : newline)
    f.write(f'안녕하세요. {i}\n')

# 파일을 닫는다.
f.close()

# option 2. 컨택스트 매니저(context manager) with 구문
with open('ssafy_with.txt','w') as f:
    for i in range(5):
        f.writelines(['은정','인성\n'])