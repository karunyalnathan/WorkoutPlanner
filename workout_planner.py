'''
@author: Karunya Nathan
Dec 16, 2022

This program prompts the user to provide a file that lists workouts--
the file must list a day of the week followed by the exercises
to be performed in the workout. The day of the week and each workout 
should all be on separate lines. If there is a workout history
the user is instead asked if they want to keep the history or 
start a new. 

once the program is initalized the user is continually prompted
whether they want to:
edit workouts, start today's workout, print this weeks plan, or quit.

exercise histories and changes to the workout plan are saved to files
and reloaded (if keep is selected during initalization)

At the end of the program the user is prompted to provide an output file to
print readable exercise histories.
'''
import planner
import exercise
import datetime
import util

PLAN = planner.Planner()
 
def run_edit():
    while(True):
        day = input('what day\'s workout do you want to edit?: ').upper()
        if day in PLAN.workout_plan.keys():
            print('The currently in the library include:', end= " ")
            print(', '.join(list(PLAN.exercises.keys())))
            print('Please note exercises must be added in order.')
            while(True): 
                print('Would you like to add or remove an exercise?')
                anwser = util.get_yes_no('add','remove')
                e = input('Enter exercise: ').lower()
                if anwser:
                    PLAN.add_exercise_to_workout(day,e) 
                else:
                    PLAN.remove_exercise_from_workout(day,e)    

                if(len(PLAN.workout_plan[day]) == 0):
                    print(f'\n{day} is now a: REST DAY')
                else:           
                    print(f'\n{day}\'s workout is now:')
                    print('\n'.join(PLAN.workout_plan[day]))
                print(f'\nWould you like to add or remove another exercise to {day}\'s workout?')
                if util.get_yes_no():
                    continue
                else:
                    break
            
            print('Would you like edit another workout?')
            if util.get_yes_no():
                continue
            else:
                print('\n')
                print('This weeks workout plan: ')
                print(PLAN)
                break   
        else:
            print(f'{day} was not recogized as a day of the week. Try again.')
    return True


def run_start():
    
    workout = PLAN.workout_plan[list(PLAN.workout_plan.keys())[datetime.datetime.now().weekday()]]

    if len(workout) == 0:
        print('\nToday is a rest day! There is no workout to complete.')
        return True

    for name in workout:
        exercise =  PLAN.get_exercise(name)
        print('\n'+name.upper() + ':')
        exercise.print_last()
        working = True
        set = 1
        while working:
            print(f'    Set {set}:')
            reps = input('        Enter how many reps:')
            weight = input('        Enter the weight used:')
            exercise.log(reps.replace(' ', ''), weight.replace(' ', ''))
            print('\n        Would you like to do another set?')
            working = util.get_yes_no()
            set += 1
    
    print('\nGOOD JOB!! You finished you workout!!!')


    for name in workout:
        print(name.upper()+':')
        e = PLAN.get_exercise(name).get_printable_sets(str(datetime.datetime.today().date()))
        if e != None:
            print(e)

    return True

def run_print():
    print(PLAN)
    return True

def run_quit():
    print('Would you like to export you exercise progress to a file?')
    if util.get_yes_no():
        PLAN.print_output_exercise_history(input('What is the name of the file: '))
    print('\nThank you for using workout Planner!!!')
    return False

def read_input_file() -> list:
    lines = None
    while(lines == None):
        print('\nWhen providing a text file, the file must :')
        print('   List a day of the week followed by the exercises to be performed in the workout.')
        print('   The day of the week and each exercise should all be on separate lines.')
        print('example:')
        print('Monday\nPush ups\nPlank\nTuesday\nSquats')

        file_name = input('\nPlease provide a list of workouts to create your workout plan: ')
        lines = util.read_file(file_name, f'{file_name} was not found. Try again.')
    return lines

command_dict = {
    'edit' : run_edit,
    'start' : run_start,
    'print' : run_print,
    'quit' : run_quit
}


def init_new():
    print('Would you like to provide a workout plan or start fresh?')
    print('    provide = provide a text file that lists exercises days of the week')
    print('    fresh = start with an empty workout plan')
    if util.get_yes_no('provide', 'fresh'):

        PLAN.read_workout_plan(read_input_file())

if PLAN.has_history():
    print('Would like to:')
    print('    new = start a new workout plan')
    print('    keep = keep workout plan and all history')
    if util.get_yes_no('new', 'keep'):
        print('Do you want to delete all exercise history too?')
        print('    yes = delete all exercise history')
        print('    no = keep all exercise history')
        if util.get_yes_no():
            exercise.Exercise.delete_all_history()
        planner.Planner.delete_history()
        init_new()
    else:
        PLAN.load_history()
else:
    init_new()

print('This weeks workout plan: ')
print(PLAN)


running = True
while(running):
    command = input('''
    To edit your workouts, type: edit
    To start today's workout, type: start
    To print this weeks plan, type: print
    To quit type: quit

    what would you like to do: ''').lower()

    if command in command_dict.keys():
        running = command_dict[command]()
    else:
        print('The command you ented was not recognized. Please try again.')