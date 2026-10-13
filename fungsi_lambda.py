aggregate = lambda message, numbers, f: print(f"{message} is {f(numbers)}") 

numbers = [24, 67, 22, 98, 3, 50] 

def average1(numbers): 
    return sum(numbers) / len(numbers) 

aggregate("average", numbers, average1) 
# output ➜ average is 44.0 

average2 = lambda numbers : sum(numbers) / len(numbers) 
aggregate("average", numbers, average2) 
# output ➜ average is 44.0 

aggregate("average", numbers, lambda numbers : sum(numbers) / len(numbers)) 
# output ➜ average is 44.0