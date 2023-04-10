import os
import subprocess

folders = open("folders.txt","r")

# create main repo folder
if not os.path.isdir("repo"):
    os.makedirs("repo")

for x in folders:
    line = x.strip()
    description = line.replace("-", " ").title()

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
        f.write("# %s" % description)
        f.write("`%s` is a ready-to-use template for building web applications using the Next.js framework. Next.js is a React-based web framework that enables server-side rendering, automatic code splitting, and efficient client-side routing. The %s provides a basic structure and set of features to help developers get started with Next.js quickly." % (description,description))
        f.write("[https://free-templates.cc/template/%s]https://free-templates.cc/template/%s" % (line,line))
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
        subprocess.run(["git", "pull"], cwd=folder)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder)
