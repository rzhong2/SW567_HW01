def classify_triangle(a, b, c):
    if a<b+c and b<a+c and c<a+b:
        if a==b==c:
            print('equilateral triangle')
        elif a==b or a==c or b==c:
            print('isosceles triangle')
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('right triangle')
        else:
            print('scalene triangle')
    else:
        print('not a triangle')