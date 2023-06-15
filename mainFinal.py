"""DESCRIPTION OF THE MODULE GOES HERE

Author: Quinn Agabob
Class: CSI-260-02
Assignment: Final
Due Date: March 8, 2019 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
Classes for working with Temperatures."""
from finalClasses import nonMod, mod, user
import pickle


quinn = mod('QuinnBob87', 'Q', 'A')
grace = nonMod('GracieG', 'G', 'G')
toma = nonMod('tomaB', 'T', 'B')
noah = nonMod('noahhh', 'N', 'S')
carly = nonMod('charles', 'C', 'C')
reece = nonMod('greesyreesy', 'R', 'R')

quinn.follow(grace)
quinn.follow(toma)
quinn.follow(noah)
quinn.follow(carly)
quinn.follow(reece)
grace.follow(quinn)
quinn.makePost('Hi guys')
quinn.makePost('Hello everyone')
toma.makePost('I love all dogs')
toma.makePost('my roomate smells')
noah.makePost('I do not smell bad')
carly.makePost('Noah smells bad')
reece.makePost('I do not smell very bad')


quinn.posts[1]['comments'].append({'user': grace, 'comment': 'hi q t'})
quinn.posts[1]['comments'].append({'user': quinn, 'comment': 'taxx'})
quinn.posts[1]['comments'].append({'user': grace, 'comment': 'hi q tdastgsvcte'})

x = 1
while x != 0:
    tmp = input('Please login to an account\nUsername: ')
    tnp = input('Password: ')
    loggy = user.login(tmp, tnp)
    if loggy:
        loggy.printSelfPost()
        z = ''
        while z != '7':
            print(
                'What would you like to do?\n'
                '1.) Print Feed\n'
                '2.) Manage Followers\n'
                '3.) Manage Following\n'
                '4.) Edit Profile\n'
                '5.) Search user\n'
                '6.) Make a new post\n'
                '7.) Log out\n'
                '8.) Shut down\n'
                '9.) Print own Account'
                )
            if loggy.isMod:
                print(
                    '10.) Print all users'
                )
            z = input()
            if z == '1':
                loggy.printFeed()
            elif z == '2':
                loggy.printFollowers(loggy)
            elif z == '3':
                loggy.printFollowers(loggy)
            elif z == '4':
                loggy.editAccount()
            elif z == '5':
                loggy.searchUser()
            elif z == '9':
                loggy.printSelfPost()
            elif z == '6':
                tmp = input('What is the caption?')
                loggy.makePost(tmp)
            elif z == '8':
                quit()
            elif z == '10':
                if loggy.isMod:
                    loggy.printUsers()
            elif z != '7':
                print('please pick a number')

