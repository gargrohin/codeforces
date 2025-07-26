def solve():

    x = int(input())
    digits = []
    while x:
        digits.append(x%10)
        x = int(x/10)
    
    return min(digits)


    




def main():
    T= int(input())
    for _ in range(T):
        ans = solve()
        print(ans)

if __name__ == "__main__":
    main()
    
