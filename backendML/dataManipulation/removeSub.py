import re
target = open('forRooday.json','w')
with open('usersClustered.json') as f:
        for line in f:
                jline = re.sub('\\\\"','',line)
#                print(jline)
                target.write(jline)
target.close()

