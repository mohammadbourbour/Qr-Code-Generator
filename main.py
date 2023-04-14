"""
This File will show the saved Wi-Fi password's on target system

Made by : Mohammad boorboor
Email : m.boorboor315@gmail.com

"""

# Refrence

import subprocess
from termcolor import colored
import pyfiglet


def show_wifi_passwords():
    # My information
    email = "m.boorboor315@gmail.com"
    name = "Mohammad boorboor"

    # program information
    description = "This program displays saved Wi-Fi networks and their passwords."
    Banner = "Wi-Fi Show"

    # print program information
    print(colored(pyfiglet.figlet_format(Banner), color="green"))
    print(colored(description, color="green") + "\n")
    print(f"Made By : {name} \nEmail : {email}\n")

    # prompt user to proceed
    input("Press Enter to continue...")

    # get list of saved Wi-Fi profiles
    try:
        data = (
            subprocess.check_output(["netsh", "wlan", "show", "profiles"])
            .decode("utf-8")
            .split("\n")
        )
    except subprocess.CalledProcessError as e:
        print("An error occurred: ", e)
        return

    profiles = [i.split(":", 1)[1].strip() for i in data if "All User Profile" in i]

    # get Wi-Fi passwords for each profile
    ssid_passwords = {}
    for profile in profiles:
        try:
            results = (
                subprocess
                .check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
                .decode("utf-8")
                .split("\n")
            )
        except subprocess.CalledProcessError as e:
            print("An error occurred: ", e)
            continue

        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            ssid_passwords[profile] = results[0]
        except IndexError:
            ssid_passwords[profile] = ""

    # print results
    print("{:<30}|  {:<}".format("SSID", "Password"))
    print("-" * 45)
    for ssid, password in ssid_passwords.items():
        print("{:<30}|  {:<}".format(ssid, password))

    # prompt user to exit
    input("\nPress Enter to exit...")


if __name__ == '__main__':
    show_wifi_passwords()
    input()
