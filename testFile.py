from django.core.files import File

with open('/test.txt', 'w') as f:
    myfile = File(f)
    myfile.write('hello world!')
    print myfile.name

myfile.closed
f.closed