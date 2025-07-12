import math

def solve():
    n = int(input())
    px,py,qx,qy = map(int, input().split())
    a = list(map(int, input().split()))

    dist_pq = math.sqrt((px-qx)**2 + (py-qy)**2)

    a.append(dist_pq)

    b = sorted(a)

    if sum(b[:-1]) >= b[-1] :
        return("YES")
    else:
        return("NO")

def main():
    T= int(input())
    for _ in range(T):
        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()
    
