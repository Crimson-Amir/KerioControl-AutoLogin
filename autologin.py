import subprocess
import requests

def get_ssid():
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return None

if get_ssid() != "Keyhan":
    print("Not connected to keyhan. Exiting.")
    exit()

# -- Proceed with login --
USERNAME = ""
PASSWORD = ""

payload = {
    "kerio_username": USERNAME,
    "kerio_password": PASSWORD,
    "login": "Login"
}

try:
    response = requests.post(LOGIN_URL, data=payload)
    if response.ok and "Logout" in response.text:
        print("✅ Logged in.")
    else:
        print("⚠️ Login failed.")
except Exception as e:
    print(f"❌ Error: {e}")
