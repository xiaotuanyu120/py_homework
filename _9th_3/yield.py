def say():
    for i in range(10):
        j = yield i
        print j

t = say()
for i in t:
    print 'haha', t.next()
    t.send(1)
