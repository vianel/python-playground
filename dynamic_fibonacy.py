

def dynamic_fib(n, cache = {}):
    print(f"using {n} the cache is {cache}")
    if n == 0 or n == 1:
        return 1
    try:
        print(f"try clause ${n} and cache {cache}")
        return cache[n]
    except KeyError:
        tmp = dynamic_fib(n - 1, cache) + dynamic_fib(n-2, cache)
        print(f"key error got tmp {tmp} and cache {cache}")
        cache[n] = tmp
        return tmp


if __name__ == '__main__':
    inp = int(input('Choose: '))

    print(dynamic_fib(inp))
