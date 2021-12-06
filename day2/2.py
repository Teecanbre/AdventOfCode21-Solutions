f = open("2.txt","r")
commands = list(map(lambda line :line.strip("\n"),f.readlines()))
horizontalCount = 0
depthCount = 0 
aim = 0
horizontalPosition = 0 
depthPosition = 0 
for i in  commands :
	if i.startswith("forward" )  :
		horizontalCount = horizontalCount + int(i.strip("forward "))
		horizontalPosition = horizontalPosition + int(i.strip("forward "))
		depthPosition = depthPosition + aim*int(i.strip("forward "))
	if i.startswith("down") :
		depthCount  = depthCount + int(i.strip("down "))
		aim = aim + int(i.strip("down "))
	if i.startswith("up") :
		depthCount  = depthCount - int(i.strip("up "))
		aim = aim - int(i.strip("up "))
print(depthCount*horizontalCount)
print(horizontalPosition*depthPosition)

#first and second solution -> second one is about aim 

