print()
stu=(input('What is the name of the student:').title())
print()
if stu=='Eliabe Gomes Araujo':
    print('-'*50)
    print('The student {} cannot be judged'.format(stu))
    print('-'*50)
    exit()
elif stu=='Eliabe Araujo':
    print('-'*50)
    print('No result')
    print('-'*50)
    exit()
else:      
   a=float(input('Type the first grade:'))
   s=float(input('Type the second grade:'))
   d=float(input('Type the third grade:'))
   f=float(input('Type the fourth grade:'))
from time import sleep
q=(a+s+d+f)/4
print()
print('{:.2f}'.format(q))
print()
print('Loading Result...')
sleep(3)
if q<5:
   print('The student {} did not pass'.format(stu))
else:
     print('The student {} has passed'.format(stu))
     exit()
print('Loading Result...')
sleep(3)
if q<5:
    if q>=4.5:
        print('the student {} must go to recovery'.format(stu))
if q<4.5:
    print('The student {} is flunk'.format(stu))
    print('Try again next year.')
