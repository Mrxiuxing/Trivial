import re


def str_search(str1, str2):
    for i in str1.split():  # 将第一个字符串以空格作为分隔符进行切割
        result = re.search(r'{}'.format(i), str2, re.I)  # 循环取出并作为正则匹配规则进行匹配
        if result:  # 如果存在返回结果，不存在返回None
            return result.group()


s = "This is C programming text"
t = "This is a text for C programming"

# s = input("请输入字符串s：")
# t = input("请输入字符串t：")


res = str_search(s, t)
print(res)
