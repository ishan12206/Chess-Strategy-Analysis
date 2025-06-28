"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

def mod_factorial(k):# new defined function for filling 1st rows and cols of probability matrix
    if k==1:
        return 1
    return mod_multiply(k,mod_factorial(k-1))


# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    probability_arr = [[0]*(bob_wins+1) for _ in range(alice_wins+1)]
    probability_arr[1][1] = 1#given that Alice and Bob both have won one match each
    
    for row in range(2,alice_wins+1):
        probability_arr[row][1] = mod_divide(1,mod_factorial(row))
    
    for col in range(2,bob_wins+1):
        probability_arr[1][col] = mod_divide(1,mod_factorial(col))


    for i in range(2,alice_wins+1):
        for j in range(2,bob_wins+1):
            x = mod_multiply(probability_arr[i][j-1],mod_divide(i,(i+j-1)))
            y = mod_multiply(probability_arr[i-1][j],mod_divide(j,(i+j-1)))
            probability_arr[i][j] = mod_add(x,y)
    
    return probability_arr[alice_wins][bob_wins]
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    probability_arr = [[0]*(t+1) for _ in range(t+1)]
    probability_arr[1][1] = 1
    
    for row in range(2,t+1):
        probability_arr[row][1] = mod_divide(1,mod_factorial(row))
    
    for col in range(2,t+1):
        probability_arr[1][col] = mod_divide(1,mod_factorial(col))


    for i in range(2,t+1):
        for j in range(2,t+1):
            probability_arr[i][j] = mod_add(mod_multiply(probability_arr[i][j-1],mod_divide(i,(i+j-1))),mod_multiply(probability_arr[i-1][j],mod_divide(j,(i+j-1))))

    mean = 0
    for k in range(-(t-2),t,2):
        mean = mod_add(mean,mod_multiply(k,probability_arr[(t+k)//2][(t-k)//2])) 
    
    return mean

# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    probability_arr = [[0]*(t+1) for _ in range(t+1)]
    probability_arr[1][1] = 1
    
    for row in range(2,t+1):
        probability_arr[row][1] = mod_divide(1,mod_factorial(row))
    
    for col in range(2,t+1):
        probability_arr[1][col] = mod_divide(1,mod_factorial(col))


    for i in range(2,t+1):
        for j in range(2,t+1):
            probability_arr[i][j] = mod_add(mod_multiply(probability_arr[i][j-1],mod_divide(i,(i+j-1))),mod_multiply(probability_arr[i-1][j],mod_divide(j,(i+j-1))))

            
    var  = 0
    for k in range(-(t-2),t,2):
        var = mod_add(var,mod_multiply(k**2,probability_arr[(t+k)//2][(t-k)//2])) 
    
    return var
    
print(calc_prob(97,74))
print(calc_expectation(74))
print(calc_variance(74))#same as mod_divide(74,3)
