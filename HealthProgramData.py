import statistics as st
class stdinfo:
    def __init__(self,agelst,heightlst,weightlst):
        self.agelst = agelst
        self.heightlst = heightlst
        self.weightlst = weightlst
        pass
    def age(self):
        age_info = []
        agelst1 = self.agelst.split()
        for j in range (0, len(agelst1)):
            agelst1[j] = int(agelst1[j])
        age_info.append(agelst1)

        return age_info

    def height(self):
        height_info = []
        heightlst1 = self.heightlst.split()
        for j in range (0, len(heightlst1)):
            heightlst1[j] = int(heightlst1[j])
        height_info.append(heightlst1)
        return height_info


    def weight(self):
        weight_info = []
        weightlst1 = self.weightlst.split()
        for j in range (0, len(weightlst1)):
            weightlst1[j] = int(weightlst1[j])
        weight_info.append(weightlst1)
        return weight_info

    
    
class mean_calc(stdinfo):
    def age(self):
        age_mean = st.mean(stdinfo.age())        
        return age_mean        
    def height(self):
        height_mean = st.mean(stdinfo.height())        
        return height_mean
    def weight(self):
        weight_mean = st.mean(stdinfo.weight())        
        return weight_mean    
    
    
    
groups = []
for i in (0,1):
    group_lst = []
    num = int(input())

    group_info = stdinfo(str(input()),str(input()),str(input()))
    group_lst.extend(group_info.age())
    group_lst.extend(group_info.height())
    group_lst.extend(group_info.weight())
    groups.append(group_lst)
mean_lst = []
for i in groups:
    for j in i:
        mean_lst.append(st.mean(j))
for item in mean_lst: 
    print(float(item))
if mean_lst[0] > mean_lst[3]:
    print('A')
elif mean_lst[0] < mean_lst[3]:
    print('B')
elif mean_lst[0] == mean_lst[3]:
    if mean_lst[1] > mean_lst[4]:
        print('A')
    elif mean_lst[1] < mean_lst[4]:
        print('B')
    elif mean_lst[1] == mean_lst[4]:
        if mean_lst[2] > mean_lst[5]:
            print('A')
        elif mean_lst[2] < mean_lst[5]:
            print('B')
        elif mean_lst[2] == mean_lst[5]:
            print('Same')
