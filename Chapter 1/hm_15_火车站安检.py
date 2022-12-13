has_ticket = True

if has_ticket:
    print("车票检查通过，进站安检")
    knife_length = int(input("刀的长度："))
    if knife_length > 20:
        print("刀的长度为%d公分，禁止上车" % knife_length)
    else:   # elif knife_length <= 20:
        print("符合标准，安检通过")
else:
    print("请先购买车票")
