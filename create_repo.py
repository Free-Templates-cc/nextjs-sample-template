import subprocess
import time
import os

repos = open("repos.txt","r")
for x in repos:
    
    name = x.strip()
    description = name.replace("-", " ").title()

    createCommand = [
        "gh", "api",
         "--method", "POST",
         "-H", "'Accept: application/vnd.github+json'",
        "-H", "'X-GitHub-Api-Version: 2022-11-28'",
        "/orgs/Free-Templates-cc/repos", 
        "-f", "name=%s" % name,
        "-f", "description=%s" % description,
        "-f", "homepage=https://%s.netlify.app" % name,
        "-F", "private=true",
        "-F", "has_issues=true",
        "-F", "has_projects=true",
        "-F", "has_wiki=true" 
                     ]
    
    created = os.path.join("created",".%s" % name)
    if not os.path.exists(created):
        subprocess.run(createCommand, capture_output=True)

        f = open(created, "w")
        f.close()
        
        print("New Repo Created: %s" % name)

        time.sleep(30)

    
    