import numpy as np 
import matplotlib.pyplot as plt

######################################################


class proc(object):

    def __init__(self, arr, bur, pri, n):
        self.arr = arr
        self.bur = bur
        self.pri = pri
        self.n = n
        self.wait = 0
        self.tat = 0 
        self.weighted =0
        self.start =0
        self.finish = 0
        self.served =0
        self.time = bur



########################################################
f = open('input.txt', 'r')
processes = int(float(f.readline()))  # no of processes

arrival = f.readline()
k = arrival.split(' ')
arrivalMu = float(k[0])
arrivalSigma = float(k[1])

burst = f.readline()
k = burst.split(' ')
burstMu = float(k[0])
burstSigma = float(k[1])

priorityLamda = float(f.readline())
b = proc(4,5,6,7)

f.close()
################################################
procList = []
'''
for i in range(processes):
    arr = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    bur = (np.random.normal(loc=arrivalMu, scale=arrivalSigma))
    pri = int(np.random.poisson(lam=priorityLamda))
    procList.append(proc(arr, bur, pri, i ))                          
    '''
procList.append(proc (1,2,5,1))   
procList.append(proc (9,1,5,2)) 
#procList.append(proc (3,2,5,2)) 
#procList.append(proc (7,2,5,3)) 
#procList.append(proc (7,4,5,2)) 
processes =2

#####################################################
o = open('output.txt', 'w')
o.write(str(processes) + '\n')

for p in procList:
    o.write(str(p.n) + ' ' + str(p.arr) + ' ' + str(p.bur) + ' ' + str(p.pri) + '\n')

o.close()


#################FCFS##################################

context =1 
procList = []
procList.append(proc (1,2,5,1))   
procList.append(proc (9,1,5,2)) 
    
arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False)
    
    
for i in range(len(procList)):
    if i>0:
        if arrSorted[i].arr <= arrSorted[i-1].finish:
            arrSorted[i].start = arrSorted[i-1].finish+context
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].start
        elif arrSorted[i].arr > arrSorted[i-1].finish:
            arrSorted[i].start =arrSorted[i].arr
            arrSorted[i].finish = arrSorted[i].bur+arrSorted[i].arr
    else:
        arrSorted[i].start =arrSorted[i].arr    
        arrSorted[i].finish =arrSorted[i].arr+arrSorted[i].bur
    
st =[]  
n =[]      
diff =[]
for i in range(len(procList)):
    st.append(procList[i].start)
    n.append(procList[i].n)
    diff.append(procList[i].finish - procList[i].arr )
        
print(st,n,diff)    
plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
    
		
######################################################################
###########################SRTN#######################################
def SRTN(file,context):
    
    procList = []
    procList.append(proc (1,2,5,1))   
    procList.append(proc (9,1,5,2)) 
    st=[]
    fn=[]
    n=[]
    
    
    servedProc=-1    #no process
    timestep = 0.3
    arrSorted = sorted(procList, key=lambda x: x.arr, reverse=False) #sort according to arrival
    time =arrSorted[0].arr+float(context) 
    st.append(time)
    n.append(arrSorted[0].n)
       #start of timeline
    arrReady=[]
    c=0
    while c < len(arrSorted):
        if (arrSorted[c].arr<=time):
            arrReady.append(arrSorted[c])  # get the ready ones out of the arrival into the queue
            arrSorted.pop(c)
            c=c-1
        c = c+1
    
    
    while (len(arrSorted)>0 or len(arrReady)>0): #main loop
       
        arrReady.sort(key=lambda x: x.time, reverse=False)     # sort according to remaining time   
                
        if len(arrReady)>0:
            if servedProc!=-1 and servedProc != arrReady[0].n:
                fn.append(time)
                time += float(context)
                st.append(time)
                n.append(arrSorted[0].n)
            servedProc = arrReady[0].n       #serving
            arrReady[0].time -= timestep                    
            time+= timestep
        else:   
            time+= timestep
            servedProc=-1                               #no serving  ->advance time
        
        #new processes arriving
        
        c=0
        while c < len(arrSorted):
            if (arrSorted[c].arr<=time):
                arrReady.append(arrSorted[c])        # check new arriving
                arrSorted.pop(c)
                c=c-1
            c=c+1
            
        
        #finished proceses
        
        c=0
        while c < len(arrReady):
            if arrReady[c].time <=0:
                for j in range(len(procList)):
                    if arrReady[c].n ==procList[j].n :
                        fn.append(time+procList[j].time)        # remove finished proc from ready and set finish time in original list
                        procList[j].finish= time+procList[j].time
                        arrReady.pop(c)
                        c=c-1
                        break
            c=c+1
            
        
            
    print(st,n,diff)    
    plt.bar(st, n, width = diff ,align='edge', color = ('blue'))
    plt.show()

