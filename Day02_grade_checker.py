name = "Shane"
age = 19
gpa_target = 3.5
is_ece_student = True

print(type(name))
print(type(age))
print(type(gpa_target))
print(type(is_ece_student))

name = input("请输入你的名字：")
major = input("请输入你的专业：")
score = float(input("请输入你的分数"))
print(f"你好，{name}！")
print(f"你的专业是：{major}")


if score >= 90:
    print("优秀")
elif score >= 80:
    print("建议继续准备电子竞赛或数模选拔。")
else:
    print("先巩固基础课程和 Python。")

print(f"{name}，你的成绩是 {score}")