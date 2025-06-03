while True:
    try:
        c, tests = [int(x) for x in input().split()]
        l1 = input().lower()
        l2 = input().lower()
        dic = {}
        for a, b in zip(l1, l2):
            dic[a] = b
            dic[b] = a
        for _ in range(tests):
            phrase = input()
            result = ''
            for let in phrase:
                letlow = let.lower()
                sub = dic[letlow] if letlow in dic else let
                sub = sub.upper() if let.isupper() else sub
                result +=sub
            print(result)
        print()
    except EOFError: break
