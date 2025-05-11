class Student:
    def __init__(self, name, student_id, major):
        # 속성 (attribute)
        self.name = name
        self.__student_id = student_id  # private 속성
        self.major = major

    # 메서드 (method)
    def introduce(self):
        print(f"안녕하세요, 저는 {self.major} 전공의 {self.name}입니다.")

    def study(self, subject):
        print(f"{self.name}이(가) {subject}를 공부합니다.")


s1 = Student("태륭", "2020147577", "컴퓨터과학")
s1.introduce()
# 출력: 안녕하세요, 저는 컴퓨터과학 전공의 태륭입니다.

