import os
import subprocess
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
foldersFile = os.path.join(dir_path,"folders.txt")
folders = open(foldersFile,"r")

# create main repo folder
repoPath = os.path.join(dir_path,"repo")
if not os.path.isdir(repoPath):
    os.makedirs(repoPath)

for x in folders:

    line = x.strip()
    
    print("- - - - - - - - - - - - - - - - - - - START: %s - - - - - - - - - - - - - - - - - - -" % line)

    description = line.replace("-", " ").title()

    repoLink = "https://github.com/Free-Templates-cc/% s.git" % line
    folder = os.path.join(dir_path,"repo",line)
    
    created = os.path.join(dir_path,"created",".%s" % line)
    if not os.path.exists(created):
        print("Repo: %s not yet created" % line)
        print("--------------------------------------------------")
        continue

    if os.path.isdir(folder):
        print("Directory '% s' already exist" % line)
        print("--------------------------------------------------")
        continue

    os.makedirs(folder)
    print("Directory '% s' created" % line)

    readmeFile = os.path.join(folder,"README.md")
    if not os.path.exists(readmeFile):
        print("README.md File for '% s' created" % line)
        f = open(readmeFile, "a")
        f.write("# %s" % description)
        f.write("\n\n`%s` is a ready-to-use template for building web applications using the Next.js framework. Next.js is a React-based web framework that enables server-side rendering, automatic code splitting, and efficient client-side routing. The %s provides a basic structure and set of features to help developers get started with Next.js quickly." % (description,description))
        f.write("\n\nhttps://free-templates.cc/template/%s" % line)
        f.close()

    gitFolder = os.path.join(folder,".git")
    if not os.path.isdir(gitFolder):
        print("Initializing Git in '% s' created" % line)
        print("--------------------------------------------------")
        subprocess.run(["git", "init"], cwd=folder)
        subprocess.run(["git", "branch", "-M", "main"], cwd=folder)
        subprocess.run(["git", "add", "."], cwd=folder)
        subprocess.run(["git", "commit", "-m", "initial commit"], cwd=folder)
        
        print("- - - Adding Git Remote: %s - - -" % repoLink)
        subprocess.run(["git", "remote", "add", "origin", repoLink], cwd=folder)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder)
    
    print("- - - - - - - - - - - - - - - - - - - 20 seconds pause - - - - - - - - - - - - - - - - - - -")
    time.sleep(20)
