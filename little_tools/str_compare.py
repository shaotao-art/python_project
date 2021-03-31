class str_compare_print():
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2 = str2
        self.length1=len(str1)
        self.length2= len(str2)
        self.duode_part=self._get_duode_part()
        self.run()

        #获取长度更大的字符串的多的部分
    def _get_duode_part(self):
        if self.length1>self.length2:
            duode_part=self.str1[self.length2:]
        else:
            duode_part = self.str2[self.length1:]
        return duode_part


        #比较字符串并且记录不同字符处的索引
    def _Str_compare(self):
        index_lst=[]
        length=min((len(self.str1),len(self.str2)))
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

    #根据索引对字符串进行更新  并将不同部分高亮输出
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
        str_out.append('\033[1;37;41m')
        str_out.append(self.duode_part)
        str_out.append('\033[0m')
        res=''.join(each for each in str_out)
        print(res)

    def run(self):
        index_lst = self._Str_compare()
        self._Output(index_lst, self.str1)


str1='https://s.taobao.com/search?spm=a21bo.21814703.201856-fline.2.5af911d9BrSph5&q=%E5%9B%9B%E4%BB%B6%E5%A5%97&refpid=420461_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f67&bcoffset=0&p4ppushleft=3%2C44&s=88'
str2='https://s.taobao.com/search?spm=a21bo.21814703.201856-fline.2.5af911d9BrSph5&q=%E5%9B%9B%E4%BB%B6%E5%A5%97&refpid=420461_1006&source=tbsy&style=grid&tab=all&pvid=d0f2ec2810bcec0d5a16d5283ce59f67&bcoffset=0&p4ppushleft=3%2C44&sort=credit-desc'

a=str_compare_print(str1,str2)





