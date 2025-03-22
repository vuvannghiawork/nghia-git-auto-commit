import os
import subprocess
from datetime import datetime


paths = [
    # r"C:\Users\Admin\Desktop\NghiaGithub\api",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-git-auto-commit",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-template",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-vscode",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-autohotkey",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-manager-screenshots",
    # r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-unikey",
    # r"C:\Users\Admin\Desktop\NghiaGithub\Notes",
    # r"C:\Users\Admin\Desktop\NghiaGithub\windows",





    r"C:\Users\Admin\Desktop\NghiaGithub\api",
    r"C:\Users\Admin\Desktop\NghiaGithub\DemoWebFlux",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-notes",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-template",
    r"C:\Users\Admin\Desktop\NghiaGithub\SMR-BE",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-vscode",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows",
    r"C:\Users\Admin\Desktop\NghiaGithub\fastapi-template-project",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-autohotkey",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-clone-github",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-manager-screenshots",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-docker-compose",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-windows-unikey",
    r"C:\Users\Admin\Desktop\NghiaGithub\nghia-git-auto-commit",
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
