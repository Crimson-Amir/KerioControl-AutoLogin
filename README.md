# 🔐 AutoLogin for Kerio Control Captive Portal

Automatically log into [Kerio Control](https://www.gfi.com/products-and-solutions/network-security-solutions/kerio-control) or similar captive portals when connecting to a Wi-Fi network — no more typing your username and password every day.

---

## 📌 Description

This simple Python tool logs you into a captive Wi-Fi login page (Kerio Control) **automatically** when you connect to a specific Wi-Fi network (e.g., `"keyhan"`).  

It is currently built and tested for **Windows**, using **Task Scheduler** to detect Wi-Fi connections and run the script only once when needed.

---

## ⚙️ Features

- ✅ Detects Wi-Fi SSID
- ✅ Auto-sends login request to captive portal
- ✅ Uses Windows Task Scheduler (no resource usage)
- ✅ Configurable with your credentials
- ✅ Easy to set up

---

## 📷 Demo

> _Coming soon!_ (or you can record a short screen capture showing it in action)

---

## 🖥️ Usage (Windows Only for Now)

### 1. Clone the Repository

```
git clone git@github.com:Crimson-Amir/KerioControl-AutoLogin.git
cd kerio-auto-login
```
### 2. Edit autologin.py
Replace USERNAME and PASSWORD with your login information.

adjust LOGIN_URL or field names if your Kerio login page is customized.


### 3. Edit login_script.bat
replace autologin.py path:

bash```@echo off
py "C:\full\path\to\autologin.py"```

### 4. Add to Task Scheduler

Press Win + S → type: Task Scheduler → Open

Click Create Task (not "basic task")

#### 🔒 General Tab:
- Name: AutoLogin Keyhan

- Check: Run whether user is logged in or not

- Check: Run with highest privileges

#### ⏰ Triggers Tab:
- Click New…

- Begin the task: On an event

- Settings:

  - Log: Microsoft-Windows-NetworkProfile/Operational

  - Source: NetworkProfile

  - Event ID: 10000 (connected to Wi-Fi)

- Click OK

This will trigger whenever a network is connected

#### ⚙️ Actions Tab:
- Click New

- Action: Start a program

- Program/script: "C:\Path\To\login_script.bat"

- Conditions Tab: Uncheck Start only if on AC power (so it runs on battery too)
<br/><br/>
## ✨ Contributions Welcome!
We'd love your help to bring support to more platforms!

Also welcome:

🔒 Secure credential storage
🖼️ GUI or tray icon version
🌍 Multi-router/captive-portal compatibility
🧪 Unit testing / CI
Just fork this repo and open a PR or issue — happy to collaborate 💬

