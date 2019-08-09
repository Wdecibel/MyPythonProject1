#__author__: Han
#__date__: 2018/11/12

        # 购物车程序
        #     salary = 5000
        #
        #     1. iphone  5800
        #     2. mac book 9000
        #     3. coffee   32
        #     4. python book  80
        #     5. bicycle      1500
        #     >>> :1
        #         余额不足，差XXX钱
        #     >>> :5
        #         已加入bicycle到你的购物车，当前余额：3500
        #     >>>:quit
        #     您已购买以下商品
        #     bicycle  1500
        #     coffee   32
        #
        #     您的余额为：2970
        #     欢迎下次光临

salary = int(input("salary:"))

product = ["iphone", "macbook", "coffee", "python book", "bicycle"]
price = [5800, 9000, 32, 80, 1500]
product1 = []
price1 = []

while True:
    a = input("your choice")
    if a[1:] ==quit:

      index = int(a[1:])
    if index  != "quit":
        if salary >= price[index-1]:
            product1.append(product[index-1])
            price1.append(price[index-1])
            salary = salary - price[index-1]
            print("已加入%s到你的购物车，当前余额%d" %(product[index-1], salary ))
        else:
    else:
        print("您已购买以下商品")
        for i in range(len(product1)+1):
            print(product1[i], end = " ")
            print(price1[i])
            print("您的余额为%d" % salary)
            print("欢迎下次光临")


