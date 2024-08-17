import time

class Circuit:
	def __init__(self, sets, exerciseNum,time,restPerSet):
		self.exerciseNum = exerciseNum
		self.sets = sets
		self.time = time
		self.restPerSet = restPerSet
		self.exercises = []
		self.reps = []
	def setCircuit(self):
		for i in range(self.exerciseNum):
			self.exercises.append(input("Please add the first exercise"))
			self.reps.append(input("Please add the reps for the exercise"))
	def workout(self):
		for i in range(self.sets):
			for in range(self.exerciseNum):
				for i in range(self.time):
					print("Please Complete",self.reps[i],"reps of",self.exercise[i])
					print("You have",self.time-i,"seconds left")
					time.sleep(1)

