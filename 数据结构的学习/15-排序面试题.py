# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 09:32
# @Author  : sihao
# @File    : 15-排序面试题.py
'''
1.给定两个字符串s和t，判断t是否为s的重新排列
例如：s='rat',t='car',return false.
'''
class solution:
    def isAnagram(self,s,t):
        '''
        先排序，再判断
        :param s: str
        :param t: str
        :return: bool
        '''
        ss=list(s)
        tt=list(t)
        ss.sort()
        tt.sort()
        return ss==tt

class solution:
    def isAnagram(self,s,t):
        '''
        先统计字母个数，再判断
        :param s: str
        :param t: str
        :return: bool
        '''
        dict1={}
        dict2={}
        for ch in s:
            dict1[ch]=dict1.get(ch,0)+1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        return s==t

'''
2.给定一个m*n的二维列表，查找一个数是否存在
'''
class solution:
    def searchMatrix(self,matrix,target):
        '''

        :param matrix:
        :param target:
        :return:
        '''
        for line in matrix:
            if target in line:
                return True
        return False

'''
3.给定一个列表和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数
例如：列表[1,2,5,4]与目标整数3，1+2=3，结果为（0，1）
'''
class solution:
    def twoSum(self,nums,target):
        '''

        :param nums: list
        :param target: int
        :return: list
        '''
        n=len(nums)
        for i in range(n):
            for j in range(n-i,n):
                if nums[i]+nums[j]==target:
                    return sorted([i,j])
