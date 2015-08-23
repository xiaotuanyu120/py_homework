# coding=utf-8
#!/usr/bin/pythonp
# Filename:test_lower.py
s = '''
Have you thought about what you want people to say about you after you’re gone? Can you hear the voice saying, “He was a great man.” Or “She really will be missed.” What else do they say?
One of the strangest phenomena of life is to engage in a work that will last long after death. Isn’t that a lot like investing all your money so that future generations can bare interest on it? Perhaps, yet if you look deep in your own heart, you’ll find something drives you to make this kind of contribution---something drives every human being to find a purpose that lives on after death.
'''
# count how many letters in string s
#s=s.lower()
letter_keep = [i for i in range(len(s)) if s[i].isalpha()]
print 'Total letter : %s' % len(letter_keep) 

# dereplication string s
letter_unique = [j for j in list(set(s)) if j.isalpha()]

# make a dict by zip() to store the result of count
alpha_print = sorted(zip([list(s).count(l) for l in letter_unique],letter_unique))

# print result
for n in range(len(letter_unique)-1, -1, -1):
    print '%-s: %s' %(alpha_print[n][1],alpha_print[n][0])
