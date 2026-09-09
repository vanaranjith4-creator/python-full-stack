ranjith_details_sbi ={
    "Name" : 'ranjith',
    'adr' : '1234567890',
    'pan' : 'TZJPS564E',
    'ATMPIN' : '6600',
    'Balance' : 10000
}
All_attmps = 3
while All_attmps >0:
    user_pin = input('Enter you Atm pin: ')
    if user_pin in ranjith_details_sbi['ATMPIN']:
        print('Welcome to sbi ATM')
        choice_= int(input('Enter \n1.withdraw \n2.diposite: '))
        if choice_ == 1:
            with_m = int(input('Enter amount to withdraw: '))
            if with_m <= ranjith_details_sbi['Balance'] and with_m % 100 ==0:
                ranjith_details_sbi['Balance'] -= with_m
                print(f'take your cash and balance is {ranjith_details_sbi['Balance']} ')
            else:
                print(f'insuficiant balance or this Atm not provide change')
        elif choice_ ==2:
                depo_m = int(input('Enter ammount to deposite: '))
                if depo_m % 100 == 0:
                    ranjith_details_sbi['Balance'] += depo_m
                    print(f'amount is deposite and total balance is {ranjith_details_sbi['Balance']}')
                else:
                    print(f'This ATM is not accepts change')
        
        break
    else:
        All_attmps -= 1
        if All_attmps >0:
            print(f'incorrect pin entered and you have {All_attmps} left')
        else:
            print('your card is blocked')
