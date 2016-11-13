import csv
import numpy as np

vitechData = np.genfromtxt('parsedVitechData.csv',dtype=None, delimiter = ',')
zipcodeMoney = np.genfromtxt('zipCodeSallaries.csv', delimiter = ',')

zipCodeMoneyDict  = dict(zip(zipcodeMoney[:,0],zipcodeMoney[:,1]))

target = open('usersUnclustered.csv','w')

for person in vitechData:
        try:
            sallary = zipCodeMoneyDict[person[2]]+((.4*zipCodeMoneyDict[person[2]])*np.random.uniform())-((.2*zipCodeMoneyDict[person[2]]))#mean sallary for zip code +-20%
        except Exception:
            sallary = 51759 +((.4*51759)*np.random.uniform())-((.2*51749))#mean sallary for zip code +-20%

        monthlyIncome = [0]*24
        if (20*np.random.uniform())>1.0:   #odds of starting fired
                monthlyIncome[0]+=sallary/12.0
        for i in range(1,24):
                if (60*np.random.uniform())>1.0:
                        monthlyIncome[i]+=monthlyIncome[i-1]#fired
                if (40*np.random.uniform())<1.0:
                        monthlyIncome[i]=sallary/12.0

        expenses = [(sallary/24.0)+(np.random.uniform()*2000.0) for i in range(24)]

        #target.write(person[0]+','+person[1],+','+person[2]+','+person[3], + ','+person[4])
        target.write(person[0])
        target.write('; ')
        target.write(person[1])
        target.write('; ')
        target.write(str(person[2]))
        target.write('; ')
        target.write(person[3])
        target.write('; ')
        target.write(str(monthlyIncome))
        target.write('; ')
        target.write(str(expenses))
        target.write('; ')
        target.write(person[4])
        target.write('; ')
        target.write(str(sallary))
        target.write('; ')
        target.write(str(np.mean(expenses)))
        target.write('; ')
        target.write(str(np.var(expenses)))
        target.write('; ')
        target.write(str(np.var(monthlyIncome)))
        target.write('\n')
target.close()
