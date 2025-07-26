def solve():

    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]

    prev = 0
    curr = 0
    nh = 0

    for i in range(n):

        if a[i] == 1:
            curr = 0
            prev = 0
            continue

        if prev:
            prev = 0
            continue

        curr = curr+1
        

        if curr == k:
            prev = 1
            curr = 0
            nh+=1

    
    return nh

def main():
    T= int(input())
    for _ in range(T):
        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()
    
