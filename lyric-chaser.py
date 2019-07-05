
# coding: utf-8

# # Lyric Chaser

# A fun and simple game that quizzes you on music lyrics!

# In[1]:


import os
import re

doc = './a_la_vibora_de_la_mar.txt'
source = []
source.append(open(doc,'r').read().split('\n'))

cancion = [l for a in source for l in a]


# In[2]:


linea = [l.split() for l in cancion]


# In[3]:


incomplete = []
for l in linea:
    incomplete.append(' '.join(l[:-1]))


# In[4]:


last_words = []
for l in linea:
    last_words.append(l[-1])


# In[5]:


print('Welcome! We are Luis and Alejandro, and this is Lyric-Chaser, a fun and simple game that quizzes you on music lyrics!')
print('\nPlease guess the last word of the following lyrics to {}\n'.format(os.path.basename(doc)))     
      


# In[12]:


def guess_lyric(user_input):
    lives = 3
    score = 0
    for w in range(len(last_words)):
        if lives == 0:
            break
        user_input = input(f'{incomplete[w]} ')        
        if user_input == last_words[w]:
            score += 1
        else:
            while user_input != last_words[w]:
                lives -= 1
                if lives != 0:
                    print(f'Try again! You have {lives} lives.')
                    user_input = input(f'{incomplete[w]} ')
                else:
                    print(f'You lose! Your score is {score} point(s).')
                    break
    if lives != 0:
        print(f'You win! Your score is {score} point(s).')    


# In[13]:


guess_lyric('word')

