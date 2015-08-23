"""we provide the service of make food"""

__all__ = ["zuocai", "buy"]

def zuocai(cai):
    print "get your %s, will finish later" % cai
    qiecai(cai)
    dianhuo()
    fanchao(cai)
    zhuangpan(cai)

def buy(cai):
    print "buy the %s for you, will fire later" %cai
    zuocai(cai)

def qiecai(cai):
    print "cut %s" % cai

def dianhuo():
    print "fire is ready"

def fanchao(cai):
    print "stir fry %s for 5 minutes" % cai

def zhuangpan(cai):
    print "transfer %s to a plate" % cai
