menu_list = []

def show_bill() :
    total_price = 0
    print('----my product----')
    for i in range(len(menu_list)) :
        print(menu_list[i][0],menu_list[i][1])
        total_price += int(menu_price)
    print('Total Price : ',total_price)
while True :
    menu_name = input('please select menu : ')
    if menu_name.lower() == 'exit' :
        break
    else :
        menu_price = input('price : ')
        menu_list.append([menu_name,menu_price])
show_bill()

