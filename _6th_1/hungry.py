"""feel hungry? we can make food for you"""

from chaocai import *
def maicai(cai):
    print "bought the %s" % cai
    return cai

def ask_to_buy(cai):
    print "pls buy %s for me" % cai
    return cai

if __name__ == "__main__":
    if raw_input("do you want buy vege yourself?(yes or no)") == "yes":
        cai = maicai("cabbage")
        zuocai(cai)
    else:
        cai = ask_to_buy("cabbage")
        buy(cai)
