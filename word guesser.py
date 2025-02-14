import random  
import os  
import time

def get_word(ml):
  for j in range(len(ml)):  
    newList.append(ml[j])  
  return newList 
  
def user_choice(num_selections): 
  global word  
  time.sleep(.25)  
  word=input('\nEnter a number from 1-10 to determine your word: ')  
  while True:  
    try:  
      word=int(word)  
      if not(word>num_selections or word<1):  
       break 
      else:
        print('\033[0;31;48m\nYou entered an invalid number! Try again.\n\033[0;37;48m') 
        time.sleep(.5)
    except:
      print("\n\033[0;31;48mThat is not a number! Try again.\n\033[0;37;48m")  
      time.sleep(.5)
    word=input('Enter a number from 1-10 to determine your word: ')  
    
def in_guessed(guessed_list,letter):  
  for i in range(len(guessed_list)):  
    if guessed_list[i]==letter:  
      return True
  return False

# Main Program
words_list=['candidate','tourist','appeal','rice','bulb','clearance','atmosphere','retain','absorption','surround'] 
menu='o'  
games=0  
wins=0 
print('Welcome to Word Guesser!\n')  
while menu==1 or menu==2 or menu=='o':  
  print('\033[1;37;48mMENU\n\033[0;32;48m1. Play\n\033[0;36;48m2. Instructions\n\033[0;33;48m3. Stats\n\033[0;31;48m4. Quit')  
  menu=input('\033[0;37;48mEnter which number to proceed with: ')  
  while True:
    try:
      menu=int(menu)
      if not(menu>4 or menu<1): 
       break  
      else:
        print('\033[0;31;48m\nYou entered an invalid number! Try again.\n')  
        time.sleep(.25)
    except:
      print("\033[0;31;48m\nThat is not a number! Try again.\n")  
      time.sleep(.25)
    print('\033[1;37;48mMENU\n\033[0;32;48m1. Play\n\033[0;36;48m2. Instructions\n\033[0;31;48m3. Quit')
    menu=input('\033[0;37;48mEnter which number to proceed with: ')
    
  if (menu==2):  
    time.sleep(.25)
    print("\033[1;36;48m\nINSTRUCTIONS\n\033[0;37;48mYou will be given a random word that is blocked out with stars. It is your objective to guess all of the letters while making less than five mistakes. Make sure to keep your letters lowercase or else they will count towards your mistakes!\n")  
    time.sleep(1)

  if (menu==3):  
    print('\n\033[0;33;48mSTATS\033[0;30;48m\nGames played:',games,'\nGames won:',wins) 
    if (games!=0 and wins!=0):  #no games played or no wins
      print('You are at a',round((wins/games)*100,2),'% win rate')  
    else:  
      print('You are at a 0 % win rate')
    time.sleep(.5)
    print()
    menu='o'  
    
  while (menu==1): 
    play=0
    time.sleep(.25)
    print("\033[1;32;48m\nPLAY\n\033[0;37;48m1. Random\n2. Choose via number\n3. Back to Menu")  
    play=input('\033[0;37;48mEnter which number to proceed with: ')
    while True:
      try:  
        play=int(play)
        if not (play>3 or play<1):
          break
        else:
          print('\033[0;31;48m\nYou entered an invalid number! Try again.\n')  
      except:
        print("\033[0;31;48m\nThat is not a number! Try again.\n")
      print("\033[1;32;48m\nPLAY\n\033[0;37;48m1. Random\n2. Choose via number\n3. Back to Menu")  
      play=input('\033[0;37;48mEnter which number to proceed with: ')
      
    newList=[]  
    present_word=[] 
    guessed_letters=[]  
    wrong=0  
    
    if play==1:  
      word=random.randint(1,10)  
    if play==2:  
      user_choice(10)
    if play==3:
      menu='o'
      print()
      time.sleep(.25)

    if menu==1:  
      get_word(words_list[word-1])
      
      for i in range(len(newList)):
        present_word+=['*']
      print('\033[0;34;48m\nYour word has',len(newList),'letters!')
      time.sleep(.25)
      
      while ('*'in present_word):
        correct=0
        print('\033[0;37;48m\nWord: ',*present_word, sep='')
        guess=input('Enter a letter: ')
        for o in range(len(newList)):
          if guess==newList[o]:
            present_word.insert(o,newList[o])
            del(present_word[o+1])
            correct+=1
        if not('*'in present_word):
          print('\033[1;32;48m\nYou guessed the word:',words_list[word-1],'\033[0;33;48m\n With',wrong,'mistake(s)!\n')
          games+=1
          wins+=1
          time.sleep(.5)
        if (in_guessed(guessed_letters,guess)):
          print('\033[0;35;48m\n You already guessed this letter!!!!!')
          time.sleep(.25)
        if correct>0:
          if in_guessed(guessed_letters,guess):
            print()
          elif ('*' in present_word):
            print('\033[0;32;48m\n',guess,'is in the word!')
            time.sleep(.25)
        if (correct==0):
          if in_guessed(guessed_letters,guess):
            print()
          else:
            wrong += 1
            if wrong<5:
              print("\033[0;33;48m\n Sorry, that letter is not in the word. You have made", wrong, "mistake(s).")
            time.sleep(.25)
        if (wrong >= 5):
          print("\033[1;31;48m\nGame over! You lost. You have made too many mistakes.\n")
          games+=1
          time.sleep(.5)
          present_word.clear()
        guessed_letters+=[guess]
       
  if (menu==4):
    time.sleep(.5)
    os.system('clear') 
