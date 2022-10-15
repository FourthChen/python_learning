# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 21:44
# @Author  : sihao
# @File    : 02-替换空格.py
"""

请实现一个函数，
将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
"""
# def replace_space(s):
#     s_=''
#     for i in s:
#         if i==' ':
#             s_=s_+'%20'
#         else:
#             s_=s_+i
#     return s_
#
# def main():
#     s="We are family"
#     print(s)
#     print(replace_space(s))
#
# if __name__=='__main__':
#     main()

nums = [1, 7, 3, 6, 5, 6]


class Solution:
    def pivotIndex(self, nums):
        sum = 0
        for i in nums:
            sum += i
        sum1 = 0
        for i in range(1,len(nums)):
            sum1 += nums[i-1]

            if sum1 * 2 + nums[i ] == sum:
                print(i)
        else:
            return -1

a=Solution()
a.pivotIndex(nums)