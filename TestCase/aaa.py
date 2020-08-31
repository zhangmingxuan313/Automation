import re
import sys

class Solution(object):
    def __init__(self):
        print("Please input digits from 0 to 99(then press enter key):")
        self.digits=input()
        
        while re.fullmatch("[1-9][0-9]?|[0]", self.digits) is None:
            print("Illegal input! Only 0-99 digits can be entered. Please re-enter:")
            self.digits = input()

        letters=self.letterCombinations(self.digits)
        res=""
        for i in letters:
             res=res+i+" "
        print("The letters combinations of '%s' are：%s" %(self.digits,res))

    def letterCombinations(self,digits):
        # 创建字母对应的字符列表的字典
        dic = {0: [''],
               1: [''],
               2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z']
               }
        # 存储结果的数组
        ret_str = []
        if len(digits) == 0:
            return []
        # 递归出口，当递归到最后一个数的时候result拿到结果进行for循环遍历
        if len(digits) == 1:
            return dic[int(digits[0])]
        # 递归调用
        result = self.letterCombinations(digits[1:])
        # result是一个数组列表，遍历后字符串操作，加入列表
        for j in dic[int(digits[0])]:
            for r in result:
                ret_str.append(j + r)
        return ret_str


if __name__ == '__main__':
    Solution()

