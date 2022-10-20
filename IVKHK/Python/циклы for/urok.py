
# prost = []
# delitel = 0
# for num in range(2, 100):
#     for j in range(2, num):
#         if num % j == 0:
#             delitel = delitel + 1
#     if delitel == 0:
#         prost.append(num)
#     else:
#         delitel = 0
# print (prost)



for num in range(1, 100):
    s = 1
    for j in range(2, num):
        if num % j == 0:
            s += j
    if s == num:
        print(num)