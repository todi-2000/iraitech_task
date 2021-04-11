#Question 3

# Function to find power
def power(base,exp):
    ans = 1
    while exp != 0:
        if exp % 2 != 0:
            ans *= base
            exp-=1;
        else:
            base *= base
            exp /= 2
    return ans
    
    
def math_function(x,y,a,b):
    val1 = power(x/y,a)
    val2 = power(x/y,b)
    return val1*val2
    
x = int(input())
y = int(input())
a = int(input())
b = int(input())
print(math_function(x,y,a,b))