#######################################################
###############calc#################################	
'''
avgTat =0
weightedAvg =0
		
for i in range(len(procList)):
    arrSorted[i].tat = arrSorted[i].finish - arrSorted[i].arr
    arrSorted[i].wait= arrSorted[i].tat - arrSorted[i].bur	 # calc finish
    avgTat+=arrSorted[i].tat;
    weightedAvg += arrSorted[i].tat/arrSorted[i].bur
        
avgTat = avgTat/processes
weightedAvg = weightedAvg/processes
'''
'''
gui -> get data from text boxes and connect the button and get data form combo box 
code to read new input file 
'''
#################################################################################### SALAMA ###########################################################################
'''

###################   Code for Files #############################
processNumbers=[]
processArrivals=[]
processBursts=[]
processPriorities=[]

f=open("output.txt","r")
lines=f.readlines()
lines.remove(lines[0])
for x in lines:
    processNumbers.append(x.split(' ')[0])
for x in lines:
    processArrivals.append(x.split(' ')[1])
for x in lines:
    processBursts.append(x.split(' ')[2])
for x in lines:
    processPriorities.append(x.split(' ')[3])

f.close()


for x in range(len(processPriorities)):
    processPriorities[x]=processPriorities[x].replace('\n', '')
    
for i in range(len(processNumbers)):
    procList.append(proc(float(processArrivals[i]),float(processBursts[i]),int(processPriorities[i]),int(processNumbers[i])))


o=open("output2.txt", "w")
for p in procList:
    o.write(str(p.n) + ' ' + str(p.arr) + ' ' + str(p.bur) + ' ' + str(p.pri) + '\n')

o.close()
'''
#######################################################################
#################### RR ###############################################
'''
cpyProcList=[]
cpyProcList.append(proc(0,8,3, 0 + 1))
cpyProcList.append(proc(1, 4,3 , 1 + 1))
cpyProcList.append(proc(2, 9, 3, 2 + 1))
cpyProcList.append(proc(3,5, 4, 3 + 1))


cpyProcList.sort(key=lambda x: x.arr, reverse=False)
readyQueue=[]
seq=[]
quantum=4


t=cpyProcList[0].arr #initial time 
readyQueue.append(cpyProcList[0])
cpyProcList[0].beenReady=1

################# Arrays for Graph####################
procStarts=[]
procEnds=[]
procDiff=[]
procIDs=[]



flag=0
while True:
    if len (readyQueue) !=0:
        if readyQueue[0].bur > quantum:
            t+=context
            procStarts.append(t)
            t+= quantum
            procEnds.append(t)
            readyQueue[0].bur-=quantum
            for u in range (len(cpyProcList)):
                if readyQueue[0].n == cpyProcList[u].n:
                    cpyProcList[u].bur=readyQueue[0].bur
            readyQueue[0].arr+=quantum
            seq.append("->")
            seq.append(readyQueue[0].n)
            procIDs.append(readyQueue[0].n)
            
        else:
            t+=context
            procStarts.append(t)
            t+=readyQueue[0].bur
            procEnds.append(t)
            readyQueue[0].arr+=readyQueue[0].bur
            for j in range(len(procList)):
                if readyQueue[0].n == procList[j].n:
                    procList[j].finish=t
                    seq.append("->")
                    seq.append(procList[j].n)
                    procIDs.append(readyQueue[0].n)
            readyQueue[0].bur=0
            for u in range (len(cpyProcList)):
                if readyQueue[0].n == cpyProcList[u].n:
                    cpyProcList[u].bur=readyQueue[0].bur
                    
                    
                    
        for index in range (len(cpyProcList)):
            if cpyProcList[index].arr<=readyQueue[0].arr:
                if cpyProcList[index].beenReady==0:
                    readyQueue.append(cpyProcList[index])
                    cpyProcList[index].beenReady=1
                    
        if readyQueue[0].bur!=0:
            for index in range (len(cpyProcList)):
                if cpyProcList[index].arr<=t:
                    if cpyProcList[index].beenReady==0:
                        readyQueue.append(cpyProcList[index])
                        cpyProcList[index].beenReady=1
            readyQueue.append(readyQueue[0])
            readyQueue.remove(readyQueue[0])
        else:
            readyQueue.remove(readyQueue[0])
            
            
            
        
    else:
        t+=1

        
    
    for index in range (len(cpyProcList)):
         if cpyProcList[index].bur==0:
             flag+=1
    if flag == len(cpyProcList):
        break
    else:
        flag=0

         
            
        




#printing sequense
for index in range (len(seq)):
    print(seq[index])
    
for index in range (len(procEnds)):
    procDiff.append(procEnds[index]-procStarts[index])
    print(procIDs[index],procStarts[index],procEnds[index],procDiff[index])

    

print("/n")


for index in range (len(procList)):
    procList[index].tat=procList[index].finish-procList[index].arr
    procList[index].wait=procList[index].tat-procList[index].bur
    procList[index].weighted=float(procList[index].tat)/float(procList[index].bur)
    print(procList[index].n)
    print(procList[index].finish)

#################################################################################
'''

