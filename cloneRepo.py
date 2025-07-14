import os
import subprocess

def check_missing_mods(modlist_file, mods_folder):
    missing = []

    with open(modlist_file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        repo_name = url.rstrip("/").split("/")[-1]
        repo_path = os.path.join(mods_folder, repo_name)

        if not os.path.exists(repo_path):
            missing.append(url)

    return missing


if __name__ == "__main__":
    missing_repos = check_missing_mods("modlist.txt", "mods")

    if missing_repos:
        print("These mods are not yet cloned:")
        for url in missing_repos:
            print(url)
            repo_name = url.rstrip("/").split("/")[-1]
            subprocess.run(["git", "clone", url, f"mods/{repo_name}"])
    else:
        print("✅ All mods are already cloned.")