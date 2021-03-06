#!/usr/bin/env python
# coding: utf-8

# # 5장. 문자열과 배열

# ## 문자열

# In[1]:


print("My friend's house.")


# In[2]:


# print('My friend's house.') 이렇게 쓰면 안 된다. #때에 따라 작은따옴표와 큰따옴표를 잘 구분해서 써야 한다.


# In[3]:


print('엔시티 재현이가 말했다. "안녕!"') #여기도 작은따옴쓰와 큰따옴쓰를 잘 구별...


# In[4]:


animal = 'frog' #문자열은 처음 인덱스부터 0, 1, 2... 이렇게 되는 배열이다 사실.
print(animal[3])


# In[5]:


animal = 'frog' #마지막 인덱스부터 -1, -2... 할 수도 있다.
print(animal[-1])

Quiz 5.2 (p.67)
# In[6]:


fruit = '오렌지'
print(fruit[1]) #양수 인덱스 함 해 봐 ㅋ
print(fruit[-2]) #음수 인덱스 함 해 봐 ㅋ

Quiz 5.3
# In[7]:


animal = 'frog'
print(animal[1:4:2])


# In[8]:


animal = 'elephant'
print(animal[1:7:2])


# In[9]:


animal = 'elephant'
print(animal[5:])


# In[10]:


animal = 'elephant'
print(animal[3:-3]) #인덱스가 -3인 놈은 a지만, 슬라이싱은 마지막 놈 '바로 전'까지 출력하는 놈이라 그렇다.


# In[11]:


animal = 'elephant'
print(animal[-5:]) #어 이게 이렇게 되네

퀴즈) pha만 출력되게 해 보시오.
# In[12]:


print(animal[3:6])


# In[13]:


print(animal[3:-2])


# In[14]:


print(animal[-5:-2]) #우와 이렇게 다양한 방법으로 할 수 있어요~~~ ㅋ~~~~ (제발 제발 음수 인덱스 쓸 일 없게 해 주세요 귀찮단말임)

퀴즈) 아래 3개를 출력하면 어떻게 될까?? (글쎄요)
# In[15]:


animal = 'elephant'
print(animal[::3])
print(animal[::-1])
print(animal[::])


# ### 문자열 함수들 (p.71)

# In[16]:


animal = 'elephant'
print(len(animal))


# In[17]:


animal = 'elephant'
print('e 개수:', animal.count('e'))
print('ep 개수:', animal.count('ep'))


# In[18]:


animal = 'elephant'
print('앞쪽 찾기:', animal.find('e'))
print('ep 앞쪽 찾기:', animal.find('ep'))
print('뒤쪽 찾기, right find의 줄임말:', animal.rfind('e'))
print('위치:', animal.index('e'))
print('n이 있냐?:', 'n' in animal)

퀴즈 5.4) 한 줄에 알파벳 하나씩 출력되게 해 보자 ㅋ 교과서 p.74 ㅋ
# ### 내가 답을 못 맞췄던 퀴즈 5.4 (p.74)

# In[19]:


seq = 'Hello!'
for s in seq: #헐. 이게되네.
    print(s)


# In[20]:


seq = 'Hello!'
for s in range(len(seq)): #교과서의 의도와는 조금 다르지만... "이것도되네"
    print(seq[s])


# In[21]:


seq = 'Hello!'
for s in seq:
    print(s, end = '') #print(s, end = "\t")라고 하면 아 아 안 녀 어 엉 이렇게 칠 수 있다.

https://www.geeksforgeeks.org/python-sep-parameter-print/
여기 가 보면 파이썬 print()문의 sep(separator)와 end의 용례를 자세히 볼 수 있다. 참고하셈.
# In[22]:


seq = 'Hello!'
for i in seq:
    print(i, sep = '.', end = '') #print(i)만 여러 번 돌아가는 거라 sep은 안 작동한다. print('H', 'e', 'llo','!', sep = '.) 하면 내 생각대로 될걸.


# In[23]:


print('H', 'e', 'llo','!', sep = '.') #어. 이제되지?


# ### 문자열 계속... p.73, 정보 수정 메소드들

# In[24]:


