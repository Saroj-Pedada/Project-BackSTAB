def choose_sets(lst, k):
    if len(lst)==k :
        return [lst]
    if  k==0:
        return [[]]
    if k==1:
        return [[i] for i in lst]
    sub_lst1=choose_sets(lst[1:],k-1)
    for i in sub_lst1:
        i.append(lst[0])
    sub_lst2=choose_sets(lst[1:],k)
    final_lst=[]
    final_lst.extend(sub_lst1)
    final_lst.extend(sub_lst2)
    return final_lst