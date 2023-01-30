class A:

    def test(self):
        print("test 方法")


class B:

    def demo(self):
        print("demo 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()
c.demo()
c.test()

# 确定C类对象调用父类方法的顺序
"""method resolution order"""
print(C.__mro__)
