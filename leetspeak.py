#This code will translate a given paragraph into Leetspeak

givenString = 'I now must type a paragraph which will then be passed through a for loop and change the paragraph to Leetspeek.'
leetLetters = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
leetNums = ['4', '3', '6', '1', '0', '5', '7']
givenString = givenString.upper()


for i in range(len(givenString)):
    for j in range(len(leetLetters)):
        if leetLetters[j] == givenString[i]:
            givenString = givenString.replace(givenString[i], leetNums[j])
print(givenString)