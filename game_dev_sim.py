import time
import threading
import os

employees = 1
project = False
difficulty = 1
projectName = None;
finishedProjs = []
projectProgress = 0
money = 1000
username = input("What is your name ")


def projectTick():
	global project
	global difficulty
	global projectProgress
	global projectName
	if project == True:
		projectProgress += 10 / difficulty
		print(f"Working on {projectName}")
		print(f"{projectProgress}% |" + "#" * round(projectProgress / 10) + "|")
		time.sleep(1)
		os.system('cls')
	else:
		a = input("New Project Y|N")
		if a.lower() == "y":
			projectName = input("Project Name ")
			project = True
			print(project)
def projectDone():
	global project
	global projectProgress
	if projectProgress >= 100:
		finishedProjs.insert(1, projectName)
		project = False
		projectProgress = 0


def Tick():
	projectTick()
	projectDone()



while True:
	time.sleep(0.5)
	Tick()



