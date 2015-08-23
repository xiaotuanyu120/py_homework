# coding=utf-8
#!/usr/bin/pythonp
# Filename:test_05.py
s = '''
Have you thought about what you want people to say about you after you’re gone? Can you hear the voice saying, “He was a great man.” Or “She really will be missed.” What else do they say?
One of the strangest phenomena of life is to engage in a work that will last long after death. Isn’t that a lot like investing all your money so that future generations can bare interest on it? Perhaps, yet if you look deep in your own heart, you’ll find something drives you to make this kind of contribution---something drives every human being to find a purpose that lives on after death.
'''

def str_to_dict(str_in):
    # dereplication string
    str_list_unique = list(set(str_in))
    str_list = list(str_in)
    letter_unique = [x for x in str_list_unique if x.isalpha()]
    # make a dict by zip() to store the result of count
    return dict(zip(letter_unique,[str_list.count(y) for y in letter_unique]))

# count how many letters in string s
#s=s.lower()
letter_keep = [i for i in s if i.isalpha()]
print 'Total letter : %s' % len(letter_keep) 

letter_dict = sorted(str_to_dict(s).items(), key=lambda x:x[1],reverse=True)
for j in range(len(letter_dict)):
    print '%-s: %s' %(letter_dict[j][0],letter_dict[j][1])
