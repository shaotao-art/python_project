'''
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。


'''
'''
参数：原矩阵
     重塑矩阵行与列
     
1判断能否重构 数据数量判断
2能重构  如何变成新数组
'''
class Solution:
    def matrixReshape(self, nums, r: int, c: int) :
        old_row=len(nums)
        old_col = len(nums[0])
        sum=old_row*old_col
        ans=[[]*r]
        if sum != r*c:
            return nums
        else:
            for i in range(old_col):
                for j in range(old_row):
                    for x in range(c):
                        for y in range(r):
                            ans[x].append(nums[i][j])
            return ans


nums = [[1,2],[3,4]]
a=Solution()
a_a=a.matrixReshape(nums,1,4)
for i in range(len(a_a)):
    for j in range(len(a_a[0])):
        print(nums[i][j])


# nums = [[1,2],[3,4]]
# old_row=len(nums)
# old_col=len(nums[0])
# for i in range(old_col):
#     for j in range(old_row):
#         print(nums[i][j])