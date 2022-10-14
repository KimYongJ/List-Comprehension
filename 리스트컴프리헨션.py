# List Comprehension : 리스트 내에서 특정 조건에 해당하는 것만 뽑아내거나 아니면 특정 조건에 해당하는 값만 바꿔서 새로운 리스트를 만들 때 사용할 수 있다.
# 문법 : new_list = [ 변수활용  for  변수  in  반복대상 if 조건 ]

##### 예시
li = [ 1,2,3,4,5 ]
new_li = [ x for x in li if x > 3 ] # 위에 선언된 리스트안에서 3보다 큰 값만 따로 빼고 싶을 때 사용
print(new_li)

# 아웃풋 : [4, 5]

##### 응용
li = [ 1,2,3,4,5 ]
new_li = [ str(x)+'입니다' for x in li if x > 3 ] # 위에 선언된 리스트안에서 3보다 큰 값만 따로 빼고 싶을 때 사용
print(new_li)

# 아웃풋 : ['4입니다', '5입니다']


# 'a'로 시작하는것만 따로 뽑아오려 할 때는 아래와 같이 작성하면 된다.
li = [ 'aa', 'ab', 'ac' , 'ba', 'bb', 'bc' ]
new_li = [ x for x in li if x.startswith('a')]
print(new_li)

# 아웃풋 : ['aa', 'ab', 'ac']


# 리스트안의 모든 글자를 대문자로 변경을 원하면 아래와 같이 작성하면 된다
li = [ 'aa', 'ab', 'ac' , 'ba', 'bb', 'bc' ]
new_li = [ x.upper() for x in li ]
print(new_li)

# 아웃풋 : ['AA', 'AB', 'AC', 'BA', 'BB', 'BC']


# 리스트안에서 마지막 글자가 'c'로 끝나는 요소 뒤에 '끝' 이라는 글자를 붙이려면 아래와 같이 작성하면 된다.
li = [ 'aa', 'ab', 'ac' , 'ba', 'bb', 'bc' ]
new_li = [ x+'끝' for x in li if x.endswith('c')]
print(new_li)

# 아웃풋 : 


