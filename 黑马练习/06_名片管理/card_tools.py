card_list = []

def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("欢迎使用【名片管理系统】 V1.0")
    print("")
    print("1. 增加名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2. 根据用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)
    # 4. 提示用户添加成功
    print("添加 %s 的名片成功" % name_str)


def show_all():
    """显示全部名片"""

    print("-" * 50)
    print("显示全部")

    # 判断是否存在名片记录 如果没有 提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片 请使用新增功能增加名片")
        # return 可以返回一个函数的执行结果
        # return 后的代码不会执行
        # 如果return后没有任何内容 将会返回到调用函数的位置 并且不会返回任何内容
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],
                                       card_dict["qq"], card_dict["email"]))


def search_card():
    """查询名片"""

    print("-" * 50)
    print("查询名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入要查找的姓名：")
    # 遍历名片列表 查询要搜索的姓名 如果没有找到 要提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"],
                                            card_dict["qq"], card_dict["email"]))
            # 针对找到的字典做修改和删除的操作
            deal_card(card_dict)
            break

    else:
        print("抱歉 没有找到%s的名片" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    action_str = input("请选择要执行的操作："
                       "[1] 修改  [2] 删除  [0] 返回上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：（回车则不修改）")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：（回车则不修改）")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq：（回车则不修改）")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：（回车则不修改）")
        print("修改名片成功")

    elif action_str == "2":
        print("删除名片")
        card_list.remove(find_dict)


def input_card_info(dict_valve, tip_message):
    """
    输入名片信息
    :param dict_valve: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容 就返回内容 否则返回字典原有的值
    """
    # 1.提示用户输入内容
    return_str = input(tip_message)
    # 2.针对用户的输入进行判断 如果用户输入了内容 直接返回结果
    if len(return_str) > 0:
        return return_str
    # 3.如果用户没有输入内容 返回字典中原本的值
    else:
        return dict_valve
