
from tkinter import *
import pandas as pd

dat = pd.read_excel("./service.xlsx")

window= Tk()
window.title("Food price and store introduction")

# 01 입력 상자 설명 레이블
label = Label(window, text="원하는 음식 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(entry)
entry=Entry(window,width=15,bg='light pink')
entry.grid(row=1,column=0,sticky=W)

#제출 버튼을 클릭했을때, 동작가능
def click():
    print("버튼이 클릭되었습니다.")
    word=entry.get()
    output.delete(0.0,END)
    try:
        def_word1 =dat.loc[dat['품목별']==word, '조사가격'].values[0]
        def_word12 = dat.loc[dat['품목별'] == word, '상호'].values[0]
        def_word13 = dat.loc[dat['품목별'] == word, '연락처'].values[0]
    except:
        def_word1="단어 뜻을 찾을 수 없음."
    output.insert(END, def_word1)
    output.insert(END, def_word12)
    output.insert(END, def_word13)

# 03 제출 버튼 추가
btn = Button(window, text="엔터", width=5, command=click) #함수연결
btn.grid(row=1, column=0, sticky=E)

# 04 설명 레이블 - 의미
lable2 = Label(window, text="\n의미:")
lable2.grid(row=2, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light yellow")
output.grid(row=3, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()