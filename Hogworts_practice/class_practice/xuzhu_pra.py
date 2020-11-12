from Hogworts_practice.class_practice.tonglao import TongLao


class XuZhu(TongLao):

    def read(self):
        print("罪过罪过")


if __name__ == "__main__":
    xuzhu = XuZhu(100)
    xuzhu.read()