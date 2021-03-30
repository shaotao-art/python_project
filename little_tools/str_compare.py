class str_compare_print():
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2 = str2
        self.run()


    def _Str_compare(self):
        index_lst=[]
        length=max((len(self.str1),len(self.str2)))
        i=0
        while i < length:
            if self.str1[i]!=self.str2[i]:
                index_lst.append(i)
                #连续不同后第一个相同推出
                while  i<length and self.str1[i]!=self.str2[i] :  #当最后一个元素不同时 会出错
                    i+=1
                #连续不同后第一个相同推出  所以应该append i-1
                #但是为了后面的插入  这里就append i
                index_lst.append(i)
            else:
                i+=1
        return index_lst
    def _Output(self,index_lst,str_out):
        #为了插入改变idex_lst值
        for i in range(len(index_lst)):
            index_lst[i]+=i
        #变成list 以便进行insert操作
        str_out=list(str_out)
        #插入字符来显示高亮
        for each in index_lst:
            if index_lst.index(each)%2==0:
                str_out.insert(each,'\033[1;37;41m')
            else:
                str_out.insert(each, '\033[0m')
        res=''.join(each for each in str_out)
        print(res)
    def run(self):
        index_lst = self._Str_compare()
        self._Output(index_lst, self.str1)


str1='abcde123fg779hgh'
str2='abcde243fg888hii'

a=str_compare_print(str1,str2)





