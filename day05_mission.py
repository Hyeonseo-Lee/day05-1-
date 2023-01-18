#8.12
word = 'Got'
a_generator = ('Got' for i in range(10))
b_generator=(i for i in range(10))
c_generator=a_generator,b_generator
for k,l in c_generator:
    print(k, l)
