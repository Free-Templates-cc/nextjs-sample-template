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
        break
    
    gitFolder = os.path.join(folder,".git")
    if not os.path.isdir(gitFolder):
        break

    subprocess.run(["git", "remote", "add", "origin", repoLink], cwd=folder)
    subprocess.run(["git", "stash"], cwd=folder)
    subprocess.run(["git", "pull", "origin", "main", "--rebase"], cwd=folder)

    readmeFile = os.path.join(folder,"README.md")
    f = open(readmeFile, "w")
    f.write("# %s" % description)
    f.write("\n\n`%s` is a ready-to-use template for building web applications using the Next.js framework. Next.js is a React-based web framework that enables server-side rendering, automatic code splitting, and efficient client-side routing. The %s provides a basic structure and set of features to help developers get started with Next.js quickly." % (description,description))
    f.write("\n\nhttps://free-templates.cc/template/%s" % line)
    f.close()

    subprocess.run(["git", "add", "."], cwd=folder)
    subprocess.run(["git", "commit", "-m", "initial commit"], cwd=folder)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder)
