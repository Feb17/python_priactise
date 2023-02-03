class MusicPlayer(object):
    instance = None
    init_flag = False
    """ 单例模式 """

    def __init__(self):
        if not MusicPlayer.init_flag:
            print("MusicPlayer init")
            MusicPlayer.init_flag = True

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if not cls.instance:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super(MusicPlayer, cls).__new__(cls)
        # 返回当前类的实例
        return cls.instance


# create 3 instances of MusicPlayer class, print memory address of each class instance
player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)
