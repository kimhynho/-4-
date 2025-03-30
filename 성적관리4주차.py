students = []


def input_scores():
    student_id = input("학번: ")
    name = input("이름: ")
    english = int(input("영어 점수: "))
    c_language = int(input("C-언어 점수: "))
    python = int(input("파이썬 점수: "))
    total = english + c_language + python
    avg = total / 3
    grade = calculate_grade(avg)
    students.append({
        "학번": student_id, "이름": name, "영어": english, "C-언어": c_language, "파이썬": python,
        "총점": total, "평균": avg, "학점": grade, "등수": 0
    })


def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def calculate_ranks():
    total_scores = [student['총점']  for student in students]  # 총점만 추출
    sorted_scores = sorted(total_scores, reverse=True)  # 총점을 내림차순 정렬

    for student in students:
        student['등수'] = sorted_scores.index(student['총점']) + 1  # 원래 리스트 순서 유지하며 등수 할당

    print("등수별 학생 목록:")
    for student in students:
        print(f"{student['등수']}등: {student['이름']}")


def print_scores():
    print("학번", "이름", "영어", "C-언어", "파이썬", "총점", "평균", "학점", "등수", sep='\t')
    for student in students:
        print(student['학번'], student['이름'], student['영어'], student['C-언어'], student['파이썬'],
              student['총점'], f"{student['평균']:.2f}", student['학점'], student['등수'], sep='\t')


def delete_score():
    student_id = input("삭제할 학생의 학번: ")
    global students
    for i, student in enumerate(students):
        if student['학번'] == student_id:
            del students[i]
            print(f"학번 {student_id} 학생의 성적이 삭제되었습니다.")
            return
    print("해당 학번을 찾을 수 없습니다.")


def search_student():
    search_key = input("학번 또는 이름을 입력하세요: ")
    for student in students:
        if student['학번'] == search_key or student['이름'] == search_key:
            print(student)
            return
    print("학생을 찾을 수 없습니다.")


def sort_by_total():
    students.sort(key=lambda x: x['총점'], reverse=True)
    print_scores()


def count_above_80():
    count = sum(1 for student in students if student['평균'] >= 80)
    print(f"80점 이상 학생 수: {count}")


def main():
    while True:
        print("1. 성적 입력\n2. 성적 출력\n3. 등수 계산\n4. 성적 삭제\n5. 성적 탐색\n6. 총점 정렬\n7. 80점 이상 학생 수\n8. 종료")
        choice = (input("메뉴를 선택하세요: "))
        if choice == '1':
            input_scores()
        elif choice == '2':
            print_scores()
        elif choice == '3':
            calculate_ranks()
        elif choice == '4':
            delete_score()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_by_total()
        elif choice == '7':
            count_above_80()
        elif choice == '8':
            break
        else:
            print("올바른 선택이 아닙니다.")


if __name__ == "__main__":
    main()
