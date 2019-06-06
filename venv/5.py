# Dictionary | JSON(Explore)
dishes = {"dal":100, "paneer":200, "chicken":300}
print(dishes)
print(hex(id(dishes)))
print(type(dishes))

print(dishes["dal"],hex(id(dishes["dal"])))
print(dishes["paneer"],hex(id(dishes["paneer"])))
print(dishes["chicken"],hex(id(dishes["chicken"])))

print("dal" in dishes)
print(100 in dishes)
# Draw memory Representation of Dictionary