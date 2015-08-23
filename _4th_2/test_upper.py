# coding=utf-8
#!/usr/bin/pythonp
# Filename:test_05.py
s = '''
Have you thought about what you want people to say about you after you’re gone? Can you hear the voice saying, “He was a great man.” Or “She really will be missed.” What else do they say?
One of the strangest phenomena of life is to engage in a work that will last long after death. Isn’t that a lot like investing all your money so that future generations can bare interest on it? Perhaps, yet if you look deep in your own heart, you’ll find something drives you to make this kind of contribution---something drives every human being to find a purpose that lives on after death.
'''
# count how many letters in string s
letter_count = 0
for i in range(len(s)):
    if s[i].isalpha():
        letter_count += 1
print 'Total letter : %s' %letter_count

# dereplication string s
letter_unique = list(set(s))
letter_alpha = ['null']
k = 0
for j in range(len(letter_unique)):
    if letter_unique[j].isalpha():
        letter_alpha[k] = letter_unique[j]
        k += 1
        letter_alpha += ['null']
letter_alpha.remove('null')

# make a dict to store the result of count
alpha_count = {}
list_s = list(s)
for l in letter_alpha:
    alpha_count[l] = list_s.count(l)

# print result
alpha_print = [(x,y) for y,x in alpha_count.items()]
alpha_print.sort(reverse=True)
for n in range(len(alpha_count)):
    print '%-s: %s' %(alpha_print[n][1],alpha_print[n][0])
