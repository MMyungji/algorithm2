for _ in range(10):
    n = int(input())
    search = input()
    data = input()

    cnt = data.count(search)
    print(f"#{n} {cnt}")