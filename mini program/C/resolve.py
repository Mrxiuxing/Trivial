"""
某些整数能分解成若干个连续整数的和的形式，例如
15 = 1 + 2 + 3 + 4 + 5 
15 = 4 + 5 + 6
15 = 7 + 8 
某些整数不能分解为连续整数的和，例如:16 
输入: 一个整数N(N <= 10000)
输出:整数N对应的所有分解组合，按照每个分解中的最小整数
从小到大输出，每个分解占一行 ，每个数字之间有一个空格(每
行最后保留一个空格);如果没有任何分解组合，则输出NONE

上面的15 可以拆成 3*5 和 5*3，对于奇数还有特殊解，14/2+16/2
所以可以将目标数num改写成a*b，这里将a理解成中间数，b理解成项数，比如15=5*3，5 就是中间数 3 就是项数，结果就是（5-3//2）+ 5 + （5+3//2）
这有个前提，就是项数是奇数，如果项数是偶数的话，比如125*8，那就改写成（62+63）*8
"""


def func_resolve(num):
    n = int(num ** 0.5)
    # 这里直接开根号，缩小循环范围
    res = []
    # 研究规律发现除了15=7+8 这种两项的，其他都是多项
    # 可以转化成中间项的倍数，所以下面for循环求得是中间项的值
    for i in range(2, n + 1):
        if num % i == 0:
            mid_01 = i  # 中间数
            mid_02 = int(num / i)  # 项数
            # 分解出来为mid_01*mid_02的形式，
            if mid_02 % 2 == 1:  # mid_02为奇数
                first_1 = (mid_01 - mid_02 // 2)
                last_1 = (mid_01 + mid_02 // 2)
                if first_1 >= 0:
                    res.append('+'.join([str(j) for j in range(first_1, last_1 + 1) if j > 0]))
            else:  # mid_02 为偶数，拆分mid_01 比如：125拆成62+63
                if mid_01 % 2 == 1:
                    t_01 = int((mid_01 - 1) / 2)
                    t_02 = int((mid_01 + 1) / 2)
                    if t_01 - mid_02 >= 0:
                        lists_01 = [str(i) for i in range(t_01 - mid_02 + 1, t_01 + 1) if i > 0]
                        lists_02 = [str(i) for i in range(t_02, t_02 + mid_02) if i > 0]
                        res.append('+'.join(lists_01 + lists_02))
            # 此处仅仅将上面的mid_01*mid_02 调换成mid_02*mid_01 中间值和项数对调
            if mid_01 % 2 == 1:
                first_2 = (mid_02 - mid_01 // 2)
                last_2 = (mid_02 + mid_01 // 2)

                if first_2 >= 0:
                    res.append('+'.join([str(j) for j in range(first_2, last_2 + 1) if j > 0]))
            else:  # mid_02 为偶数，拆分mid_01:125拆成62+63
                if mid_02 % 2 == 1:
                    t_01 = int((mid_02 - 1) / 2)
                    t_02 = int((mid_02 + 1) / 2)
                    if t_01 - mid_01 >= 0:
                        lists_01 = [str(i) for i in range(t_01 - mid_01 + 1, t_01 + 1) if i > 0]
                        lists_02 = [str(i) for i in range(t_02, t_02 + mid_01) if i > 0]
                        res.append('+'.join(lists_01 + lists_02))
    # 上面要防止第一项等于0
    # 奇数特殊解
    if num % 2 == 1:
        mid = int((num + 1) / 2)
        res.append('+'.join([str(mid - 1), str(mid)]))
    if res:
        return set(res)  # 去除重复结果
    else:
        return [None]


res = func_resolve(int(input("请输入一个整数N(N<=10000):")))
for i in res:
    if i:
        print(i)
    else:
        print(None)
