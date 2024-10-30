global_card_list = []

def show_menu():
    """显示菜单"""

    print("*" * 50)
    print("Welcome to Business Card Management System V1.0", end="\n\n")
    print("1  Add business cards")
    print("2  Show all business cards")
    print("3  Inquire business card", end="\n\n")
    print("0  exit the system")
    print("*" * 50)


def add_business_cards():
    """增加名片"""
    print("-" * 50)
    print("Add business cards")
    name_str = input("please input name: ")
    phone_str = input("please input phone: ")
    wx_str = input("please input wx: ")
    email_str = input("please input email: ")
    card = {"name": name_str,
            "phone": phone_str,
            "wx": wx_str,
            "email": email_str}
    global_card_list.append(card)
    print("Add success")


def show_all_business_cards():
    """显示全部名片"""
    print("-" * 50)
    print("Show all business cards")
    if len(global_card_list) == 0:
        print("No business cards, Please enter new business card")
        return
    for name in ["name", "phone", "wx", "email"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card in global_card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t" % (card["name"], card["phone"],
                                          card["wx"],   card["email"]))


def inquire_business_card():
    """查询名片"""
    print("-" * 50)
    print("Inquire business card")

    name_find = input("please enter the name of the business card: ")
    for card in global_card_list:
        if card["name"] == name_find:
            print("name\t\tphone\t\twx\t\temail")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"], card["phone"],
                                            card["wx"], card["email"]))
            deal_card(card)
            break
    else:
        print("sorry don't find [%s]'s card" % name_find)


def deal_card(card_find):
    """
    处理找到的名片
    :param card_find: 查找到的名片
    :return: 无返回值
    """
    cmd = input("please enter cmd"
                "[1] amend   [2] delete    [3] backup"
                ": ")
    if cmd == "1":
        card_find["name"] = input_card_info(card_find["name"], "name:(Carriage return is not modified)")
        card_find["phone"] = input_card_info(card_find["phone"], "phone:(Carriage return is not modified)")
        card_find["wx"] = input_card_info(card_find["wx"], "wx:(Carriage return is not modified)")
        card_find["email"] = input_card_info(card_find["email"], "email:(Carriage return is not modified)")
        print("amend card info successful")
    elif cmd == "2":
        print("delete card")
        global_card_list.remove(card_find)


def input_card_info(card_value, tip_message):
    """
    输入名片信息
    :param card_value: 字典中原本的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容 就返回新内容 否则 返回字典原来的值
    """
    str = input(tip_message)
    if len(str) > 0:
        return str
    else:
        return card_value