print ('Hello, welcome to trivia!') #opening statements

ans = input ('Are you ready to play (yes/no):  ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input ('1. Which U.S President is featured on the $2 bill? ')#first question
    if ans.lower() == 'thomas jefferson':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

              
    ans = input ('2. Who was the first President of the United States? ')#second question
    if ans.lower() == 'george washington':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
          

    ans = input ('3. What is 2 + 3 + 4 + 5 - 3 ')#third question
    if ans == '11':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

            
    ans = input ('4. What is the name of the NBA basketball team in Miami, Florida? ')#fourth question
    if ans.lower() == 'the heat' or ans.lower() == 'the miami heat' :
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    print ('Thank you for playing, you got' ,score, 'questions correct.') #end game
    YourScore = (score/total_q) * 100

    print ('Your Score:', str(YourScore) + '%')  #print score total 
print ('Goodbye')
