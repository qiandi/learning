shopList=["apple","mango","carrot","banan"]

print("I have",len(shopList),"items to purchase")

print("These items are:")
for item in shopList:
    print(item)

print("I also have to buy rice.")

shopList.append('rice')

print("My shopping list is low",shopList)

print("I will sort my list now")

shopList.sort()

print("Sorted shopping list is",shopList)

print("The first item I will buy is",shopList[0])

olditem = shopList[0]

del shopList[0]

print("I bought the",olditem)
print("My shopping list is now",shopList)