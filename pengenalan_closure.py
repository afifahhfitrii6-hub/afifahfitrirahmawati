def outer_func(numbers = []): 
    print(f"numbers: {numbers}") 
    
    def inner_func(): 
        print(f"max: {max(numbers)}")