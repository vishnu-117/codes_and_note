prime_number = []


def primenumber(number):
    for i in range(number):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    # print("not pirme number")
                    break
            else:
                prime_number.append(i)


primenumber(10)
print(prime_number)
