import os
import sys
import glob
sys.path.append('..')


# Prompts the user to confirm overriding file

def save_override(arg, targetAccount):
    if arg == 's':
        print('[INFO]: A file already exists with the name ' +
              targetAccount + '_followers.txt')
        usr = input('[WARNING]: OVERRIDE CURRENT FILE WITH NEW FILE? (y/n):')
        if usr.lower() == 'y':
            return True
        else:
            return False
    elif arg == 'g':
        print('[INFO]: A file already exists with the name ' +
              targetAccount + '_following.txt')
        usr = input('[WARNING]: OVERRIDE CURRENT FILE WITH NEW FILE? (y/n):')
        if usr.lower() == 'y':
            return True
        else:
            return False
    elif arg == 'r':
        print('[INFO]: A file already exists with the name ' +
              targetAccount + '_results.txt')
        usr = input('[WARNING]: OVERRIDE CURRENT FILE WITH NEW FILE? (y/n):')
        if usr.lower() == 'y':
            return True
        else:
            return False


# Checks to see if a file with the regular output filename exists

def save(list_name, arg, targetAccount):
    if arg == 's':
        if find_files(targetAccount + '_followers.txt'):
            if save_override(arg, targetAccount):
                regular_save(list_name, arg, targetAccount)
            else:
                irregular_save(list_name, arg, targetAccount)
        else:
            regular_save(list_name, arg, targetAccount)
    elif arg == 'g':
        if find_files(targetAccount + '_followers.txt'):
            if save_override(arg, targetAccount):
                regular_save(list_name, arg, targetAccount)
            else:
                irregular_save(list_name, arg, targetAccount)
        else:
            regular_save(list_name, arg, targetAccount)
    elif arg == 'r':
        if find_files(targetAccount + '_results.txt'):
            if save_override(arg, targetAccount):
                regular_save(list_name, arg, targetAccount)
            else:
                irregular_save(list_name, arg, targetAccount)
        else:
            regular_save(list_name, arg, targetAccount)


# Outputs the lists to a regular output filename

def regular_save(list_name, arg, targetAccount):
    if arg == 's':
        print('[INFO]: Saving to ' + targetAccount + '_followers.txt...')
        file = open(targetAccount + "_followers.txt", "w")
    elif arg == 'g':
        print('[INFO]: Saving to ' + targetAccount + '_following.txt...')
        file = open(targetAccount + "_following.txt", "w")

    elif arg == 'r':
        print('[INFO]: Saving to ' + targetAccount + '_results.txt...')
        file = open(targetAccount + "_results.txt", "w")

    for usr in list_name:
        file.write(usr + '\n')
    file.close()

    if arg == 's':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_followers.txt')
    elif arg == 'g':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_following.txt')
    elif arg == 'r':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_results.txt')


# Outputs the lists to an irregular output filename

def irregular_save(list_name, arg, targetAccount):
    if arg == 's':
        print('[INFO]: Saving to ' + targetAccount + '_followers2.txt...')
        file = open(targetAccount + "_followers2.txt", "w")
    elif arg == 'g':
        print('[INFO]: Saving to ' + targetAccount + '_following2.txt...')
        file = open(targetAccount + "_following2.txt", "w")
    elif arg == 'r':
        print('[INFO]: Saving to ' + targetAccount + '_results2.txt...')
        file = open(targetAccount + "_results.txt", "w")

    for usr in list_name:
        file.write(usr + '\n')
    file.close()

    if arg == 's':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_followers2.txt')
    elif arg == 'g':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_following2.txt')
    elif arg == 'r':
        print('[INFO]: Followers list successfully saved to ' +
              targetAccount + '_results2.txt')


def find_files(filename):
    files = glob.glob('**/*.txt', recursive=True)
    if filename in files:
        return True
    else:
        return False

# END
