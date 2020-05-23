if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student_scores = student_marks[query_name]
    sum_of_scores = float()
    for marks in student_scores:
        sum_of_scores += marks

    average = sum_of_scores / len(student_scores)
    print("{:.2f}".format(round(average, 2)))
