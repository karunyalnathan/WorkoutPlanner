'''
@author: Karunya Nathan
Dec 16, 2022

util.py is a genetic util class.
'''

def read_file(filename: str, error: str = f"Unable to load file.")->list:
    try:
        text_file = open(filename, 'r')
    except FileNotFoundError:
        print(f'{filename} was not found.')
    except:
        print(error)
    else:
        lines = text_file.read().split('\n')
        text_file.close()
        return lines


def write_file(filename: str, output: str ):
    try:
        text_file = open(filename, 'w')
        text_file.write(output)
        text_file.close()
    except:
        print('Unable to write to file')
    else:
        None


def get_yes_no(option_a = 'yes', option_b = 'no'):
    while True:
        anwser = input(f'Enter {option_a} or {option_b}: ')
        if anwser.lower() == option_a.lower():
            return True
        elif anwser.lower() == option_b.lower():
            return False
        else:
            print(f'{anwser} was not recognized as {option_a} or {option_b}. Try again.')