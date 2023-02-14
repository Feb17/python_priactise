try:
    num = int(input('输入一个整数: '))

    result = 8 / num

    print(result)

except ZeroDivisionError:
    print('除数不能为0')

except ValueError:
    print('输入错误')

# 捕获未知异常
except Exception as e:
    print(e)

else:
    print('没有异常')
finally:
    print('执行完毕')
