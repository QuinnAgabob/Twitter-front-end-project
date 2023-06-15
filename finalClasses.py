# pip install pillow

class user():
    mostRecent = 0
    _users = []

    def __init__(self, pofileName, _userName, _password):
        self.bio = ''
        self.followers = []
        self.following = []
        self.posts = []
        self._userName = _userName
        self._password = _password
        self.feed = []
        self.pofileName = pofileName
        self.blocked = []
        user._users.append(self)
    """
    Logs in and tests credentials
    """
    def login(username, password):
        for x in range(len(user._users)):
            if username == user._users[x]._userName and password == user._users[x]._password:
                print(user._users[x].pofileName + ' logged in.\n')
                return user._users[x]
        print('Failed to login')
        return False

    """
    Runs as a screeen when opeing a profile of somene else 
    """
    def openProfile(self, fwend):
        print(
            fwend.pofileName + '\n'
            'Bio: ' + fwend.bio + '\n'
            'Followers: ' + str(len(fwend.followers)) + '\n'
            'Following: ' + str(len(fwend.following)) + '\n'
            'Bio: ' + fwend.bio + 'n'
        )
        if len(fwend.posts) > 0:
            for x in range(len(fwend.posts)):
                print(str(x) + '.)')
                fwend.printPost(fwend.posts[x])
            print('Follow: ' + str(len(fwend.posts)))
            print('Remove Friend: ' + str(len(fwend.posts) + 1))
            print('Block: ' + str(len(fwend.posts) + 2))
            print('unBlock: ' + str(len(fwend.posts) + 3))
            tmp = input('Enter what you would like do: ')
            if int(tmp) >= 0 and int(tmp) < len(fwend.posts):
                self.editPost(fwend.posts[int(tmp)])
            elif tmp == str(len(fwend.posts)):
                self.follow(fwend)
            elif tmp == str(len(fwend.posts) + 1):
                self.removeFollower(fwend)
            elif tmp == str(len(fwend.posts) + 2):
                self.block(fwend)
            elif tmp == str(len(fwend.posts) + 3):
                self.unBlock(fwend)
            elif tmp == str(len(fwend.posts) + 4) and self.isMod:
                self.ban(fwend)

    """
    edit a posts that a user made for themselves
    """
    def editPost(self, posty):
        self.printPost(posty)
        tmp = input('Would you like to:'
                    '\n1.) Like post\n'
                    '2.) Comment on post')
        if tmp == '1':
            self.like(posty)
        elif tmp == '2':
            txt = input('What comment would you like to make?')
            self.makeComment(posty, txt)




    """
    print 1 post and its comments
    """
    def printPost(self, posty):
        print(
            'Likes: ' + str(len(posty['likes'])) + '\n' +
            posty['user'].pofileName + ': ' + posty['caption'] +
            '\nComments (' + str(len(posty['comments'])) + '): '
        )
        if len(posty['comments']) > 0:
            for x in range(len(posty['comments'])):
                print(
                    posty['comments'][x]['user'].pofileName + ': ' + posty['comments'][x]['comment']
                )
    """
    print posts of user
    """
    def printSelfPost(self):
        print(self.pofileName)
        print('Followers: ' + str(len(self.followers)))
        print('Following: ' + str(len(self.following)))
        print('Posts: ' + str(len(self.posts)))
        if len(self.posts) > 0:
            for x in range(len(self.posts)):
                self.printPost(self.posts[x])
    """
    print posts of a specific account
    """
    def printPostOther(fwend):
        print(fwend.pofileName)
        print('Followers: ' + str(len(fwend.followers)))
        print('Following: ' + str(len(fwend.following)))
        print('Posts: ' + str(len(fwend.posts)))
        if len(fwend.posts) > 0:
            for x in range(len(fwend.posts)):
                fwend.printPost(fwend.posts[x])
    """
    prints an account(not posts)
    """
    def printAccount(self):
        print(
            self.pofileName + '\n'
            'Bio: ' + self.bio + '\n'
            'Followers: ' + str(len(self.followers)) + '\n'
            'Following: ' + str(len(self.following)) + '\n'
            'Bio: ' + self.bio + 'n'
        )
    """
    search for a user
    """
    def searchUser(self):
        fwend = input('Search for a profile: ')
        tmp = []
        y = 1
        for x in range(len(user._users)):
            if fwend in user._users[x].pofileName:
                print(str(y) + '.) ' + user._users[x].pofileName)
                tmp.append(user._users[x])
                y = y + 1
        if y > 1:
            z = input('Select a person: ')
            if 0 < int(z) < y:
                self.openProfile(tmp[int(z) - 1])
            else:
                print('That is not a correct selection')
        else:
            print('Sorry, there is no ' + fwend)

    """
    eedits acount. only works on users account
    """
    def editAccount(self):
        x = input(
            'What would you like to edit?\n'
            '1.) Public Name\n'
            '2.) Bio\n'
            '3.) Login Credentials\n'
            '4.) Back\n'
            'Input: '
        )
        if x == '1':
            tmp = input('Enter new public name: ')
            self.editPublicName(tmp)
        elif x == '2':
            tmp = input('Enter new bio: ')
            self.editBio(tmp)
        elif x == '3':
            newU = input('What is the new login username: ')
            newP = input('What is the new login password: ')
            self.editLoginCredentials(newU, newP)
    """
    Creates a post
    """
    def makePost(self, y):
        post = {'user': self, 'caption': y, 'num': user.mostRecent, 'likes': [], 'comments': []}
        self.posts.append(post)
        user.mostRecent = user.mostRecent + 1
    """
    prints feed
    this prints self post and the people who you follow
    This prints with the most new to be at the bottom
    """
    def printFeed(self):
        for x in range(len(self.following)):
            for y in range(len(self.following[x].posts)):
                self.feed.append(self.following[x].posts[y])
        for x in range(len(self.posts)):
            self.feed.append(self.posts[x])
        for x in range(len(self.feed)):
            if x > 0:
                if self.feed[x]['num'] < self.feed[x - 1]['num']:
                    y = self.feed[x]
                    self.feed[x] = self.feed[x - 1]
                    self.feed[x - 1] = y
        for x in range(len(self.feed)):
            self.printPost(self.feed[x])

    def editPublicName(self, diff):
        self.pofileName = diff


    def editBio(self, diff):
        self.bio = diff

    def editLoginCredentials(self, newU, newP):
        self._userName = newU
        self._password = newP

    def makeComment(self, post, text):
        post['comments'].append({'user': self, 'comment': text})

    def like(self, post):
        if self not in post['likes']:
            post['likes'].append(self)

    def removeFollower(self, fwend):
        if len(self.followers) > 0:
            if fwend in self.followers:
                self.followers.remove(fwend)
                fwend.following.remove(self)
                print(str(fwend.pofileName) + ' removed!')
            else:
                print('That username doesnt exist')
        else:
            print('You have no followers, loser')

    def unFollow(self, fwend):
        if len(self.following) > 0:
            if fwend in self.following:
                self.following.remove(fwend)
                fwend.followers.remove(self)
                print(str(fwend.pofileName) + ' removed!')
            else:
                print('That username doesnt exist')

    def follow(self, fwend):
        if (fwend not in self.blocked) and (self not in fwend.blocked) and (fwend not in self.following):
            self.following.append(fwend)
            fwend.followers.append(self)
            print(str(fwend.pofileName) + ' added!')
        elif fwend in self.blocked:
            print('You have them blocked')
        elif self  in fwend.blocked:
            print('They have you blocked')
        elif fwend  in self.following:
            print('You already are folllowing them')

    def block(self, enemy):
        if enemy not in self.blocked:
            self.blocked.append(enemy)
            if enemy in self.followers:
                self.followers.remove(enemy)
                enemy.following.remove(self)
            if enemy in self.following:
                self.following.remove(enemy)
                enemy.followers.remove(self)
            print(enemy.pofileName + ' is now blocked.')
        else:
            print(enemy.pofileName + ' is already blocked.')

    def unBlock(self, fwend):
        if fwend in self.blocked:
            self.blocked.remove(fwend)
            print(fwend.pofileName + ' is now unblocked.')
        else:
            print(fwend.pofileName + ' is not blocked.')

    """
    edits a post afteer inputing a post
    """
    def editPosts(self, post):
        x = '1'
        while x != '5':
            self.printPost(post)
            x = input(
                'What part of this post would you like to edit?\n'
                '2.) The caption\n'
                '3.) Remove A comment\n'
                '4.) Delete Post\n'
                '5.) Go back\n'
            )
            if x == '2':
                y = input('Enter the caption desired: ')
                post['caption'] = y
            elif x == '3':
                if len(post['comments']) > 0:
                    z = str(len(post['comments']))
                    while z != str(len(post['comments']) + 1):
                        for t in range(len(post['comments'])):
                            print(
                                str(t) + '.) ' + post['comments'][t]['user'].pofileName + ': ' + post['comments'][t][
                                    'comment'] + '\n'
                            )
                        print(str(len(post['comments']) + 1) + '.) Go back')
                        z = input('Which comment would you like to remove?: ')
                        if int(z) >= 0 and int(z) < len(post['comments']):
                            print(
                                'The comment: ' + post['comments'][int(z)]['comment']
                                + ' by user ' + post['comments'][int(z)]['user'].pofileName
                                + ' is now removed.\n'
                            )
                            post['comments'].pop(int(z))
                        else:
                            z == str(len(post['comments']) + 1)

                else:
                    print('There are no comments on this post yet.\n')
            elif x == '4':
                y = input(
                    'Are you sure you want to remove this post?\n'
                    '1/) Yes\n'
                    '2.) No'
                )
                if y == '1':
                    print('Post deleted\n')
                    self.posts.remove(post)
                    x = '5'
                elif y == '2':
                    pass
                else:
                    print('That is not an option')
            else:
                if x != '5':
                    print('That is not one of the options. Please select a number 1-5\n')


    def printFollowers(self, usery):
        print('Followers: ' + str(len(usery.followers)))
        for x in range(len(usery.followers)):
            print(str(x + 1) + ' ' + usery.followers[x].pofileName)
            ttt = x
        if len(usery.followers) <= 0:
            ttt = 0
        print(str(ttt + 2) + ' go back')
        tmp = input()
        if int(tmp) > 0 and int(tmp) <= len(usery.followers):
            self.openProfile(usery.followers[int(tmp)-1])

    def printFollowing(self, usery):
        print('Following: ' + str(len(usery.following)))
        for x in range(len(usery.following)):
            print(str(x + 1) + ' ' + usery.following[x].pofileName)
        print(str(x + 2) + ' go back')
        tmp = input()
        if int(tmp) > 0 and int(tmp) <= len(usery.following):
            user.openProfile(usery.following[int(tmp)-1])



