from __future__ import print_function
import getpass

def promptUser():
    "Prompts user to enter password"
    userInput = str(getpass.getpass("Please enter your password: "))
    return userInput

def checkCondition(userInput):
    "check whether the four conditions are met and stored the individual result in an array and return it"
    conditionCheck = [1, 1 , 1 ,1]
    if (len([c for c in userInput if c.islower()]) > 0) and (len([c for c in userInput if c.isupper()]) > 0):
        conditionCheck[0] = 0
    if (len([c for c in userInput if c.isdigit()]) > 0):
        conditionCheck[1] = 0      
    if ((len([c for c in userInput if c.isalpha()]) +
         len([c for c in userInput if c.isdigit()])) < len(userInput)):
        conditionCheck[2] = 0
    if (len(userInput) > 6):
        conditionCheck[3] = 0
    return conditionCheck
    
def outputCondition(conditions):
    "check and report the strength of the password and the conditions met/not met by the passwords"
    conditionStatement = ["At least one uppercase and one lowercase.",
                          "At least one digit.",
                          "At least one character that is not a letter or a digit.",
                          "At least 6 characters in length."]
    met = []
    notMet = []
    times = 0
    if (conditions.count(0) == 4):
        print("Your password is strong.")
    elif (conditions.count(0) == 3):
        print("Your password is high medium strength.")
    elif (conditions.count(0) == 2):
        print("Your password has medium strength.")
    elif (conditions.count(0) == 1):
        print("Your password is weak.")
    else:
        print("Your password is very weak")
    for index in conditions:
        if index == 0:
            met.append(conditionStatement[times])
        else:
            notMet.append(conditionStatement[times])
        times += 1
    print("This is the list of conditions you have met:" + "\n" + "\n".join(met))
    print("This is the list of conditions you failed to meet:" + "\n" + "\n".join(notMet))
        
def searchCommon(commonText, userInput, l, h, times):
    "search whether the input password matches any common words in the common.txt file and report the times of search"
    times += 1
    if (l > h):
        print("Took " + str(times) + " searches.")
    else:
        mid = int(l + (h - l)/2)
        if userInput == commonText[mid]:
            print("Took " + str(times) + " searches.")
            print("Your password is too common!")
        elif userInput < commonText[mid]:
            return searchCommon(commonText, userInput, l, mid - 1, times)
        else:
            return searchCommon(commonText, userInput, mid + 1, h, times)

def main():
    commonText = [line.strip() for line in open("/Users/dandanbang/Desktop/common.txt", 'r')]
    userInput = promptUser()
    while userInput != "finish":
        conditions = checkCondition(userInput)
        outputCondition(conditions)
        searchCommon(commonText, userInput, 0, len(commonText) - 1, 0)
        userInput = promptUser()

if __name__ == "__main__":
    main()
