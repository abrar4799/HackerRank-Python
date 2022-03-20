score_list = []
mark_sheet = []
for i in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        mark_sheet.append([name,score])
second_low = sorted(list(set(score_list)))[1]
for a,b in sorted(mark_sheet):
        if b==second_low:
                print(a)
# print(second_low)
#
# print(score_list)
# print(mark_sheet)
