num = float(input())

if (num<1024):
    print(num, " B")
elif (num>=1024 and num<(1024*1024)):
    print(int(num/1024), " KB")
elif (num>=1024*1024 and num<(1024*1024*1024)):
    print(int(num/(1024*1024)), " MB")
else:
    print(int(num/(1024*1024*1024)), " GB")
