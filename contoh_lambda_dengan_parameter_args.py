# %% A.26.4. Lambda *args dan **kwargs 

def debug1(separator, *params): 
    res = [] 
    for i in range(len(params)): 
        res.append(f"param {i}: {params[i]}") 
        return separator.join(res) 
    
debug2 = lambda separator, *params : separator.join([f"param {i}: {params[i]}" for i in range(len(params))]) 

res = debug1(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True) 
print(res) 
# output ➜ param 0: Darion Mograine, param 1: ['Highlord', 'Horseman of the Ebon Blade', 'Ashbringer'], param 2: True 

res = debug2(", ", "Darion Mograine", ["Highlord", "Horseman of the Ebon Blade", "Ashbringer"], True) 
print(res) 
# output ➜ param 0: Darion Mograine, param 1: ['Highlord', 'Horseman of the Ebon Blade', 'Ashbringer'], param 2: True