import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '1234567890'
symbols = '!@#$%^\?/>><&*()~'



for i in range(1,5):
    Use_for = lower_case + upper_case +number +symbols
    length_for_password = 10
    generated_password = "".join(random.sample(Use_for, length_for_password))
    print(f"${i} no generated password is: ",generated_password,'\n')