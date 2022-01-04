with open("tried_combinations.txt","a") as f:
    chars = '0123456789abcdef'
    for char in chars:    
        f.write(char*64+"\n")
