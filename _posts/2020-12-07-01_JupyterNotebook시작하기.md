---
title : "[프로그래머스 인공지능 스쿨]Jupyter Notebook 시작하기"
data : 2020-12-07 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
---
# Jupyter Notebook 시작하기
## Jupyter Notebook
기존의 IDE는 주석을 쓰기 힘들다. 주석을 길게 달면 코드 내용의 메인을 따라가기 힘들게 만들기 때문이다. 주피터 노트북은 interactive한 파이썬 코드를 작성하고 공유를할 수 있도록 도와주는 개발 도구이다. <br>
파이썬 코드와 마크다운 영역을 나눠서 작성이 가능하다.<br>
- jupyer notebook 설치 및 실행
```
$ sudo rm -rf /Library/Frameworks/Python.framework
$ rm /usr/local/bin/python3*
$ brew uninstall python3
$ brew install python3
$ which python3
$ sudo python3 -m pip install --upgrade pip
$ sudo python3 -m pip install jupyter
$ which jupyter
$ jupyter notebook
```

### jupyter notebook 사용하기 꿀팁

![Alt Text](/assets/images/20201207/1.png)  

ln[]:가 있는 초록창 안에서 shift+enter버튼을 누르면 실행 결과가 나오며 새로운 칸이 생긴다.<br>
esc를 누르면 초록색 테두리에서 파란색 테두리로 바뀌고, m을 누르면 앞의 In[]:이 사라진다. 이후 다시 enter를 누르면 초록색 테두리로 변하고, ###Hello World!를 입력한 후 shift+enter를 누르면 마크다운으로 변한다! <br>
1. Notebook의 2가지 Mode
- 초록색 테두리 : 입력 모드
    - Enter로 접근
- 파란색 테두리 : 명령 모드
    - ESC로 접근

2. Notebook의 2가지 Cell
- Code Cell
    - Python 3을 실행할 수 있는 Cell
    - 왼쪽에 In[]:이 뜬다.
- Markdown Cell
    - Markdown을 작성할 수 있는 Cell
    - 왼쪽에 In[]:이 뜨지 않는다.

ESC를 누른 상태에서...<br>
M : Mardown Cell로 바꾸는 명령어<br>
Y : Code Cell로 바꾸는 명령어<br>

3. Cell 추가하기
명령 Mode에서(ESC):<br>
A : Above 를 통해 현재 Cell 위에 새로운 Cell 추가 <br>
B : Below 를 통해 현재 Cell 아래에 새로운 Cell 추가 <br>

4. Cell 삭제하기
명령 Mode에서(ESC):<br>
dd를 통해 현재 Cell 삭제 <br>

5. Cell 실행하기
입력 Mode에서:<br>
ctrl/cmd + enter를 통해 현재 Cell 실행<br>
shift + enter를 통해 현재 Cell 실행 후 다음 셀로 넘어감<br>

<br>
<br>
<br>

## Markdown
Markdown의 여러 문법들! 이 블로그 또한 마크다운으로 작성하고 있어 익숙하지만 정리해두고자 한다.<br>

## 1. Header(#, ##, ###, ...)  

```
# Header 1 - 제목
```
# Header 1 - 제목

```
## Header 2 - 소제목
```
## Header 2 - 소제목

```
## Header 3 - 강조 등등..
```
## Header 3 - 강조 등등..


## 2. Italic(*...*, _..._)
마크다운 문법에는 엔터(줄바꿈)이 없으므로 내용을 입력하고 띄어쓰기를 두번 해줘야 엔터가 된다. 혹은 <br>을 쓰면 된다.
```
*Italic*  
_Italic_  
```
*Italic*  
_Italic_  


## 3. Bold(**...**, __...__)
```
**bold**  
__bold__
```
**bold**  
__bold__  
```
나는 __불닭볶음면__ 을 좋아해.
나는 **불닭볶음면** 을 좋아해.
```
나는 __불닭볶음면__ 을 좋아해.  
나는 **불닭볶음면** 을 좋아해.  


## 4. Strikethrough (~...~)
```
~strikethrough~  
```
~strikethrough~  <-문자 중간에 취소선이 그어짐!  

## 5. Unordered List(- ..., * ...)
```
- 하나
- 둘
- 셋
* 하나
* 둘
* 셋
```
- 하나
- 둘
- 셋
* 하나
* 둘
* 셋

## 6. Ordered List(1. ...)
```
1. 하나
2. 둘
3. 셋
```
1. 하나
2. 둘
3. 셋

