def add(a, b):
    c = a + b

    print('the answer is {}'.format(c))


print('this is addtion and you can inpur q to quit')
while True:
    a = input('the first')
    while a != 'q':
        try:
            a = float(a)
        except ValueError:
            print('you should input a  number')
            a = input('the first')
        else:
            break


    if a == 'q':
        break
    else:

      b = input('the second')
      while b != 'q':
          try:
              b = float(b)
          except ValueError:
              print('you should input a  number')
              b = input('the second')
          else:
              break

      if b == 'q':
          break
    result=a+b
    print(result)
    break


