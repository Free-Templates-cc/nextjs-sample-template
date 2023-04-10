import os
import subprocess

folders = open("folders.txt","r")

# create main repo folder
if not os.path.isdir("repo"):
    os.makedirs("repo")

for x in folders:
    line = x.strip()
    print("Directory '% s' created" % line)
    folder = os.path.join("repo",line)
    
    if not os.path.isdir(folder):
        os.makedirs(folder)

    print("README.md File for '% s' created" % line)
    f = open(os.path.join(folder,"README.md"), "a")
    f.write("# % s" % line)
    f.close()

    subprocess.run(["cd", folder])
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "\"initial commit\""])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin","https://github.com/Free-Templates-cc/sintec-nextjs-starter-template.git"])
