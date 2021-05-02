#!/usr/bin/env python3
import instaloader
import argparse
import time
import getpass
import library.functions as f



# Set Variables

targetAccount = ''
session = instaloader.Instaloader()


# Define Functions

def welcome():
    print('''

  ------ ------  |      |  -----------
        |        ||     |  |
        |        | |    |  |
        |        |  |   |  |
        |        |   |  |  |----
        |        |    | |  |
        |        |     ||  |
  ------ ------  |      |  |


    Version: 2.0
    @anxiouscrypt

  ''')


# Extracts a lists of followers from the specified 'targetAccount'

def get_followers():
    print("[INFO]: Extracting followers' list from " + targetAccount + '...')
    session.login(login_username, login_password)
    profile = instaloader.Profile.from_username(session.context, targetAccount)

    usrs = []
    for usr in profile.get_followers():
        usrs.append(usr.username)
    return usrs


# Extracts a lists of following from the specified 'targetAccount'

def get_following():
    print("[INFO]: Extracting following list from " + targetAccount + '...')
    session.login(login_username, login_password)
    profile = instaloader.Profile.from_username(session.context, targetAccount)

    usrs = []
    for usr in profile.get_followees():
        usrs.append(usr.username)
    return usrs


# Extracts a lists of accounts that the specified 'targetAccount' follows but dont follow them back

def extract_accounts(following_list, followers_list):
    print('[INFO]: Extracting accounts...')
    usrs = set(following_list).difference(followers_list)
    return usrs


# Gets the user login data 

def authenticate():
    global login_username
    login_username = input(
        "[WELCOME]: Enter the Username you would like to login with:")
    time.sleep(2)
    global login_password
    login_password = getpass.getpass("[SECURE]: Enter your Password:")
    session__init__()
    return login_username, login_password


# Initiates session and checks if login data is valid

def session__init__():
    session = instaloader.Instaloader()
    print('[INFO]: Logging in..')
    session.login(login_username, login_password)  # (Regular login)
    # session.login('yzspam', 'arabus33')  # (My Login)
    print('[INFO]: Logged in')
    time.sleep(2)
    return True


# Parse Arguments

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--account", required=True,
                help="name of the account to be scraped for followers")

ap.add_argument("-s", "--followers", required=False,
                help="print the account's followers list", action="store_true")

ap.add_argument("-g", "--following", required=False,
                help="print the account's following list", action="store_true")

args = vars(ap.parse_args())

if args["account"]:
    targetAccount = format(args["account"])


authenticate()


followers = get_followers()
if args["followers"]:
    f.save(followers, 's', targetAccount)

following = get_following()
if args["following"]:
    f.save(following, 'g', targetAccount)


f.save(extract_accounts(following, followers), 'r', targetAccount)

# END