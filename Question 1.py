#Question 1

# Method 1
def summation(x,n):
    ans = 0
    previous = 1
    for i in range(n):
        ans += previous*(1/x)
        previous *= (1/x)
    return ans
    
#Method 2 using recursion
def summation_recursion(x,n):
    if n==0:
        return 0
    return ((1/x)**n)+summation_recursion(x,n-1)

