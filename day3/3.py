f = open("3.txt","r")
input_list = list(map(lambda line : str(line.strip("\n")),f.readlines()))
bitList = [0] * len(input_list[0])
maxNumList = [0] * len(input_list[0])
decimalCalculator1 = 0
decimalCalculator2 = 0
for i in range(len(input_list)) :
	tmp = input_list[i]
	for j in range(len(input_list[0])) :
		if tmp[j:j+1] == "1" :
			bitList[j] +=1
for i in range(len(input_list[0])) :
	if max(bitList[i],len(input_list)-bitList[i]) == bitList[i] :
		maxNumList[i] = 1 
	decimalCalculator1 += pow(2,(len(input_list[0])-1-i))*maxNumList[i]
decimalCalculator2 = pow(2,len(input_list[0])) -1 - decimalCalculator1
print(decimalCalculator1*decimalCalculator2)
#first solution



o2List = input_list.copy()
co2List = input_list.copy()



def mostCommonValue(cnt,o2List) :
		forO2 = 0
		for i in range(len(o2List)) :
			if(o2List[i][cnt] == "1") :
				forO2 +=1
		if forO2 >= len(o2List) / 2 and len(o2List) > 1 :
			removing = 0
			for i in range(len(o2List)) :
				if o2List[i-removing][cnt] == "0" :
					o2List.pop(i-removing)
					removing+=1
		elif forO2 < len(o2List) / 2 and len(o2List) > 1 :
			removing = 0
			for i in range(len(o2List)) :
				if o2List[i-removing][cnt] == "1" :
					o2List.pop(i-removing)
					removing+=1
		if len(o2List) > 1 : 
			return mostCommonValue(cnt+1,o2List)
		else :
			return o2List

def leastCommonValue(cnt,co2List) :
		forCo2 = 0
		for i in range(len(co2List)) :
			if(co2List[i][cnt] == "1") :
				forCo2 +=1
		if forCo2 >= len(co2List) / 2 and len(co2List) > 1 :
			removing = 0
			for i in range(len(co2List)) :
				if co2List[i-removing][cnt] == "1" :
					co2List.pop(i-removing)
					removing+=1
			
		elif forCo2 < len(co2List) / 2 and len(co2List) > 1 :
			removing = 0
			for i in range(len(co2List)) :
				if co2List[i-removing][cnt] == "0" :
					co2List.pop(i-removing)
					removing+=1
		if len(co2List) > 1 : 
			return leastCommonValue(cnt+1,co2List)
		else :
			return co2List



tmp = 0
o2List = mostCommonValue(tmp,o2List)
co2List = leastCommonValue(tmp,co2List)
decimalForO2 = 0
decimalForCO2 = 0

for i in range(len(o2List[0])) :
	decimalForO2 = decimalForO2 + int(o2List[0][i])*pow(2,len(o2List[0])-i-1)
for i in range(len(co2List[0])) :
	decimalForCO2 = decimalForCO2 + int(co2List[0][i])*pow(2,len(co2List[0])-i-1)
		

print(decimalForCO2*decimalForO2)

#second solution