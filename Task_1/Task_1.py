
def caching_fibonacci():
    """
    Returns a Fibonacci function that uses recursion and caching.
    The cache is preserved between calls using a closure.
    """
    cache = {0: 0, 1: 1}  # base values
  
    def fibonacci(n: int) -> int:
        """Provides a Fibonacci function with caching."""
        if n < 0:
            return 0
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    cached_fib = caching_fibonacci()

    while True:
        user_input = input("Input a number or 'exit': ").strip().lower()

        if user_input == "exit":
            print("Good bye!")
            break

        try:
            n = int(user_input)
        except ValueError:
            print("Please enter an integer number")
            continue

        print(f"Fibonacci({n}) = {cached_fib(n)}")