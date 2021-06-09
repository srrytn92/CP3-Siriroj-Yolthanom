menu = {'ข้าวมันไก่ต้ม':40,'ข้าวมันไก่ทอด':45,'ข้าวมันไก่ผสม':45}
menu_list = []

def show_bill() :
    total_price = 0
    print('----my product----')
    for i in range(len(menu_list)) :
        print(menu_list[i][0],menu_list[i][1])
        total_price += int(menu_list[i][1])
    print('Total Price : ',total_price)
while True :
    print(menu)
    print('If you exit menu please input "exit"')
    menu_name = input('please select menu : ')
    if menu_name.lower() == 'exit' :
        break
    else :
        menu_list.append([menu_name,menu[menu_name]])
show_bill()