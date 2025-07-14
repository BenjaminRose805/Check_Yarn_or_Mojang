# Check\_Yarn\_or\_Mojang

This project helps check which Minecraft Fabric mods use **Yarn** mappings, **Mojang** mappings, both, or neither.

It does so by:

✅ Cloning a list of mod repositories from GitHub.
✅ Letting you run `./gradlew dependencies` to inspect mapping usage.
✅ Helping verify whether a mod targets **Minecraft 1.20.1** (Fabric).
✅ Recording results into a shared **Google Sheet** for easy tracking and collaboration.

---

## 📋 Prerequisites

Before you run this project, make sure you have the following installed:

### 1. **Git**

Git is a version control system used to download and manage code from remote repositories like GitHub. It allows you to clone projects, track changes, and contribute code.

* Download Git from [git-scm.com](https://git-scm.com/downloads) and follow the installation instructions for your operating system.

* After installation, you may need to configure your name and email for Git:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  ```

* To check if Git is installed and working, run:

  ```bash
  git --version
  ```

  You should see output similar to:

  ```
  git version 2.42.0
  ```

If you’re new to Git, check out the [Pro Git book](https://git-scm.com/book/en/v2) for a gentle introduction.

---

### 2. **Python 3**

Required to run the `cloneRepo.py` script.

* Download from [python.org](https://www.python.org/downloads/)
* Check your version:

  ```bash
  python --version
  ```

  or

  ```bash
  python3 --version
  ```

---

### 3. **Java JDK 17 or newer**

Most Fabric mods for Minecraft 1.20.1 require at least Java 17.

* Download the JDK:

  * [Temurin / Adoptium JDK](https://adoptium.net/)
  * [Oracle JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)

* Check your Java version:

  ```bash
  java -version
  ```

  You should see something like:

  ```
  openjdk version "17.0.8" ...
  ```

---

### 4. **Gradle**

Most mod repos include Gradle Wrapper (`gradlew`), so you usually don’t need Gradle installed globally.
If you’d like to install it globally, visit [gradle.org/install](https://gradle.org/install/).

---

## 🚀 How to Use

### 1. Clone This Repo

```bash
git clone https://github.com/YOUR_USERNAME/Check_Yarn_or_Mojang.git
cd Check_Yarn_or_Mojang
```

---

### 2. Review or Edit `modlist.txt`

This project already includes a **`modlist.txt`** file containing a list of GitHub URLs for various Minecraft Fabric mods, one URL per line, for example:

```
https://github.com/Author/ExampleMod
https://github.com/SomeoneElse/CoolFabricMod
```

You can:

* Leave it as-is
* Add new mod URLs
* Remove any you’re not interested in

---

### 3. Run the Script

This checks which repos are missing locally and clones them into a `mods` folder:

```bash
python cloneRepo.py
```

or on some systems:

```bash
python3 cloneRepo.py
```

* If all mods are already cloned, you’ll see:

  ```
  ✅ All mods are already cloned.
  ```

* Otherwise, the script will clone any missing repositories.

---

## 🔎 How to Check Mappings

Once a mod repo is cloned under `mods/`, check which mappings it uses:

1. **Change into the repo folder.**

   ```bash
   cd mods/ExampleMod
   ```

2. **Run Gradle dependencies.**

   On macOS/Linux:

   ```bash
   ./gradlew dependencies
   ```

   On Windows:

   ```powershell
   gradlew.bat dependencies
   ```

3. Look for references such as:

   ```
   net.fabricmc:yarn:...
   ```

   → This means the mod uses **Yarn** mappings.

   Or:

   ```
   net.minecraft:minecraft-mapped...
   ```

   or:

   ```
   mojang-mappings
   ```

   → This indicates **Mojang** mappings.

If you see neither, the mod might not expose mapping details directly or could rely on other mechanisms.

---

## ✅ How to Verify Minecraft Version

Make sure each mod targets **Minecraft 1.20.1 (Fabric)** by checking:

* The `build.gradle` or `gradle.properties` file for lines like:

  ```gradle
  minecraft_version = 1.20.1
  ```

  or:

  ```gradle
  minecraft {
      version = "1.20.1"
  }
  ```

* Or look in the Gradle dependencies output for:

  ```
  net.fabricmc:fabric-loader:...
  net.fabricmc:yarn:1.20.1+build...
  ```

If it’s not 1.20.1, note the version so you know it may need updating.

---

## 📊 Tracking Results in Google Sheets

All mods listed in `modlist.txt` are tracked in a shared **Google Sheet** for easy collaboration:

👉 [**Open the Google Sheet**](https://docs.google.com/spreadsheets/d/12FrHxua2egSYZVTXXyI8enTTm_DoAELPMD16uvKW7Yo/edit?usp=sharing)

This sheet helps you:

* See which mods are cloned
* Record which mappings they use (Yarn, Mojang, both, or neither)
* Note the Minecraft version each mod targets

### How to Update the Sheet

After checking a mod’s mappings and version:

* Open the Google Sheet
* Find the mod in the list
* Enter one of the following values under the **Mappings** column:

  * `Yarn`
  * `Mojang`
  * `Both`
  * `Neither`

Optionally record:

* The mod’s exact Minecraft version
* Any other notes (e.g. build errors, special setup instructions)

This keeps the mod list organized and ensures everyone working on the project sees the same information.

---

## 🗂 Folder Structure

After running the script, your folder will look like this:

```
Check_Yarn_or_Mojang/
│
├── cloneRepo.py
├── modlist.txt
├── mods/
│   ├── ExampleMod/
│   ├── CoolFabricMod/
│   └── ...
└── README.md
```

---

## 🤝 Contributing

Feel free to:

* Add more mod URLs to `modlist.txt`
* Fork this repo and open PRs
* Suggest improvements

Let’s figure out who’s using Yarn, Mojang, both, or neither—and keep the results organized in the spreadsheet!

---

## 📄 License

MIT
