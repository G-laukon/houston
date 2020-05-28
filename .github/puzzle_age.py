def puzzle_age():
    m = 0    
    while m < 10:
        older = 9*m
        age = 0        
        n = 0
        while age < 100:
            age_mom = age + older
            if int(str(age_mom)[::-1]) == age:
                n = n + 1
                if n == 6:
                    age_now = age
                
            age = age + 1
        if n == 8:
            print(age_now,older)
        m = m + 1
