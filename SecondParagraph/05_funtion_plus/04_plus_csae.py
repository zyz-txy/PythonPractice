#递归调用函数:函数在函数体内调用自身
#案例1：计算n的阶乘
def factorial(n):
    """
    计算n的阶乘
    :param n: 阶乘的参数
    :return: 阶乘结果
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#-------------------------------------------------------

#案例2：电商订单计算器

def calc_order_cost(*args , coupon = 0 , score = 0 , express):
    """
    计算订单总金额
    :param args:商品信息
    :param coupon:优惠券
    :param score:积分
    :param express:运费
    :return:订单总金额
    """
    #订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    total_price = sum([goods[1] * goods[2] for goods in args])
    total_cost = total_price
    #优惠券
    if total_price >= 5000 and coupon <= total_price:
        total_cost -= coupon
    #积分
    if total_price >= 5000 and score // 100 <= total_price:
        total_cost -= score // 100
    #运费
    total_cost += express
    return total_cost
print(calc_order_cost(("商品1",1000,2),("商品2",3000,1),coupon=500,score=1000,express=100))
print(calc_order_cost(("商品1",1000,2),("商品2",3000,1),express=100))







