
def tonguoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

def amicable(n):
    amicable_pair = []
    for num in range(1, n + 1):
        partner = tonguoc(num)
        if partner > num and tonguoc(partner) == num :
            amicable_pair.append((num, partner))
    return amicable_pair

def main():
    try: 
        n = int(input("Nhap n: "))
        if n < 1:
            print("N phai la so nguyen duong")
        amicable_pairs = amicable(n)
        if len(amicable_pairs) == 0:
            print("Khong co cap amicable nao thoa man trong doan 1 -> ", n)
        else:
            print("Cac cap amicable thoa man trong doan 1 ->", n ," la: ")
            for pair in amicable_pairs:
                print(pair)
    except ValueError:
        print("Ban can nhap vao mot so nguyen")
if __name__ == "__main__":
    main()