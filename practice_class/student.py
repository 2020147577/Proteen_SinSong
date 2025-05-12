# 실습 2: class Student
from contextlib import nullcontext


class Student:
    def __init__(self, name, student_id, major):
        # 속성 (attribute)
        self.name = name
        self.__student_id = student_id  # private 속성
        self.major = major
        '''
        TODO: 새로운 속성 만들기
        grade: 본인의 학년
        gpa: 본인의 내신 등급(외부에서 접근이 안되도록 접근 제어자로 설정)
        (HINT: self를 이용해서 설정한 속성을 nullcontext 로 설정)
        e.g) self.{속성이름} = nullcontext
        '''

    '''
    TODO: 새로운 생성자 만들기
    이번 생성자는 name, student_id, major 뿐만 아니라
    새로 추가된 grade gpa 등도 모두 받을 수 있도록 제작.
    e.g)
    def __init__(self, ...):
        self.gpa = ...
        ...
    주의할 점: 새로운 생성자는 위에 있는 기존 생성자와 받는 인자(argument)들과 완벽히 일치하면 안됨!
    '''

    # 메서드 (method)
    def introduce(self):
        print(f"안녕하세요, 저는 {self.major} 전공의 {self.name}입니다.")

    def study(self, subject):
        print(f"{self.name}이(가) {subject}를 공부합니다.")

    '''
    TODO: 새로운 메서드 만들기 1
    본인의 학년을 출력하는 메서드를 제작.
    위 introduce, study와 유사하게 print를 이용해서 출력!
    e.g)
    def get_grade(self):
        print(...)
        
    실행 예시) 태륭이(가)는 4학년 학생입니다.
    '''

    '''
    TODO 새로운 메서드 만들기 2
    gpa는 접근 제어자로 설정되어서 외부에서 직접 접근이 불가능하므로
    외부에서 gpa정보를 얻을 수 있는 메서드를 제작
    e.g)
    def get_gpa(self):
        print(...)

    실행 예시) 제 gpa는 XXX입니다.
    '''

    '''
    TODO: 새로운 메서드 만들기 3
    본인의 gpa를 수정하는 메서드를 제작
    인자로 gpa를 받아서 속성을 수정할 수 있도록 한다
    e.g)
    def set_gpa(self, gpa):
        ...
    '''


s1 = Student("태륭", "2020147577", "컴퓨터과학")
s1.introduce()
# 출력: 안녕하세요, 저는 컴퓨터과학 전공의 태륭입니다.

'''
TODO: 새로운 객체 만들기
각자의 이름과 학번, 희망하는 학과로 학생 객체를 생성해보기.
s2 = Student(...)
'''

'''
TODO: 객체 내부에 있는 속성을 그냥 출력해보기
(HINT: print를 사용해서 name, major 등을 출력)
-> 접근 제한자로 설정된 속성은 출력할 수 없어야 한다!
'''

'''
TODO: 객체의 메서드를 호출해보기
위 s1.introduce()의 예시와 같이 제대로 메서드가 제작되었는지 확인해보기 위해 출력하기
'''

