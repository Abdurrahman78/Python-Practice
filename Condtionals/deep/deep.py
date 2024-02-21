#implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No

#grab the users input
answer= input('What is the answer to the Great Question of Life, the Universe and Everything? ')

#print yes if the answer equals the required answer , else print no
if answer.strip() == '42':
    print('yes')

elif answer.lower() == 'forty-two':
    print('yes')

elif answer.lower() == 'forty two':
    print('yes')

else:
    print('No')
