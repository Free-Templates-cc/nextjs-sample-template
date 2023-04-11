import os
import subprocess
import time

folders = open("folders.txt","r")

# create main repo folder
if not os.path.isdir("repo"):
    os.makedirs("repo")

for x in folders:
    line = x.strip()
    
    description = line.replace("-", " ").title()

    repoLink = "https://github.com/Free-Templates-cc/% s.git" % line
    folder = os.path.join("repo",line)
    
    created = os.path.join("created",".%s" % line)
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
        
        print(repoLink)
        subprocess.run(["git", "remote", "add", "origin", repoLink], cwd=folder)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder)
    
    print("--------------------------------------------------")
    time.sleep(120)
