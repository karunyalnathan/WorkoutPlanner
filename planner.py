'''
@author: Karunya Nathan
Dec 16, 2022

planner.py holds the class Planner.
The planner object has 2 instance variables: 
1. exercises, which is a dictionary of exercises.
the key being the name of the exerices and the 
value being the exercise object.
2. workout_plan which is a dictionary of workouts.
the key being the day of the week, and the value
being the workout for that given day.

Edits to planner are saved to an exernal file and can be reloaded.
Please note there should only be one instance of this class.
'''
import os
import exercise
import util
class Planner():

    __HISTORY_FILE_NAME = '__workout_plan.txt'    
    __SELF = None

    def __init__(self, exercises : list = []):
        Planner.__SELF = self
        self.exercises =  {}
        for e in exercises:
            self.add_exercise(e)
        self.workout_plan = { 
            'MONDAY': [],
            'TUESDAY': [],
            'WEDNESDAY': [],
            'THURSDAY': [],
            'FRIDAY': [],
            'SATURDAY': [],
            'SUNDAY': []
            }

    def __new__(cls):
    #reference: https://www.geeksforgeeks.org/__new__-in-python/
        if Planner.__SELF == None:
            return super(Planner, cls).__new__(cls)
        else:
            return Planner.__SELF

    def has_history(self):
        return os.path.exists(Planner.__HISTORY_FILE_NAME)

    def add_exercise(self, new_exercise: str):
        self.exercises[new_exercise.lower()] = exercise.Exercise(new_exercise.lower())
        self.__save()

    def add_exercises(self, new_exercises: list):
        for e in new_exercises:
            self.add_exercise(e)

    def add_exercise_to_workout(self, workout: str, new_exercise: str):
        new_exercise = new_exercise.lower()
        if new_exercise in self.exercises.keys():
            self.workout_plan[workout].append(new_exercise)
        else:
            print(f'{new_exercise} is not in the current exercise library would you like to add it?')
            if util.get_yes_no():
                self.add_exercise(new_exercise)
                self.workout_plan[workout].append(new_exercise)
                print(f'{new_exercise} was added to the exercise library and to {workout}\'s workout.')
            else:
                print(f'{new_exercise} was not added.')
        self.__save()

    def remove_exercise_from_workout(self,workout: str, exercise: str):
        try:
            self.workout_plan[workout].remove(exercise)
            self.__save()
        except:
            print(f'{exercise} was not removed.')

    def get_exercise(self, name: str) -> exercise.Exercise:
        if name in self.exercises.keys():
            return self.exercises[name]

    def __str__(self) -> str:
        output = ''
        for k,v in self.workout_plan.items():
            output += k + ':'
            if len(v) == 0:
                output += '\n    REST'
            else:
                for e in v:
                    output += '\n    ' + str(e).capitalize()
            output += '\n\n'
        return output

    def __save(self):
        output = ''
        for k,v in self.workout_plan.items():
            output += k+'\n'
            for e in v:
                output += e + '\n'
        util.write_file(os.getcwd()+'/'+Planner.__HISTORY_FILE_NAME, output)

    
    def load_history(self):
        self.read_workout_plan(util.read_file(Planner.__HISTORY_FILE_NAME, 'Unable to load workout history, sorry.'))

    def delete_history():
        os.remove(Planner.__HISTORY_FILE_NAME)

    def read_workout_plan(self, input: list):
        workout = ''
        for line in input:
            if len(line) == 0:
                continue
            elif line.upper() in self.workout_plan.keys():
                workout = line.upper()
            else:
                self.add_exercise(line.lower())
                if len(workout) != 0:
                    self.workout_plan[workout].append(line.lower())

    def print_output_exercise_history(self, filename: str):
        output = ''
        for k in sorted(self.exercises.keys()):
            output += str(self.get_exercise(k))+'\n'
        util.write_file(os.getcwd()+'/'+filename, output)



def __unit_test_1():
    '''
    tests that adding exercise
    '''
    planner = Planner()
    planner.add_exercise('squat')
    assert len(planner.exercises),1

def __unit_test_2():
    '''
    tests removing an exercise
    '''
    planner = Planner()
    planner.add_exercise('squat')
    planner.add_exercise('dl')
    planner.workout_plan['MONDAY'].append('squat')
    planner.workout_plan['MONDAY'].append('dl')
    assert len(planner.workout_plan['MONDAY']),2
    planner.remove_exercise_from_workout('MONDAY', 'squat')
    assert len(planner.exercises),1 
    assert len(planner.workout_plan['MONDAY']),1


if __name__ == '__main__':
    __unit_test_1()
    __unit_test_2()