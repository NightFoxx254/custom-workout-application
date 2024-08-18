import time
import os

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
			self.exercises.append(input("Please add the first exercise: "))
			self.reps.append(int(input("Please add the reps for the exercise: ")))
	def workout(self):
		for a in range(self.sets):
			for b in range(self.exerciseNum):
				for c in range(self.time):
					print("Please Complete",self.reps[b],"reps of",self.exercises[b])
					print("You have",self.time-c,"seconds left")
					time.sleep(1)
					os.system("clear")
			for d in range(self.restPerSet):
				print("Rest for",self.restPerSet-d,"more seconds")
				time.sleep(1)
				os.system("clear")

circuits =[]
while True:
	action = input("What do you want to do?(Add a circuit or complete a workout) ")
	if "add" in action:
		circuits.append(Circuit(int(input("Please enter the number of sets: ")),int(input("Please enter the number of exercises: ")),int(input("Please enter the time per exercise: ")),int(input("Please enter the rest in between sets: "))))
		circuits[len(circuits)-1].setCircuit()
	elif "complete" in action:
		action = int(input("what workout would you like to complete?"))
		circuits[action-1].workout()


