n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
query_name = input()
x = list(student_marks[query_name])
print(format(sum(x)/len(x)  , '.2f'))
# for i in x:
#      _sum = 0
#      _sum = _sum + i
#      print(_sum)

