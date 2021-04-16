#!/usr/bin/env python3

import instaloader
import argparse
import getpass
import time


print('''

------ ------  |      |  -----------
      |        ||     |  |
      |        | |    |  |
      |        |  |   |  |
      |        |   |  |  |----
      |        |    | |  |
      |        |     ||  |
------ ------  |      |  |


		Version: 1.1
		@anxiouscrypt

	''')



L = instaloader.Instaloader()


# parse arguments and get account name and percentage of followers to be extracted

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--account", required=True,
	help="name of the account to be scraped for followers")

args = vars(ap.parse_args())

targetAccount = ""
login_username = ""
login_password = ""


if args["account"]:
	targetAccount = format(args["account"])


# Get Login Credentials

login_username = input("[WELCOME]: Enter the Username you would like to login with:")

time.sleep(2)

login_password = getpass.getpass("[SECURE]: Enter your Password:")

# Login or load session

print('[INFO]: Logging in..')

L.login(login_username, login_password)        # (login)

print('[INFO]: Logged in')

time.sleep(2)


# Obtain profile metadata

profile = instaloader.Profile.from_username(L.context, targetAccount)


# Print list of followees

print("[INFO]: Extracting followers' list from " + targetAccount + '...')

follow_list = []

file = open(targetAccount + "_followers.txt","w")

count=0

for followee in profile.get_followers():
    follow_list.append(followee.username)
    file.write(follow_list[count])
    file.write("\n")
    count=count+1
file.close()

print('[INFO]: Followers list successfully saved to ' + targetAccount + '_followers.txt')


# Print list of followees

print("[INFO]: Extracting following's list from " + targetAccount + '...')
following_list = []

file = open(targetAccount + "_following.txt","w")

count=0

for following in profile.get_followees():
    following_list.append(following.username)
    file.write(following_list[count])
    file.write("\n")
    count=count+1
file.close()

print('[INFO]: Following list successfully saved to ' + targetAccount + '_following.txt')


# Extract list of accounts that follow but dont follow back

print('[INFO]: Extracting accounts...')

time.sleep(2)
followers_input_file = targetAccount + "_followers.txt"
following_input_file = targetAccount + "_following.txt"

Following_File = open(following_input_file, "r")
Following = [(line.strip()) for line in Following_File]
Following_File.close()

Followers_File = open(followers_input_file, "r")
Followers = [(line.strip()) for line in Followers_File]
Followers_File.close()

result = set(Following).difference(Followers)


# Print that List

print('[INFO]: Saving to ' + targetAccount + '_results.txt...')

File = open(targetAccount + "_results.txt", "w")

for name in result:
	File.write(name + '\n')

File.close()
time.sleep(2)

print('[INFO]: List successfully saved to ' + targetAccount + '_results.txt')
