import math

print("используйте только цифры и точки")
while 0 == 0 :
 print("Введите широту исходной точки:")
 y = float(input())
 print("Введите долготу исходной точки:")
 x = float(input())
 print("Введите широту точки азимут которой надо найти:")
 y1 = float(input())
 print("Введите долготу точки азимут которой надо найти:")
 x1 = float(input())
 if y1 == y:
    print("Искомый азимут в градусах:")
    print(0)
    print("\n\n ___________________________________________")
    print("| Для завершения программы нажсимте ctrl+C  |")
    print("|___________________________________________|\n\n") 
    continue;
 ax = math.atan((x1 - x)/(y1 - y))
 print("Искомый азимут в градусах:")
 print(a = ax*180/3.1415926535897932384626433832795)
 print("\n\n ___________________________________________")
 print("| Для завершения программы нажсимте ctrl+C  |")
 print("|___________________________________________|\n\n")

 print("\n\n ___________________________________________")
 print("| antenna adjuster_  by keyj    _           |")
 print("|___________________________________________|\n\n")

 



