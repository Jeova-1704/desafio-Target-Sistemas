def fibonnaci(n):
    fib_init = [0, 1]
    next_fib = 0

    while next_fib < n:
        next_fib = fib_init[-1] + fib_init[-2]
        fib_init.append(next_fib)
        
    return n in fib_init


if __name__ == "__main__":
    n = int(input("Digite um número: "))
    print(fibonnaci(n))