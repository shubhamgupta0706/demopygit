f1 = open('image_0123.jpg', 'rb')
f2 = open('ritika.JPG', 'wb')


for i in f1:
    f2.write(i)