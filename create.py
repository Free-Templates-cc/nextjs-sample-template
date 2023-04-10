import os
import subprocess

folders = open("folders.txt","r")

# create main repo folder
if not os.path.isdir("repo"):
    os.makedirs("repo")

for x in folders:
    line = x.strip()
    

    repoLink = "https://github.com/Free-Templates-cc/% s.git" % line
    folder = os.path.join("repo",line)
    
    if not os.path.isdir(folder):
        print("Directory '% s' created" % line)
        os.makedirs(folder)
    else:
        print("Directory '% s' already exist" % line)
    
    readmeFile = os.path.join(folder,"README.md")
    if not os.path.exists(readmeFile):
        print("README.md File for '% s' created" % line)
        f = open(readmeFile, "a")
        f.write("# % s" % line)
        f.close()

    gitFolder = os.path.join(folder,".git")
    if not os.path.isdir(gitFolder):
        print("Initializing Git in '% s' created" % line)
        subprocess.run(["git", "init"], cwd=folder)
        subprocess.run(["git", "branch", "-M", "main"], cwd=folder)
        subprocess.run(["git", "add", "."], cwd=folder)
        subprocess.run(["git", "commit", "-m", "\"initial commit\""], cwd=folder)
        
        print(repoLink)
        subprocess.run(["git", "remote", "add", "origin", repoLink], cwd=folder)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder)
