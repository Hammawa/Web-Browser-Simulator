#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of code:
#
# Author: Abdullah 1619949
# Collaborators/references: Stackoverflow
#----------------------------------------------------

from stack import Stack

def getAction():
    """Prompts the user for a valid command until one is given
       input: N/A
       output: a valid command given by the user"""
    invalid_response = True
    valid_actions = ['=', '<', '>', 'q']
    
    #conditions to get out of the while loop are not satisfied until the user provides a valid response
    
    while invalid_response:
        action = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
        if action not in valid_actions:
            print('Invalid Entry.')
        else:
            invalid_response = False
    return action

def goToNewSite(current, bck, fwd):
    """Prompts the user for the url of a novel site.
       Then proceeds to add the previous and currently entered URL into the bck stack before clearing the forward one.
       Input: The current  url, a reference to the Stack holding the webpage addresses to go back to, and a
       reference to the Stack holding the webpage addresses to go forward to
       Output: The url entered by the user"""
    url = input('URL: ')
    bck.push(current)
    fwd.items.clear()
    return url
    
def goBack(current, bck, fwd):
    """Takes a the valid command for going back to show the user the most recent webpage visited
       Input: The current  url, a reference to the Stack holding the webpage addresses to go back to, and a
       reference to the Stack holding the webpage addresses to go forward to
       Output: The webpage the user most recently viewed in the back stack""" 
    
    if bck.isEmpty() == False:
        fwd.push(current)
        current = bck.pop()
    else:
        print('Cannot go back.')
    return current
    
def goForward(current, bck, fwd):
    """Takes a the valid command for going back to show the user the most recent webpage visited
       Input: The current  url, a reference to the Stack holding the webpage addresses to go back to, and a
       reference to the Stack holding the webpage addresses to go forward to
       Output: The webpage the user most recently viewed in the forward stack"""  
    
    # when the forward stack has elements we do the opposite of what I did in the back function by pushing the current webpage into bck
    # also due to the way items need to be taken from the forward stack I used its list property so that they could be called in the right order
    
    if fwd.isEmpty() == False:
        bck.push(current)
        current = fwd.items[fwd.size() - 1]
        i = fwd.items.index(current)
        fwd.items.pop(i)
    else:
        print('Cannot go forward.')
    return current 
   

def main():
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        action = getAction()
        
        if action == '=':
            current = goToNewSite(current, back, forward)
        elif action == '<':
            current = goBack(current, back, forward)
        elif action == '>':
            current = goForward(current, back, forward)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    