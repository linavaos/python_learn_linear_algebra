class Vector:
    def __init__(self,list) -> None:
        self._values = list

    def __getItem__(self,index):
        return self._values[index]


    def __len__(self):
        return len(self._values)

    # python中用于返回对象字符串形式
    #  更加正式，适用于开发和调试
    #  比如debug的时候
    def __repr__(self) -> str:
        return "Vector({})".format(self._values)
    
    # python中用于返回对象字符串形式
    # 更加非正式，适用于用户。通常print调用这个
    # 如果没有__str__则会调用__repr__
    def __str__(self) -> str:
        return "({})".format(",".join(str(e) for e in self._values))