########################################### HPF #################################
#################################################################################
'''
servedProcList = []
procList.sort(key=lambda x: x.arr, reverse=False)

#handeling first process
tmparr=[]
for i in range (len(procList)):
    if procList[0].arr==procList[i].arr:
        tmparr.append(procList[i])
tmparr.sort(key=lambda x: x.pri, reverse=True)
for index in range(len(procList)):
    if tmparr[0].n == procList[index].n:
        procList[index].start=procList[index].arr+context
        procList[index].finish=procList[index].start+procList[index].bur
        procList[index].served=1
        servedProcList.append(procList[index])
tmparr=[]
######################################################
allProcessesAreDone=False
while allProcessesAreDone!=True:
    for i in range (len(procList)):
        temparr=[]
        #first case if the arrival time of [i] is less than the finish time [i-1]
        if True:
            if procList[i].served!=1:
                for index in range(len(procList)):
                    if procList[index].served!=1 and procList[index].arr<=servedProcList[-1].finish:
                        temparr.append(procList[index])
                if len(temparr)>0:
                    temparr.sort(key=lambda x: x.pri, reverse=True)
                    for index in range(len(temparr)):
                        if temparr[index].arr == temparr[0].arr and temparr[index].pri==temparr[0].pri and temparr[index].n<temparr[0].n:
                            temparr[0]=temparr[index]
                for index in range(len(procList)):
                    if len(temparr)>0 and temparr[0].n == procList[index].n:
                        if len(servedProcList)>0:
                            procList[index].start=servedProcList[-1].finish+context
                            procList[index].finish=procList[index].start+procList[index].bur
                        else:
                            procList[index].start=procList[index].arr+context
                            procList[index].finish=procList[index].start+procList[index].bur
                        procList[index].served=1
                        servedProcList.append(procList[index])
#################################################################################################################################
                #second case if the arrival time of [i] is greater than the finish time [i-1]
                if len(temparr)==0:
                    for index in range(len(procList)):
                        if procList[index].served!=1 and procList[index].arr>servedProcList[-1].finish:
                            temparr.append(procList[index])
                    temparr.sort(key=lambda x: x.arr, reverse=False)
                    for index in range(len(temparr)):
                        #check if there is more than on e process have > arr but diff priorities
                        if temparr[index].arr == temparr[0].arr and temparr[index].pri>temparr[0].pri:
                            temparr[0]=temparr[index]
                        elif temparr[index].arr == temparr[0].arr and temparr[index].pri==temparr[0].pri and temparr[index].n<temparr[0].n:
                            temparr[0]=temparr[index]
                    #marking process as served and put it in the served list
                    for index in range(len(procList)):
                        if temparr[0].n == procList[index].n:
                            if len(servedProcList)>0:
                                procList[index].start=procList[index].arr+context
                                procList[index].finish=procList[index].start+procList[index].bur
                            procList[index].served=1
                            servedProcList.append(procList[index])
#####################################################################################################################################
    #check if all processes are served to exit the while loop
    for i in range (len(procList)):
        if procList[i].served!=1:
            allProcessesAreDone=False
            break
        else:allProcessesAreDone=True


for i in range (len(servedProcList)):
    servedProcList[i].tat=servedProcList[i].finish-servedProcList[i].arr
    servedProcList[i].wait=servedProcList[i].tat-servedProcList[i].bur
    servedProcList[i].weighted=float(servedProcList[i].tat)/float(servedProcList[i].bur)
    print(servedProcList[i].finish)
    print(servedProcList[i].n)
################################ HPF Graph ####################################   
procStarts=[]
procEnds=[]
procDiff=[]
procIDs=[]
for i in range (len(servedProcList)):
    procIDs.append(servedProcList[i].n)
    procStarts.append(servedProcList[i].start)
    procEnds.append(servedProcList[i].finish)
    procDiff.append(procEnds[i]-procStarts[i])
    print( procIDs[i],procStarts[i], procEnds[i],procDiff[i])
###############################################################################
'''