for _ in range(int(input())):
    og = input()
    mod = ''
    for let in og:
        mod += chr(ord(let)+3) if let.isalpha() else let

    inv = mod[::-1]
    half = len(inv)//2
    final = inv[:half]
    for let in inv[half:]:
        sub = chr(ord(let)-1)
        final += sub
    print(final)
