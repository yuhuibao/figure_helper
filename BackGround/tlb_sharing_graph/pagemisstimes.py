import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


access_times = pd.read_csv("pagemisstimes.csv",skiprows=0)


pages = access_times.iloc[:,0]
pages = pd.unique(pages)

hashpages = []



for i in range(0,len(pages)):
	

	page = pages[i]



	isPage = access_times.iloc[:,0] == page
	accessInfo = access_times[isPage]


	tlbIDs = accessInfo.iloc[:,1]
	times  = accessInfo.iloc[:,2]


	timeList = times.tolist()


	


	arrayTime = np.array(timeList)
	sort_index = np.argsort(arrayTime) 

	tlbIDs = tlbIDs.tolist()
	sortedTLB = sorted(tlbIDs)    
	mask = 0b11111111111111111111

	hashPage = page & mask

	#print(hashPage)
	
	hashpages.append(hashPage)

	

	test_list = [27, 15, 9, 4, 60, 48, 12, 16]
	count = 0

	timeForFourPages = []
	tlbForFourPages  = []

	tlbIDsSorted =[0]*len(test_list)
	timeSorted  = [0.0]*len(test_list)

	#print tlbIDs



	for i in range(0,len(tlbIDs)):
		if tlbIDs[i] in test_list:
			timeForFourPages.append(arrayTime[i])
			tlbForFourPages.append(tlbIDs[i])
			count = count + 1

	#print (count)



	tlbIDMapped = [0]*len(test_list)

	if count == len(test_list):
		print tlbForFourPages



		
		fourPageArrayTime = np.array(timeForFourPages)
		sort_index = np.argsort(fourPageArrayTime) 
		
		for i in range(0, len(tlbIDsSorted)):
			tlbIDsSorted[i] = tlbForFourPages[sort_index[i]]
			timeSorted[i] = timeForFourPages[sort_index[i]]*10**(-6)

   
			for j in range(0,len(test_list)):
				if tlbIDsSorted[i] == test_list[j]:
					tlbIDMapped[i] = j + 1

		


		print tlbForFourPages
		print tlbIDsSorted
		print tlbIDMapped
		style = dict(size=10, color='gray')

        #print(tlbForFourPages)
        #print(tlbIDsSorted)
        #print(timeForFourPages)



		'''fig, ax1 = plt.subplots(figsize=(8, 4))
		color = 'tab:pink'
		ax1.set_xlabel('time(s)')
		ax1.set_ylabel('TLB ID', color=color)
		label = "T"+str(tlbIDMapped[0])
		#for i in range(0,len(tlbIDMapped)):
			#ax1.text(timeSorted[i], tlbIDMapped[i], label, **style)
		
		ax1.plot(timeSorted, tlbIDMapped, marker="o",markerfacecolor= "r")
		ax1.legend()
		plt.savefig(str(page)+".pdf",bbox_inches='tight')
		time.sleep(5)'''



myset = set(hashpages)
print(len(myset))
    



	#time = access_times.iloc[:,0]