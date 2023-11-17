sp=int(input('enter the number'))
cp=int(input('enter the number'))
if sp>cp:
    profit=sp-cp
    profit_parcentage=profit/cp*100
    print(profit_parcentage)
elif cp>sp:
    loss=cp-sp
    loss_parcentage=loss/cp*100
    print(loss_parcentage)
else:
    print('no profit no loss')