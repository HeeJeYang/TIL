## 제어문

- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능

## 조건문

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
- 기본 형식
    - 조건에는 참/거짓에 대한 조건식
        - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 실행
        - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블록을 실행
            - else는 선택적으로 활용할 수 있음
- 중첩 조건문
    - 조건문은 다른 조건문에 중첩되어 사용될 수 있음
        - 들여쓰기에 유의하여 작성할 것
        
- 조건 표현식
    - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
    - 삼항 연산자로 부르기도 함
    

## 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- while문
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
    - 조건식이 참인 경우 반복적으로 코드를 실행
        - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
        - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
        - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요
- for문
    - 반복가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)
- 반복 제어
    - break, continue, for-else
- 복합연산자
    - 복합 연산자는 연산과 할당을 합쳐 놓은 것
        - 예시) 반복문을 통해서 개수를 카운트 하는 경우

## for문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iteravle)의 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
- Iterable
    - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
    - 순회형 함수(enumerate)
- **추가 메서드를 활용한 딕셔너리(Dictionary) 순회**
    - keys() : Key로 구성된 결과
    - values(): value로 구성된 결과
    - items() : (Key, value)의 튜플로 구성된 결과
    - enumerate 순회
        - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
            - (index, value) 형태의 tuple로 구성된 열거 객체를 반환
- **List Comprehension**
    - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
    
    ```python
    [code for 변수 in iterable]
    
    [code for 변수 in iterable if 조건식]
    ```
    
- Dictionary Comprehension
    - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
    
    ```python
    {key: value for 변수 in iterable}
    
    {key: value for 변수 in iterable if 조건식}
    ```
    
- **반복문 제어**
    - break
        - 반복문을 종료
    - continue
        - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    - for-else
        - 끝까지 반복문을 실행한 이후에 else 문 실행
            - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음
    - pass
        - 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)
        

## 함수

- 함수의 종류
    - 내장 함수
        - 파이썬에 기본적으로 포함된 함수
    - 외장함수
        - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    - 사용자 정의 함수
        - 직접 사용자가 만드는 함수
- 사용 이유
    - 분해(Decomposition) : 기능 분해, 재사용 가능
    - 추상화(Abstraction) : 복잡한 내용을 몰라도 사용 가능, 재사용성과 가독성, 생산성
    
- 함수의 정의
    - 특정한 기능을 하는 코드의 조각(묶음)
    - 특정 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용
    
    ```python
    def function_name(parameter):
        # code block
        return returning_value
    ```
    
- 함수 기본 구조
    - 선언과 호출(define & call)
    - 입력(Input)
    - 문서화(Docstring)
    - 범위(Scope)
    - 결과값(Output)
- 선언과 호출(define & call)
    - 함수의 선언은 def 키워드를 활용함
    - 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함

- 함수의 결과값(Output)
    - 값에 따른 함수의 종류
        - Void function
            - 명시적인 return 값이 없는 경우, None을 반환하고 종료
        - Value returning function
            - 함수 실행 후, return 문을 통해 값 반환
            - return을 하게 되면, 값 반환 후 함수가 바로 종료
- **print vs return**
    - print 함수와 return의 차이점
        - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
        - 데이터 처리를 위해서는 return 사용
    - REPL(Read-Eval-Print Loop) 환경(Jupiter 등)에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 같은 동작을 하는 것으로 착각할 수 있음
- 두 개 이상의 값 반환
    - Tuple 활용 (return x, y)
    
- **파라미터 : 함수를 정의할 때, 함수 내부에서 사용되는 변수**
- **Argument : 함수를 호출할 때, 넣어주는 값**
    - 소괄호 안에 할당 func_name(argument)
        - 필수 Argument : 반드시 전달되어야 하는 argument
        - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달
- Positional Arguments
    - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
- Keyword Arguments
    - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
    - Keyword Argument 다음에 Positional Argument를 활용할 수 없음
    
    ```python
    def add (x, y):
        return x + y
    
    add(x=2, y=5)
    add(2, y=5)
    add(x=2, 5) => Error 발생
    ```
    
- Default Arguments Values
    - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
        - 정의된 것보다 더 적은 개수의 argument 들로 호출될 수 있음
        
        ```python
        def add(x, y = 0):
            return x + y
        ```
        
    
- 정해지지 않은 여러 개의 Arguments 처리
    - 애스터리스트(Asterisk) 혹은 언패킹 연산자라고 불리는 * 이용
    - 가변 인자(*args)
        - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    - 몇 개의 Positional Argument를 받을 지 모르는 함수를 정의할 때 유용
- 패킹 / 언패킹
    - 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야 함
    - 패킹
        - 여러 개의 데이터를 묶어서 변수에 할당하는 것
        
        ```python
        numbers = (1, 2, 3, 4, 5) # 패킹
        print(numbers) # (1, 2, 3, 4, 5)
        ```
        
    - 언패킹
        - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
        - 언패킹 시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
        - 언패킹 시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 **리스트**에 담을 수 있음
        
        ```python
        numbers = (1, 2, 3, 4, 5)
        a, b, c, d, e = numbers # 언패킹
        print(a, b, c, d, e) # 1 2 3 4 5
        ```
        
