import random

user_input = input("Liste elemanlarını girin (virgülle ayırarak): ")
user_list = user_input.split(',')

random.shuffle(user_list)

print("Karıştırılmış liste:", user_list)
