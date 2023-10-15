

#Задание 1
a = int(input("Введите число: "))
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число не является простым")


#Задание 2
numbers = [5,9,1,4,8,3,1,6,2]
numbers2 = 1
while numbers2 < len(numbers):
     for i in range(len(numbers)-numbers2):
          if numbers[i] > numbers[i+1]:
               numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
     numbers2 += 1
print(numbers)


#Задание 3
def name(cur):
    most = cur[0]
    for i in range(1, len(cur)):
     if cur[i] > most:
      most = cur[i]
    return most
list = [1,2,3,4,5,6,7,8,9,10]
mostel = name(list)
print(mostel)


#Задание 4
def name2(a):
    if a == 1 or a == 2:
        return 1
    return name2(a - 1) + name2(a - 2)
b = int(input())
print(name2(b))


#Задание 5
s= ['tshhs','stdhsth','tshhs']
c=0
a=0
for i in s:
  if s.count(i)>=c:
   c=s.count(i)
a=i
print(a)