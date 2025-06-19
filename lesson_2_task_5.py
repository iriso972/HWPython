def month_to_season(number):
    if 1<= number <= 2:
        return "Зима"
    elif 3<= number <= 5:
        return "Весна"
    elif 6<= number <= 8:
        return "Лето"
    elif 9<= number <= 11:
        return "Осень"
    else: 
        return "Зима"
    
try:
    number = int(input("Введите номер месяца (1-12): ")) 
    print(month_to_season(number))  
    
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")   

    
    
    