class nonMod(user):
    def __init__(self, pofileName, _userName, _password):
        super().__init__(pofileName, _userName, _password)
        self.isMod = False


class mod(user):
    _users = user._users
    def __init__(self, pofileName, _userName, _password):
        super().__init__(pofileName, _userName, _password)
        self.isMod = True

    """
    def ban(self, toof):
        if self.isMod:
            for x in range(len(mod._users)):
                if toof.pofileName in mod._users[x].followers:
                    mod._users[x].followers.delete(toof.pofileName)
                if toof.pofileName in mod._users[x].following:
                    mod._users[x].following.delete(toof.pofileName)
                for y in range(len(mod._users[x].posts)):
                    for z in range(len(mod._users[x].posts[y].comments)):
                        if mod.pofileName in mod._users[x].posts[y].comments[z]['user'].pofileName:
                            mod._users[x].posts[y].comments.pop(z)
                mod._users.remove(toof)
                del toof
    """
    def printUsers(self):
        for x in range(len(user._users)):
            print(str(x) + '.) ' + user._users[x].pofileName)



"""
quinn = mod('QuinnBob87', 'Q', 'A')
grace = nonMod('GracieG', 'G', 'G')
quinn.follow(grace)
grace.removeFollower(quinn)
grace.removeFollower(quinn)
grace.block(quinn)
grace.unBlock(quinn)
quinn.printUsers()

quinn.makePost()
quinn.makePost()
quinn.posts[1]['comments'].append({'user': grace, 'comment': 'hi q t'})
quinn.posts[1]['comments'].append({'user': quinn, 'comment': 'taxx'})
quinn.posts[1]['comments'].append({'user': grace, 'comment': 'hi q tdastgsvcte'})

quinn.editPosts(quinn.posts[1])
quinn.printSelfPost()
"""



