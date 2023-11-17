year =int(input('enter the number'))
if year%400==0:
    print('yes')
    if year%4==0:
        if year%100!=0:
            print('yes')
    
        
    else:
        print('no')
else:
    print('no')
