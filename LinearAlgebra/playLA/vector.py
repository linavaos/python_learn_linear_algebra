import math

class Vector:

    def __init__(self,list) -> None:
        self._values = list

#    类方法
    @classmethod
    def zero(cls,dim):
        # cls就是当前类、加()就是实列化啦
        return cls([0]*dim)

   # 向量模 
    def norm(self):
        return math.sqrt(sum([e*e for e in self]))    
    
    # 归一化（单位向量）
    def normalize(self):
        if self.norm()<Ellipsis:
            raise ZeroDivisionError("noraml is zero")
        return Vector([e/self.norm() for e in self])


    def __add__(self,other):
        return Vector([o1+o2 for o1,o2 in zip(self,other)])
    
    def __sub__(self,other):
        return Vector([o1-o2 for o1,o2 in zip(self,other)])
    
    # 向量*k
    def __mul__(self,k):
        # 错误，数组的乘法其实是扩容k倍
        # return Vector(self*k)
        return Vector([e * k for e in self])
    

    # 向量除以k
    def __truediv__(self,k):
        return Vector([e / k for e in self])
    
      
    # k*向量
    def __rmul__(self,k):
        return Vector([e * k for e in self])
    



    
    # 向量取正
    def __pos__(self):
        return Vector([1 * e for e in self])
    
    # 向量取负
    def __neg__(self):
        return Vector([-1 * e for e in self])
     
    


    def __iter__(self):
        return self._values.__iter__()

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