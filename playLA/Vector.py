class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """
        :param dim: 生成零向量的维数
        :return: 生成的零向量
        """
        return cls([0] * dim)

    def __add__(self, other):
        """
        :param other: 相加的另一个向量
        :return: 相加后的结果向量
        """
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """
        :param other: 相减的另一个向量
        :return: 相减后的结果向量
        """
        assert len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """
        :param k: 数量乘法的参数 k（Vector * k）
        :return: 数量乘法的结果向量
        """
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """
        :param k: 数量乘法的参数 k（k * Vector）
        :return: 数量乘法的结果向量
        """
        return self * k

    def __pos__(self):
        """
        :return: 向量取正的结果
        """
        return 1 * self

    def __neg__(self):
        """
        :return: 向量取负的结果
        """
        return -1 * self

    def __len__(self):
        """
        :return: 向量长度（有多少个元素）
        """
        return len(self._values)

    def __getitem__(self, index):
        """
        :param index: 获取元素的位置
        :return: 第index个位置上的元素
        """
        return self._values[index]

    def __iter__(self):
        """
        :return: 当前向量的迭代器
        """
        return self._values.__iter__()

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))