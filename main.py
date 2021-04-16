#!/usr/bin/env pyhton3 
import instaloader
import argparse
import getpass
import time



# Parse Arguments

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--account", required=True,
  help="name of the account to be scraped for followers")

ap.add_argument("-s", "--followers", required=False,
  help="print the account's followers list", action="store_true")

ap.add_argument("-g", "--following", required=False,
  help="print the account's following list", action="store_true")


args = vars(ap.parse_args())


# Set Variables

targetAccount = ""


# Print welcome statment

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



targetAccount = ""

if args["account"]:
  targetAccount = format(args["account"])



# Get Login Credentials

login_username = input("[WELCOME]: Enter the Username you would like to login with:")
time.sleep(2)
login_password = getpass.getpass("[SECURE]: Enter your Password:")


# Login or load session

L = instaloader.Instaloader()
print('[INFO]: Logging in..')
L.login(login_username, login_password)        # (Regular login)
print('[INFO]: Logged in')
time.sleep(2)


# Obtain profile metadata

profile = instaloader.Profile.from_username(L.context, targetAccount)


# Print list of followers

print("[INFO]: Extracting followers' list from " + targetAccount + '...')

followers_list = []
for followee in profile.get_followers():
    followers_list.append(followee.username)

if args["followers"]:
  followers_file = open(targetAccount + "_followers.txt", "w")
  for usr in followers_list:
    followers_file.write(usr + '\n')
  followers_file.close()
  print('[INFO]: Followers list successfully saved to ' + targetAccount + '_followers.txt')


# Print list of followees

print("[INFO]: Extracting following's list from " + targetAccount + '...')

following_list = []
for following in profile.get_followees():
    following_list.append(following.username)

if args["following"]:
  time.sleep(1)
  following_file = open(targetAccount + '_following.txt', "w")
  for usr in following_list:
    following_file.write(usr + '\n')
  following_file.close()
  print('[INFO]: Followers list successfully saved to ' + targetAccount + '_followers.txt')




print('[INFO]: Extracting accounts...')

time.sleep(2)
result = set(following_list).difference(followers_list)


# Print that List

print('[INFO]: Saving to ' + targetAccount + '_results.txt...')

File = open(targetAccount + "_results.txt", "w")

for name in result:
  File.write(name + '\n')

File.close()
time.sleep(2)

print('[INFO]: List successfully saved to ' + targetAccount + '_results.txt')

# END