s = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
s = sorted(s, reverse=True)
Smax = 0
for i in range(len(s)):
    for j in range(i +1, len(s)):
        for k in range(j +1, len(s)):
            a = s[i]
            b = s[j]
            c = s[k]
            if a + b > c and a + c > b and b + c > a:
                P = (a + b + c) / 2
                S = (P * (P - a) * (P - b) * (P - c)) ** (1/2)
                if S > Smax:
                    Smax = S
print("Максимальная площадь треугольника", Smax)