ai = 'python program'
print('Find and replace:', ai.replace('p', 'P'))
print('전체 소문자로:', ai.lower())
print('전체 대문자로:', ai.upper())
print('대문자 <=> 소문자:', ai.swapcase())
print('첫 문자만 대문자로:', ai.capitalize()) #아니? 내가 생각하던 것처럼 '제목 대문자화하는 방식'으로 되는 게 아니네. 유념하자. ha ha!!


# In[25]:


nct = 'NCT Jaehyun' #이렇게 대소문자 섞인 예문으로 하면 어떨까?
print('Find and replace:', nct.replace('n', 'N'))
print('전체 소문자로:', nct.lower())
print('전체 대문자로:', nct.upper())
print('대문자 <=> 소문자:', nct.swapcase())
print('첫 문자만 대문자로:', nct.capitalize())

- 먹기 전에 껍질을 까 먹어 보자. 공백 제거 메소드들
# In[26]:


animal = '     elephant             '
print('왼쪽 벗겨내기:', animal.lstrip(), '드래그해 보면 elephant 오른쪽 공백은 안 사라졌다.') 
print('오른쪽 벗겨내기:', animal.rstrip())
print('양쪽 벗겨내기:', animal.strip())

이교진 선생님께서, 웹에서 크롤링해 온 데이터는 어디에 공백이 숨어 있을지 모르니 꼭 strip()을 해서 안전하게 취급하라고 하신 말씀이 기억난다. 하긴. 괜히 숫자인데 공백 끼어 들어와서 "헐. 저 숫자 아닌데요???" 당할 수 있으니까.
# ### Random 모듈 (p.74)

# In[27]:


import random
random.random() #이러면 0과 1 사이의 실수 범위에서 ㄹㅇ '무작위 값'이 나온다.


# In[28]:


import random
random.randrange(1,7) #1과 6까지 정수(range()처럼 뒤 수 - 1까지다.) 중 랜덤한 값. 육면체 주사위를 던지는 거랑 똑같은 함수다.


# In[29]:


import random
char = '한글우수'
print(random.choice(char))
print(random.choices(char)) #리스트 배열

인간이 가장 졸린 시간, 오후 1시 48분
(정보 출처: 내가 정함)퀴즈 5.5(p.75)
# In[30]:


import random
pw = str() #pw라는 이름의 빈 문자열을 생성
chars = '한글우수'
for _ in range(5):
    pw = pw + random.choice(chars) #무작위 문자 병합
print(pw)

오 대박. 위 퀴즈 여러 번 돌려 보다가 '글글글글수' 나왔다. 코로나19 발원지인 '우한우한한'도 나왔다.

- random() 함수를 이용하면 주사위, 윷놀이, 1-45 복권 추첨 등등 다양한 걸 할 수 있겠구나.퀴즈 5.6) 비밀번호로 쓸 만 한 무작위 배열을 토해내는 함수, passwd()를 만들어 보자.
# In[45]:


import random
def passwd(length):
    
    pw = str() #str()는 빈 문자열 생성
    chars = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '!@#$%^&*'
    
    for _ in range(length):
        pw = pw + random.choice(chars)
    
    return pw

print(passwd(8))


# ## 배열의 종류
Quiz 5.7 - p.80 - 슬라이싱으로(if문 말고) 오렌지만 출력
# In[32]:


fruits = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']
print(fruits[1::2])

돌발퀴즈 1) 그치만 난 뚝심이 있는 사람이니까. if문으로도 ㄱㄱ해 보자.
# In[33]:


fruits = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']

oranges = ''

for i in fruits: #퀴즈 5.4 (차례 1.1.2)의 방법이 여기서도 된다.
    if (i == '오렌지'): #내가 if문 끝에 : 쓰는 걸 까먹었다고 에러가 났다. 파이썬에서는 :를 잘 기억하자.
        oranges = oranges + i + ' ' #여기서 oranges.append(i)라는 놈을 써도 된대.

print(oranges)


# In[41]:


fruits = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']

oranges = '' #초기화하는 걸 까먹으니까 큰일이 났었다. 꼭 초기화하자, 크킄.

for i in range(len(fruits)): # 원랜 for i in range(6)으로 했었지만, 생각해 보니 이렇게 쓰는 게 더 간지난다.
    if (fruits[i] == '오렌지'):
        oranges = oranges + fruits[i] + ' '#역시 여기도 oranges.append(i) 가능

print(oranges)


# In[43]:


fruits = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']

