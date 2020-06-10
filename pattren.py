def pattern(a):
        for i in range(0,a):
            for x in range(0,i):
               print('*',end=" ")
            print('\n')
a=int(input('Enter the rows value:'))
pattern(a)    