- Asterisk(*)와 가변 인자
    - *는 스퀸스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
        - 주로 튜플이나 리스트를 언패킹하는데 사용
        - *를 활용하여 가변 인자를 만들 수 있음
            - 가변 인자 예시
            
            ```python
            def sum_all(*numbers):
                result = 0
                for number in numbers:
                    result += number
                return result
            
            print(sum_all(1, 2, 3)) # 6
            print(sum_all(1, 2, 3, 4, 5, 6)) # 21
            ```
            
- 가변 인자 예시
    - 반드시 받아야 하는 인자와, 추가적인 인자를 구분해서 사용할 수 있음
    
    ```python
    def print_family_name(father, mother ,*pets):
        print(f"아버지 : {father}")
        print(f"어머니 : {mother}")
        print("반려동물들..")
        for name in pets:
            print(f"반려동물 : {name}")
    
    print_family_name("아부지", "어무니", "멍멍이", "냥냥이")
    ```
    

- 가변 키워드 인자(**kwargs)
    - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
    - **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
    
    ```python
    def family(**kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)
    family(father='아부지', mother='어무니', baby='아기')
    
    # father : 아부지
    # mother : 어무니
    # baby : 아기
    ```
    

- **가변 인자(*args)와 가변 키워드 인자(***kwargs) 동시 사용 가능**

- Python의 범위(Scope)
    - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
    - scope
        - global scope : 코드 어디에서든 참조할 수 있는 공간
        - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
    - variable
        - global variable : global scope에 정의된 변수
        - local variable : local scope에 정의된 변수
        - 
- 변수 수명주기(lifecycle)
    - 변수는 각자의 수명주기(lifecycle)가 존재
        - built-in scope
            - 파이썬이 실행된 이후부터 영원히 유지
        - global scope
            - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
        - local scope
            - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    
- 이름 검색 규칙(Name Resolution)
    - 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
    - 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
        - Local scope : 지역 범위(현재 작업 중인 범위)
        - Enclosed scope : 지역 범위 한 단계 위 범위
        - Global scope : 최상단에 위치한 범위
        - Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
            - ex) print()
    - **함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음**
- global 문
    - 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
        - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
        - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global 예시
    
    ```python
    # 함수 내부에서 글로벌 변수 변경하기
    a = 10
    def func1():
        global a
        a = 3
    
    print(a) # 10
    func1()
    print(a) # 3
    ```
    
- nonlocal
    - global을 제외하고 가장 가까운 (둘러싸고 있는) scope의 변수를 연결하도록 함
        - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
        - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
    - global과는 달리 이미 존재하는 이름과의 연결만 가능함
    
- **함수의 범위 주의**
    - 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료 시 사라짐
    - 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
        - 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
        - 값을 할당하는 경우 해당 scope의 이름공간에 새롭게 생성되기 때문
        - **단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것**
    - 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
        - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생
        - 가급적 사용되지 않는 것을 권장하며, **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천**

- 내장 함수(Built-in Functions)
    - 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음
    - `**map(function, iterable)**`
        - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 map object로 반환
    - `**filter(function, iterable)**`
        - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과가 True인 것들을 filter object로 반환
    - `**zip(*iterables)**`
        - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
    - `lambda[parameter]` : lambda 함수 표현식
        - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
        - return 문을 가질 수 없고, 간편 조건문 외 조건문이나 반복문을 가질 수 없음
        - 함수를 정의해서 사용하는 것보다 간결하게 사용이 가능하고, def를 사용할 수 없는 곳에서도 사용이 가능하다
- 재귀 함수 주의 사항
    - 재귀 함수는 base case에 도달할 때까지 함수를 호출함
    - 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
    - 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Error 발생
- 반복문과 재귀 함수 비교
    - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함.
    - 재귀 호출은 변수 사용을 줄여줄 수 있음
    - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림

## 모듈과 패키지

- 합, 평균, 표준편차, … 자주 쓰는 기능들
- 다양한 기능을 하나의 파일로(모듈, module)
- 다양한 파일을 하나의 폴더로(패키지, package)
- 다양한 패키지를 하나의 묶음으로(라이브러리, library)
- 이것을 관리하는 관리자(pip)
- 패키지의 활용 공간(가상환경)

- **모듈**
    - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- **패키지**
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함

- 모듈과 패키지 불러오기
    
    ```python
    import module
    from module import var, function, Class
    from module import *
    
    from package import module
    from package.module import var, function, Class
    ```
    

- 파이썬 패키지 관리자(pip)


## 요청과 응답

- API(Application Programming Interface) : 두 소프트웨어가 서로 통신할 수 있도록 연결 시켜주는 인터페이스
- 클라이언트와 서버의 접점 : 인터페이스
- pip install : 파이썬에서 필요한 모듈을 다운받을 때 사용하는 명령어
- XML이라고 하는 데이터 집합을 받아서 사용

## 가상환경(virtual environment)

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 과거 외주 프로젝트 - djange 버전 2.x
    - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어
- 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 버전 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음