oranges = [word for word in fruits if '오렌지' in word]
print(oranges)

위의 방법으로도 할 수 있다. 파이썬 책 p.84부터 나오는 '리스트의 함축'기능이다.
난 저번 주 목요일에 수면내시경 찍느라 못 들었던 부분이다.돌발퀴즈 2) count()를 이용해서 오렌지 개수: 몇 개.  이렇게 출력하는 명령어를 만들어 보자, 크킄.
# In[44]:


fruits = ['사과', '오렌지', '포도', '오렌지', '복숭아', '오렌지']

print('오렌지는', fruits.count('오렌지'), '\b개였다.')


# ### List형 자료 주무르기 -  병합(Merge), 삽입(Insert)

# In[50]:


x = 12.23
y = 23.34
packing = [x, y] # packing해 보자.
print('[x, y]라고 만든 packing의 자료형은:' , type(packing))
print('Packing:', packing)
[c1, c2] = packing #unpacking해 보자.
print('Unpacking:\nc1:', c1)
print('c2:', c2)

퀴즈 5.8 - p.81
# In[59]:


student = ['민준', 183, '서연', 168, '현우', 181, '민서', 199 ] # 다들 간지가 나게, 내 마음대로 키를 좀 올렸다.

alldata = [] #List형인 alldata를 초기화해 주려면, str처럼 '' 하는 게 아니라 [] 해야 한다.

alldata = (student + ['동현', '189']) # 동현아. 너도 예외 없이 사지연장술 받아라 ㅋ

print(str(len(alldata)) + '개 데이터') # 형변환 없이 print(len(alldata), '개 데이터')라고 해도 된다.

alldata = (student, '동현', '189')라고 하면 답이 '3개 데이터'라고 희한하게 나온다.
alldata = (student, ['동현', '189'])라고 하면 '2개 데이터'. 왜인지는 잘 생각해 보자 ㅋ
# ### 리스트에 원소 삽입하는 법: append(), insert(), 리스트 함축(Comprehension)

# In[60]:


prime = [2,3,5]
prime.append(7) #달랑달랑 매달아 주는 append() 함수. 그래서인지 달랑달랑 매달려 있는 맹장의 이름이 appendix다.
print(prime)


# In[65]:


a = list() #빈 리스트 만들기. a = []라고 쓰는 거랑 같다.
print(a)

for i in range(5):
    a.append(i)
    print(a[i], end = " ")


# In[69]:


fruit = ['사과', '굴', '포도'] #"내가 과일이라고 생각한다면, 굴도 과일이다"
fruit.append('체리')
print(fruit)


# ### 많이 헷갈렸기도 하고, 지역 변수의 개념을 이해하기 위해서도 굉장히 중요한 Quiz 5.9 - p.82

# In[72]:


def new(n, x):
    n = 2
    x.append(x[-1] + 1) #음수 배열 인덱스를 이렇게 쓰는구나. 배열 x가 있으면 걔의 마지막 인덱스 + 1을 append하라는 말이다.
    print('new:', n, x)
    
def one():
    n = 1
    x = [0, 1, 2]
    print('one:', n, x)
    new(n,x)
    print('one:', n, x)
          
one()

Quiz 5.10
# In[74]:


bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']

for i, animal in enumerate(animals):
    if(animal == '새'):
        bird_pos.append(i)
        
print(bird_pos)

Insert문으로 리스트에 뭐 넣기 - 퀴즈 5.11 (p.84)
# In[75]:


fruits = ['사과', '오렌지', '포도']
fruits.insert(-2, '키위')
print(fruits)

헐 이게 사과 키위 오렌지 포도라고 나오네!!! (-2 인덱스인 오렌지 "앞에" 저장된다고 한다. 명심하자 ㅋ)아래 내용은 4.28(목)에 쓰는 내용이다 그렇지만... "오늘 중급회계 I 시험 봐야 돼서 일찍 나갈 거야"
# In[1]:


#돌발퀴즈: 사과 오렌지 당근 포도 순서 되게, 음수 인덱스 써서 당근 삽입하기.

fruits = ['사과', '오렌지', '포도']
fruits.insert(-1, '당근') #포도의 인덱스를 입력하면 포도 '바로 전'에 당근이 삽입된다.
print(fruits)


# In[2]:


