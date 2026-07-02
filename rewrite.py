import os
import subprocess

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

# Get the list of commits
log = run('git log --pretty=format:"%H|%an|%ae|%ad|%s" --reverse main')
commits = [line.strip('"').split('|', 4) for line in log.split('\n')]

# Save the current state
run("git checkout main")

# Create an orphan branch to rebuild history
try:
    run("git branch -D temp_branch")
except:
    pass
run("git checkout --orphan temp_branch")
run("git rm -rf .")

for hsh, author, email, date, msg in commits:
    print(f"Applying {hsh}: {msg}")
    # Restore files from the commit
    subprocess.run(f"git checkout {hsh} -- .", shell=True)
    
    if email == "georgian.deep.25@gmail.com" or author == "georgiandeep25-prog":
        author = "npmPiku"
        email = "priyankabalmiki2007@gmail.com"
        
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = author
    env["GIT_AUTHOR_EMAIL"] = email
    env["GIT_AUTHOR_DATE"] = date
    env["GIT_COMMITTER_NAME"] = author
    env["GIT_COMMITTER_EMAIL"] = email
    env["GIT_COMMITTER_DATE"] = date
    
    subprocess.run("git add .", shell=True, env=env)
    with open("temp_msg.txt", "w", encoding="utf-8") as f:
        f.write(msg)
    subprocess.run('git commit -F temp_msg.txt', shell=True, env=env)

# Swap branches
run("git checkout main")
run("git reset --hard temp_branch")
run("git branch -D temp_branch")
if os.path.exists("temp_msg.txt"):
    os.remove("temp_msg.txt")
print("History rewritten successfully!")
