import os


file_setup = os.path.abspath(__file__)
file_src = os.path.join(os.path.dirname(file_setup), "nghia-git-auto-commit.bat")


startup_folder = os.path.expanduser("~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
file_link = os.path.join(startup_folder, "nghia-git-auto-commit.bat")


try:
    if os.path.exists(file_link):
        os.remove(file_link)
        print(f"Đã xóa symlink: {file_link}")
    os.symlink(os.path.abspath(file_src), file_link)
    print(f"Tạo link: {file_link}")
except OSError as e:
    print(f"Lỗi: {e}")