#돌발퀴즈 2: 사과 오렌지 당근 포도 순서 되게, 양수 인덱스 써서 당근 삽입하기.

fruits = ['사과', '오렌지', '포도']
fruits.insert(3, '당근') #양수 인덱스를 써도, 그냥 포도의 인덱스를 쓰면 된다.
print(fruits)


# ### 리스트의 함축(Comprehension) (p.78)
for i in 리스트명
    if 조건식:
        새 리스트에 i를 더해라.
        
        
뭐 이런 코드를[i for i in 리스트명 if 조건식]
이렇게 쓰는 걸 리스트의 함축이라고 한다. 양쪽 대괄호까지 써 줘야 한다.
# In[5]:


mylist = [3, 5, 4, 9, 1, 8, 2, 1]
newlist = [i for i in mylist if (i%2 == 0)]
print(newlist)


# In[10]:


#위 코드는 이 for-if문을 쓴 코드와 같다.
#사실 함축하는 것보다 이게 더 가독성이 좋다... 이것도 그냥, "함축이라는 게 있는 것만 알아 둬라"가 되지 않을까?

mylist = [3, 5, 4, 9, 1, 8, 2, 1]
newlist = []

for i in mylist:
    if (i %2 == 0):
        newlist.append(i)

print(newlist)

newlist가 빈 리스트라도 쓰기 전에 초기화해 주는 건 당연한데, 함축을 쓰는 코드에서는 초기화할 필요도 없다니.
그렇지만 초기화 할 때랑 안 할 때를 구별하는 나쁜 습관을 괜히 들이지 말자. 누울 자리 보고 발 뻗냐?
그냥... "뭘 쓰기 전엔 무조건 초기화하는 좋은 습관을 들이자"
# In[12]:


#.append(i)를 쓰지 않고, 이렇게 mylist의 각 원소 i를 리스트형으로 바꿔서 달 수도 있다.

mylist = [3, 5, 4, 9, 1, 8, 2, 1]
newlist = []

for i in mylist:
    if (i %2 == 0):
        newlist = newlist + [i]

print(newlist)

퀴즈 5.12 (p.84) - 너는 성인이냐 아니냐
(19세 이상이라고 심적으로 어른이 되는 건 아니지만, 법적으로 성인이 되는 건 맞으니까.)
# In[14]:


people = [31, 53, 41, 19, 15, 18, 21, 13]
adult = [i for i in people if(i >= 19)]
print(adult)


# In[16]:


#for문을 쓰면 이렇게 가능하다.
#교) 크롤링한 데이터를 받아들일 때는 이렇게 for문을 더 많이 써요.
#나) 함축. 너. 뉘기야. 너. 왜 배우냐.

people = [31, 53, 41, 19, 15, 18, 21, 13]
adult = []

for i in people:
    if (i >= 19):
        adult.append(i)

print(adult)


# ### 리스트의 항목 삭제(p.85)
리스트의 항목은 del 명령문, pop() 메소드, 빈 리스트를 나타내는 []로 삭제할 수 있다.
# In[25]:


nums = [0, 2, 4, 6, 8, 10]
del nums[1] 
print(nums)


# In[26]:


nums = [0, 2, 4, 6, 8, 10]
del nums[1:5] #슬라이싱으로 범위 삭제도 가능하다.
print(nums)


# In[19]:


nums = [0, 2, 4, 6, 8, 10]
nums.pop() #그냥 pop() 하면 맨 마지막 놈이 사라진다.
print(nums)


# In[22]:


nums = [0, 2, 4, 6, 8, 10]

for _ in range(6):
    nums.pop() #여드름 짜듯이 Keep popping off!!! <그리고 아무도 없었다>라는 소설이 생각나네.
    print(nums)


# In[27]:


nums = [0, 2, 4, 6, 8, 10]
nums.pop(2) #pop()으로 죽을 놈의 인덱스를 정해 줄 수도 있다.
print(nums) #('2'라는 원소를 없애는 게 아니다. 인덱스가 2번인 놈을 죽이는 것.)


# ### 존재 여부 (Checking Membership) (p.86)
내용이 있을 줄 알았지? 하하하!!! 안타깝게도 [이 몸]은 중급회계 시험에 후드려맞기 전, 집에서 '복습'하러 '탈주'한다!!!
안녕!!!!!
# In[ ]:




