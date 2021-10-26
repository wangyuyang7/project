# list 对象 alist [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]，
# 请按 alist 中元素的age 由大到小排序
alist=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
for i in range(2):
    for j in range(1,3):
        if alist[i]['age']<alist[j]['age']:
            temp=alist[i]
            alist[i]=alist[j]
            alist[j]=temp
print(alist)
# alist.sort(key=lambda x:x['age'],reverse=True)
# print(alist)
