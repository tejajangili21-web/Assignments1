def is_pronic_number(num):
 for m in range(1, int(num**0.5) + 1):
     if m * (m + 1) == num:
        return True
        return False
print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
 if is_pronic_number(i):
    print(i, end=" | ")
