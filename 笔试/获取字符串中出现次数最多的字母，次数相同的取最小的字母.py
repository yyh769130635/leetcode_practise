# -*- coding: utf-8 -*-
# @Time : 8/15/2020 4:17 PM
# @Author : Peter yang

def main():
    s = input("请输入字符串：")
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        if i not in dic:
            dic[i] = 1

    # d_order = sorted(dic.items(), key=lambda x: x[1], reverse=False)
    # res = sorted(dic.items(), key=lambda x: (x[1], x[0]), reverse=False)
    # print(res)
    num = 0
    res = "z"
    for k, v in dic.items():
        if num <= v:
            if ord(res) >= ord(k):
                num = v
                res = k
    print(res)


main()
