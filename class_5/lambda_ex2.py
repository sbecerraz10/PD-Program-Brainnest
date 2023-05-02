li_1 = [5, 7, 22, 97, 54]
li_2 = [8,2,12,109,23]
print([(lambda a = li_1[i],b=li_2[i]: max(a, b))() for i in range(len(li_2))])
