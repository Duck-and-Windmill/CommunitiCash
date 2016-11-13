from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

usersUnclustered = np.genfromtxt('usersUnclustered.csv',dtype=None, delimiter = ';')

trainData = scale([[X[7],X[8],X[9],X[10]] for X in usersUnclustered])
KMeans = KMeans(n_clusters =8).fit(trainData)


proximityCluster=KMeans.predict(trainData)

numGroups = 200000/20
numAssigned = [0]*8

numInGroup = [0]*numGroups

groupIDS = [0]*len(proximityCluster)
for i in range(len(usersUnclustered)):
        groupid = numAssigned[proximityCluster[i]]%numGroups
        numAssigned[proximityCluster[i]]+=1

        while numInGroup[groupid]>=20: #sets limit on group size
                groupid+=1
        numInGroup[groupid]+=1
        groupIDS[i]=groupid


plt.scatter(trainData[:,0],trainData[:,1],alpha=.5)
plt.title('Plain Data')
plt.show()

plt.scatter(trainData[:,0],trainData[:,1],c=proximityCluster,alpha=.5)
plt.title('Clustered Data')
plt.show()

plt.scatter(trainData[:,0],trainData[:,1],c=groupIDS,alpha=.5)
plt.title('Diverse Groups Data')
plt.show()
'''

sum0 = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0

for person in proximityCluster:
        if person==0:
                sum0+=1
        if person==1:
                sum1+=1
        if person==2:
                sum2+=1
        if person==3:
                sum3+=1
        if person==4:
                sum4+=1
        if person==5:
                sum5+=1
        if person==6:
                sum6+=1
        if person==7:
                sum7+=1

print sum0
print sum1
print sum2
print sum3
print sum4
print sum5
print sum6
print sum7
'''

numGroups = 200000/20
numAssigned = [0]*8

numInGroup = [0]*numGroups
'''
target = open('usersClustered.csv','w')
for i in range(len(usersUnclustered)):
       

        groupid = numAssigned[proximityCluster[i]]%numGroups
        numAssigned[proximityCluster[i]]+=1

        while numInGroup[groupid]>=20: #sets limit on group size
                groupid+=1
        numInGroup[groupid]+=1

        if(groupid<10):
                target.write(usersUnclustered[i][0])
                target.write('; ')
                target.write(usersUnclustered[i][1])
                target.write('; ')
                target.write(str(usersUnclustered[i][2]))
                target.write('; ')
                target.write(usersUnclustered[i][3])
                target.write('; ')
                target.write(str(usersUnclustered[i][4]))
                target.write('; ')
                target.write(str(usersUnclustered[i][5]))
                target.write('; ')
                target.write(str(usersUnclustered[i][6]))
                target.write('; ')
                target.write(str(usersUnclustered[i][7]))
                target.write('; ')
                target.write(str(usersUnclustered[i][8]))
                target.write('; ')
                target.write(str(usersUnclustered[i][9]))
                target.write('; ')
                target.write(str(usersUnclustered[i][10]))
                target.write('; ')
 
                target.write(str(groupid))
                target.write('\n')
target.close()
'''
