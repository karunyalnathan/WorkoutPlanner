'''
@author: Karunya Nathan
Dec 16, 2022

exercise.py holds the class Exercise.
An exercise object, stores the name of the exercise 
and the last number of sets, reps, and weight preformed/logged.
The name should be unique, as it is used to store the exercise history.
During runtime the exercise history is privately stored in a dictionary.
The history dictionary stores a list of sets, represented by a tuple 
holding the number or reps and the weight used in the given set.
Each list of sets can be looked by using the date it was preformed 
as the key. The history is also written to a file after each set is logged
and reread from the file in the constructor, and can thus persist across
runs. 

'''
import datetime
import os
import util

class Exercise():
    __FOLDER = 'excercises'
    def __init__(self, name: str):
        self.name = name.replace(' ', '')
        self.reps = '0'
        self.sets = '0'
        self.weight = '0lb'
        self.__history = dict()
        self.__history_filename = f'__{self.name}.txt'
        self.__load_history()

    def get_sets(self, date) -> list:
        try:
            return self.__history[date]
        except:
            print(f'could not find set for key: {date}')
            return []

    def print_last(self):
        print('Your last reps, sets and weight:')
        print(f'reps: {self.reps}, sets: {self.sets}, weight: {self.weight}')

    def get_printable_sets(self, date: str) -> str:
        printable = ''
        if date in self.__history.keys(): 
            sets = self.__history[date]
            for i, set in enumerate(sets):        
                printable += f'    Set {i+1}: reps = {set[0]}, weight = {set[1]}\n'
        return printable

    
    def log(self, reps = '1', weight = '0lb'):
        date = str(datetime.datetime.today().date()) 
        self.__log(reps, weight)
    
    def __log(self, reps:str, weight:str, date = str(datetime.datetime.today().date())):
        if date not in self.__history.keys():
            self.__history[date] = [(reps, weight)]
        else:
            self.__history[date].append((reps, weight))
        self.reps = reps
        self.weight = weight
        self.sets = len(self.__history[date])
        self.__save_exercise()

    def __save_exercise(self):
        try:
            os.mkdir(Exercise.__FOLDER)
        except:
            None
        util.write_file(os.path.join(os.getcwd(), 
        Exercise.__FOLDER, 
        self.__history_filename),
        self.__get_log())

    def __get_log(self) -> str:
        output = ''
        for date in sorted(self.__history.keys()):
            output += date+'\n'
            sets = self.__history[date]
            for set in sets:
                output += f'{set[0]} {set[1]}\n'
        return output

    def delete_all_history():
        if os.path.exists(Exercise.__FOLDER):
            for file in os.listdir(Exercise.__FOLDER):
                os.remove(os.path.join(Exercise.__FOLDER, file))

    def __load_history(self):
        if os.path.exists(Exercise.__FOLDER+'/'+self.__history_filename):
            date = ''
            for line in util.read_file(Exercise.__FOLDER+'/'+self.__history_filename, ''):
                line = str(line).split(' ')
                if len(line)==1:
                    date = line[0]
                elif len(date) != 0 and len(line)==2:
                    self.__log(line[0], line[1], date)

    def __str__(self) -> str:
        printable_histroy = ''
        printable_histroy += '--- ' + self.name.upper() + ' ---\n'
        for date in sorted(self.__history.keys()):
            printable_histroy += '  '+date + ':\n'
            sets = self.__history[date]
            for i,set in enumerate(sets):
                printable_histroy += f'    Set {i+1}: reps = {set[0]}, weight = {set[1]}\n'
        return printable_histroy

def __unit_test_1():
    '''
    tests gets log, updates instance variables
    '''
    squat = Exercise('squat')
    squat.log('3', '115lb')
    assert squat.reps, '3'
    assert squat.weight, '115lb'


def __unit_test_2():
    '''
    tests get_sets and log
    '''
    squat = Exercise('squat')
    squat.log('3', '110lb')
    set = squat.get_sets(str(datetime.datetime.today().date()))
    assert len(set), 1
    assert set[0][0], '3' 
    assert set[0][1], '110lb'


if __name__ == '__main__':
    __unit_test_1()
    __unit_test_2()