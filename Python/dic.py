import custom1;

dic={
    "test1":"sfsdfsd",
    "test2":1123,
    "test3":True
}

print("%s is test" % dic["test1"])

dic["test4"]="wrewerwer"

del dic["test1"]

for key,value in dic.items():
    print("key is %s,value is %s" % (key,value))

if "test2" in dic:
    print("test2 is eists")

custom1.sayhi()