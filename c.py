def bad_code():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                c.append(a[i] + b[j])
    print(c)

    d = "Hello, World!"
    e = d.split(" ")
    f = ""
    for g in e:
        f += g
    print(f)

bad_code()
