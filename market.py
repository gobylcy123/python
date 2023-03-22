# 商品列表
goods = {
    "001": {"name": "iPhone", "price": 5999},
    "002": {"name": "iPad", "price": 3999},
    "003": {"name": "Macbook", "price": 8999},
    "004": {"name": "Airpods", "price": 999}
}

# 购物车
cart = {}

# 商品管理
def show_goods():
    print("商品列表：")
    for code, item in goods.items():
        print("{:<10}{:<20}{:<10}".format(code, item["name"], item["price"]))

def add_to_cart(code, quantity):
    if code not in goods:
        print("该商品不存在，请重新输入商品编号。")
        return
    if code in cart:
        cart[code]["quantity"] += quantity
    else:
        cart[code] = {"name": goods[code]["name"], "price": goods[code]["price"], "quantity": quantity}
    print("添加成功！")

def remove_from_cart(code):
    if code not in cart:
        print("该商品未加入购物车，请重新输入商品编号。")
        return
    del cart[code]
    print("删除成功！")

def show_cart():
    if not cart:
        print("购物车为空。")
        return
    print("购物车：")
    total = 0
    for code, item in cart.items():
        subtotal = item["price"] * item["quantity"]
        print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(code, item["name"], item["price"], item["quantity"], subtotal))
        total += subtotal
    print("总计：{:>38}".format(total))

# 结算
def checkout():
    show_cart()
    while True:
        confirm = input("是否确认结算（y/n）：")
        if confirm == "y":
            print("结算成功！")
            cart.clear()
            break
        elif confirm == "n":
            print("已取消结算。")
            break
        else:
            print("无效输入，请重新输入（y/n）。")

# 主程序
print("欢迎来到购物系统！")
while True:
    print("请输入您要进行的操作：")
    print("1. 查看商品列表")
    print("2. 添加商品到购物车")
    print("3. 从购物车删除商品")
    print("4. 查看购物车")
    print("5. 结算")
    print("6. 退出系统")
    choice = input()
    if choice == "1":
        show_goods()
    elif choice == "2":
        code = input("请输入商品编号：")
        quantity = int(input("请输入购买数量："))
        add_to_cart(code, quantity)
    elif choice == "3":
        code = input("请输入商品编号：")
        remove_from_cart(code)
    elif choice == "4":
        show_cart()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("欢迎再次光临！")
        break
    else:
        print("无效输入，请重新输入。")
