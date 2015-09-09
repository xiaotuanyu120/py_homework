class Var(object):
    class_var = 'class variable'
    def __init__(self, var):
        self.var = var
    def print_var(self):
        print self.var
        print self.class_var

if __name__ == '__main__':
    ins = Var('instance')

    ins.print_var()
#    print ins.class_var
