
class_info = [{"name": "xiaoming", "age": 18, "score": 100}]


def show_cmd():
    print("-" * 50)
    print("学生管理系统 V1.0")
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示全部")
    print("6:退出系统")
    print("-" * 50)


def add_student():
    name = input("请输入学生姓名>>>:")
    age = 0
    score = 0
    try:
        age = int(input("请输入学生年龄>>>:"))
    except ValueError:
        print("请输入整数")
        return
    try:
        score = int(input("请输入学生成绩>>>:"))
    except ValueError:
        print("请输入整数")
        return
    for student in class_info:
        if student["name"] == name:
            print("已经添加过学生了 请重新选择")
            return

    student = {
        "name": name,
        "age": age,
        "score": score
    }
    class_info.append(student)
    print("添加%s成功" % student["name"])


def del_student():
    name = input("请输入要删除的学生姓名>>>:")
    for student in class_info:
        if student["name"] == name:
            class_info.remove(student)
            print("删除成功")
            return
    print("未找到该学生 请重新选择")


def amend_student():
    name = input("请输入需要修改的学生姓名>>>:")
    for student in class_info:
        if student["name"] == name:
            age = input("请输入需要修改的年龄（直接回车则不修改）>>>:")
            if len(age) > 0:
                age = int(age)
                student["age"] = age
            score = input("请输入需要修改的成绩（直接回车则不修改）>>>:")
            if len(score) > 0:
                score = int(score)
                student["score"] = score
            print("修改成功")
            return
    print("未查询到该学生 请重新输入")


def inquire_student():
    name = input("请输入需要修改的学生姓名>>>:")
    for student in class_info:
        if student["name"] == name:
            print("查询成功")
            print("%s----%d----%d" % (student["name"], student["age"], student["score"]))
            return


def show_all_student():
    if not len(class_info):
        print("还未添加任何学生 请先添加")
        return

    for student in class_info:
        print("%s----%d----%d" % (student["name"], student["age"], student["score"]))


while True:
    show_cmd()
    cmd = int(input("请输入命令(数字)，回车结束>>>:"))

    if cmd == 1:
        add_student()

    elif cmd == 2:
        del_student()

    elif cmd == 3:
        amend_student()

    elif cmd == 4:
        inquire_student()

    elif cmd == 5:
        show_all_student()

    elif cmd == 6:
        break

    else:
        print("命令输入错误 请重新输入")


print("欢迎您下次使用")
print("-" * 50)
