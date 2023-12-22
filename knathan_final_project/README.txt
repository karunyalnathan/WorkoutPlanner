

AUTHOR: Karunya Nathan

This read me file:
 1. summarizes what the workout plan program does and why it is useful 
 2. provides instructions on running the program  


**READ ME**

Workout Plan is a program that allows you to upload a workout plan or 
build one with the program. It allows you to create a different workout
for each day of the week, helping you stick to a routine. The program
also saves your progress for each exercise you do, so you can see your 
progress overtime.

When you run workout_plan.py, if you have a workout history you will 
be asked whether you want to keep your previous history or start new.
Starting new will delete previous exercise history and the prior workout plan.
If you choose to start new or have no prior history you are asked to either 
provide a file listing your workout plan (use workouts.txt) or start your 
plan fresh. if you provide a file, the file must list a day of the week 
followed by the exercises to be performed in the workout. The day of the week 
and each exercise should all be on separate lines.
example:
    Monday
    Push ups
    Plank
    Tuesday
    Squats

Once the program is initialized the user is continually prompted
whether they want to either edit workouts, start today's workout, 
print this weeks plan, or quit.

Editing will allow you to add or remove exercises to/from a workout.
Starting a workout will select the workout corresponding to the current
day of the week. The program will run through the list of exercise in 
a workout and will prompted you to enter the reps and weight for each set.
At the end of each set, you will be asked if you want to do another set for 
that exercise. Once your workout is complete a workout summary is printed 
to the terminal. 
Upon quitting the program you will be asked if you would like to save your
exercise history to an output file. This is allow you to easily see
you're progression for each exercise in your current workout program. 

planner.py holds the class Planner, which has 2 instance variables: 
1. exercises, which is a dictionary of exercises. The key being the name 
of the exercise and the value being the exercise object.
2. workout_plan which is a dictionary of workouts. The key being the 
day of the week, and the value being the workout for that given day.
Edits to planner are saved to an external file and can be reloaded.
Please note there should only be one instance of this class.

exercise.py holds the class Exercise, which stores the name of the exercise 
and the last number of sets, reps, and weight preformed/logged, in 
addition to the full exercise history, which privately stores a list of sets.
Each set is represented by a tuple that holds the number or reps and the weight 
used in the given set. Each list of sets can be looked by using the date it was 
preformed as the key. The history is also written to a file after each set is logged
and reread from the file in the constructor, and can thus persist across
runs. 

util.py is a genetic util class.

**** Instructions to run ****
cd in into the folder holding the above mentioned files, and run workout_planner.py

If you choose to start fresh, or are promoted and would like to provide a workout
plan, provide workouts.txt.

If you choose to start fresh and delete all workout history, backup exercise histories can 
be copied from the _backup_exercises directory and pasted into the exercises directory.

**** Files ****

	workout_plan.py : the main program from which workout plan is run. 
	     planner.py : holds the class Planner 
	    exercise.py : holds the class Exercise 
	        util.py : a genetic util class
	   workouts.txt : an input file to provide an existing workout plan

	Files that story program history:
   		     __workout_plan.txt : stores the current workout plan
	exercises/__<exercise name>.txt : stores exercise history
		_backup_exercises/*.txt : stores a copy of initial exercise histories
					  incase exercise histories are deleted by the 
					  program when prompted by the user. 
					  This folder is not used by the program, but is
					  provided for the grader's convenience. 
	
