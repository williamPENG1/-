def count_number(list,count):#算出从两侧到第一个最大值的存储油量
    try:
        a = 0
        flag = 0
        max_index = list.index(max(list))
        for i in range(max_index):
            for j in range(i+1,max_index):
                if list[i]>list[j]:
                    count+=list[i]-list[j]
                else:
                    i = j + 1
                    continue
                a+=1
                if j == max_index-1:
                    flag = 1
            if flag == 1:
                break
        print (a)
        return count
    except:
        return 0

def judge_listlen(list):
    max22 = max(list)
    max_list = []
    for i in range(len(list)):
        if list[i] == max22:
            max_list.append(i)
    return max_list

#list = [1,2,3,4,1,2,2,0,1,0,12,0,1,2,2,3,0,0]
#list = [0,2,1,3,0,2,4,2,3,0,4]
list = eval(input("input:"))
print (list)
count = 0
max_list = judge_listlen(list)#计算最大值的下标数组
count = count_number(list,count)+count_number(list[::-1],count)
if len(max_list)<=1:#如果最大值小于等于1
    count = count
else:#最大值有两个或更多
    re_max_list = [max_list[0],max_list[len(max_list)-1]]#距离最远的两个下标
    count+= (re_max_list[1]-re_max_list[0]-1)*max(list)-sum(list[re_max_list[0]+1:re_max_list[1]-1])#两个下标之间的存油量
print (count)
