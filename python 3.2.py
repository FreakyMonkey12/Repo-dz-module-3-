import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевіряємо вхідні дані
    if not (1 <= minimum <= maximum <= 1000):
        return []
    
  
    unique_numbers = set()
    
    
    while len(unique_numbers) < quantity:
        
        random_number = random.randint(minimum, maximum)
        
        unique_numbers.add(random_number)
    
   
    return sorted(list(unique_numbers))


lottery_numbers = get_numbers_ticket(1, 65, 8)
print("Ваші лотерейні числа:", lottery_numbers)