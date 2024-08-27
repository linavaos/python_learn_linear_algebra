from numpy import matrix, zeros
from LinearAlgebra.playLA.vector import Vector


class Matrix:

    @classmethod
    def zero(cls,rowSize,colSize):
        return cls([[0]*colSize for i in range(0,rowSize)])

    def __init__(self,list2Array):
        self._values = [row[:] for row in list2Array]

    # 行列转换
    def T(self):
        result = Matrix.zero(self.shape()[1],self.shape()[0])
        for i in range(0,len(self)):
            for j in range(0,self.shape()[1]):
                result[j,i] = self._values[i][j]
        return result




    def __add__(self,other):
        return Matrix([o1+o2 for o1,o2 in zip(self.row_vector(i),other.row_vector(i))] for i in range(0,len(self)))
    

    def __sub__(self,other):
        return Matrix([o1-o2 for o1,o2 in zip(self.row_vector(i),other.row_vector(i))] for i in range(0,len(self)))
    

    def __pos__(self):
        return 1*self
    
    def __neg__(self):
        return -1*self
    

    def dot(self,other: 'Matrix'):
        assert self.shape()[1]==other.shape()[0],"self.shape()[1]="+str(self.shape()[1])+" is neq other.shape()[0]"+str(other.shape()[0])
    
        # 获得 other的列数
        other_coloum_size=other.shape()[1]
        # 取出slef的每一行和other的每一列点乘
        result = [[self.row_vector(row_index).dot(other.col_vector(coloum_index)) 
                   for coloum_index in range(other_coloum_size)] 
                  for row_index in range(len(self))]
        return Matrix(result)

        # for row_index in range(0,len(self)):
        #     row = self.row_vector(row_index)
        #     result_row  = []
        #     for colum_index in  range(0,other_coloum_size):
        #         coloum = other.col_vector(colum_index)
        #         result_row.append(row.dot(coloum))
        #     result.append(result_row)
        # return Matrix(result)
                


    # 矩阵乘以k    
    def __mul__(self,k):
        return Matrix([o1*k for o1 in self.row_vector(i)] for i in range(0,len(self)))
    
    # k乘以矩阵
    def __rmul__(self,k):
        return Matrix([o1*k for o1 in self.row_vector(i)] for i in range(0,len(self)))
    
     # 向量除以k
    def __truediv__(self,k):
        return Matrix([o1/k for o1 in self.row_vector(i)] for i in range(0,len(self)))


    def __repr__(self) -> str:
        return "Matrix({})".format(self._values)
    

    def shape(self):
        return (len(self._values),len(self._values[0]))
    

    def __len__(self):
        return len(self._values)
    
    def size(self):
        r,c = self.shape()
        return r*c
    
    def __setitem__(self,pos,value):
        r,c = pos
        self._values[r][c] = value


    
    def __getitem__(self,pos):

        r,c = pos
        return self._values[r][c]
    

    def row_vector(self,rowIndx):
        return Vector(self._values[rowIndx])
    

    def  col_vector(self,coloumIndx):
        return Vector([row[coloumIndx] for row in self._values])
    


    
    __str__=__repr__
    


    
