def is_prime(number):
    if(number < 0):
        raise ValueError
    elif(number <= 1):
        return False
    elif(number == 2):
        return True
    else:
        for i in range(2,number - 1):
            if(number % i == 0):
                return False
        return True





