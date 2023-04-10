import os

mode = 0o666
folders = open("folders.txt","r")

# create main repo folder
if not os.exists("repo"):
    os.mkdir("repo", mode)

for x in folders:
    print(x)
    folder = os.path.join("repo",trim(x))
    if not os.exists(folder):
        os.mkdir(folder, mode)