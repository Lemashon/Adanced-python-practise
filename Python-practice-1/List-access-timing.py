import datetime
import random
import time

def main():
    #write an XML file with the results
    
    file = open("ListAccessTime.xml", "w")
    
    file.write('<?ml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    file.write('<Plot title = "Average List Element Access Time>\n')
    
    #Test lists of size 1000 to 200000
    xmin = 1000
    xmax = 200000
    
    #Record the list sizes in XLists and the average acess time within    
    
    xList = []
    yList = []
    
    for x in range(xmin, xmax+1, 1000):
        xList.append(x)
        prod = 0
        
    #Creates a list of size x with all 0s
    
    list = [0] * x
    
    #Let any garbafe collection mcomplete or atleast settle down
    time.sleep(1)
    
    #Time before the 1000 test retrievals
    starttime = datetime.datetime.now()
    
    for v in range(1000):
        
        val = list[index]
        prod = prod*val
        
    #Time after the 1000 test retrievals
    endtime = datetime.datetime.now
    
    #Difference in time between start and end
    
    deltaT = endtime - starttime
    
    yList.append(accessTime)
    
    file.write(' <Axes>\n')
    file.write(' <XAxis min="'+str(xmin)+'" max="'+str(xmax)+'">List Size</XAxis>\n')
    file.write(' <YAxis min="'+str(min(yList))+'" max="'+str(60)+'">Microseconds</YAxis>\n')
    file.write(' </Axes>\n')
    file.write(' </Sequence>\n')
    
    xList = lst
    yList = [0] * 200000
    
    time.sleep(2)
    
    for i in range(1000):
        starttime = datetime.datetime.now()
        index = random.randint(0,200000-1)
        xList[index] = xList[index] + 1
        endtime = datetime.datetime.now()
        deltaT = endtime - starttime
        yList[index] = yList[index] + deltaT.total_seconds() * 1000000
        
    file.write(' <Sequence title="Access Time Distribution" color="blue">\n')

    for i in range(len(xList)):
        if xList[i] > 0:
            file.write(' <DataPoint x="'+str(i)+'" y="'+str(yList[i]/xList[i])+'"/>\n')

    file.write(' </Sequence>\n')
    file.write('</Plot>\n')
    file.close()
    
if __name__ == "__main__":
    main()

    
    
    
