ZhangSan = {"name": "张三",
            "qq": "12345",
            "phone": "10086"}

LiSi = {"name": "李四",
        "qq": "54321",
        "phone": "10000"}

"""
card_list = [{"name": "张三",
              "qq": "12345",
              "phone": "10086"},
             {"name": "李四",
              "qq": "54321",
              "phone": "10000"}]
"""

card_list = [ZhangSan, LiSi]

for card_info in card_list:
    print(card_info)
