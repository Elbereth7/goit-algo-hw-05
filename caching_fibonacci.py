def caching_fibonacci():
# Create and use cache dictionary to save and reuse fibonacci numbers
    cache = {}

    def fibonacci(n):
    # Count n-fibonacci number 
        if n <= 0:
            return 0
        elif n == 1:
            return 1        
        elif n in cache:
            return cache[n] # Returns number from cache dictionary if it already exists
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
            return cache[n] # If number does not exist in cache dictionary: count the number and return the result, save the number to cache
        
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))


