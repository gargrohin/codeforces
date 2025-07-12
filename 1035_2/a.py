def solve():

    a,b,x,y = map(int, input().split())

    if a == b:
        return 0
    diff = b-a
    
    cost = 0
    if a < b:
        # we go up
        if x <=y:
            return diff*x

        while a < b:

            if a^1 > a:
                cost +=y
                a = a^1
            else:
                a = a+1
                cost +=x
        return cost
        
    if a > b:
        # we go down
        if a^1 == b:
            return y
        else:
            return -1

    return -1





def main():
    T= int(input())
    for _ in range(T):
        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()
    
