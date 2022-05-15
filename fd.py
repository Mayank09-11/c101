import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
      
import os


path = "/home"


print(os.path.join(path, "User/Desktop", "file.txt"))



path = "User/Documents"

# Join various path components
print(os.path.join(path, "/home", "file.txt"))


path = "/User"

print(os.path.join(path, "Downloads", "file.txt", "/home"))


path = "/home"

print(os.path.join(path, "User/Public/", "Documents", ""))

