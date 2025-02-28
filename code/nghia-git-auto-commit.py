import os
import subprocess
from datetime import datetime


paths = [
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu-private\nha-tro",
    
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\version-control-systems\nghia-git-auto-commit",
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\version-control-systems\nghia-gitconfig",
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\version-control-systems\nghia-template",
    
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\os\windows\nghia-windows-autohotkey",
    r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\os\windows\nghia-windows-unikey",


    # r"Đường dẫn bị sai",
    # r"C:\Users\Admin\Downloads\NghiaDownloads\NghiaGit\NghiaGithub\whynotnghiavu\nghia-git-auto-commit-test\c.py",
    # r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\version-control-systems\nghia-git-auto-commit-test\c.py",
    # r"C:\Users\Admin\Downloads\NghiaDownloads\NghiaGit\NghiaGithub\whynotnghiavu\nghia-git-auto-commit-test\test",
    # r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGitlab\whynotnghiavu\version-control-systems\nghia-git-auto-commit-test\test",

    # r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGithub\whynotnghiavu\order-ease\order-ease.code-workspace",
    # r"C:\Users\Admin\Desktop\link\NghiaDownloads\NghiaGit\NghiaGithub\whynotnghiavu\clean-architecture\tasks\note.md",



]


for path in paths:
    print(f"path = {path}")

    if not os.path.exists(path):
        print(f"Đường dẫn không tồn tại.")
        continue

    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")

    if os.path.isfile(path):
        print(f"Xử lý File.")
        os.chdir(os.path.dirname(path))
        subprocess.run(["git", "add", os.path.basename(path)])
        subprocess.run(["git", "commit", "-m", f"nghia-git-auto-commit {now}"])
        subprocess.run(["git", "push"])

    elif os.path.isdir(path):
        print(f"Xử lý Folder.")
        os.chdir(path)
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"nghia-git-auto-commit {now}"])
        subprocess.run(["git", "push"])
    else:
        print(f"Không phải File hoặc Folder.")
        exit()
