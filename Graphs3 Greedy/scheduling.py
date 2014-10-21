file = open('jobs.txt')
numJobs = int(file.readline())
jobs = []
def key(job):
	return job[0] - job[1]
def keyOptimal(job):
	return job[0]/job[1]
def keyW(job):
	return job[0]
for _i in range(numJobs):
	line = file.readline()
	job = [float(x) for x in line.split()]
	jobs.append(job)
jobs.sort(key=keyW)
jobs.sort(key=keyOptimal)
jobs.reverse()
completionTotal = 0
currentTime = 0
for job in jobs:
	currentTime += job[1]
	completionTotal += job[0] * currentTime
	# print(currentTime, completionTotal)

print(completionTotal)
