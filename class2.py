if __name__ == '__main__':
    # 新建一个列表list，逐个赋值，打印

    # 新建一个列表map，逐个赋值，打印
    map = {}
    map['name'] = "张三"
    map[2] = "男"
    map['studentNo'] = 20000565746

    for key, value in map.items():
        print("{} -> {}".format(key, value))

    for key in map.keys():
        print("{} -> {}".format(key, map.get(key)))
