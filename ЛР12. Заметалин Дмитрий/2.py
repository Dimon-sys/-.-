#Вариант10
if __name__ == "__main__":
    def t(a, c):

        def p(x):
            return ((1-x)**2 + (1-x)**3 + (1-x)**4)/x
        
        return p(a) - p(c)**(-1)
    
    a = float(input('a='))
    c = float(input('c='))
    print(t(a, c))
    