import requests
import json
import pandas as pd
import csv
import os
import time

def get_devices(domain, api_key):
    url = ("https://" + str(domain) + ".okta.com/api/v1/devices")
    headers = {
        "Authorization": ("SSWS " + str(api_key)),
        "Accept": "Application/JSON"
    }
    request = requests.get(url=url, params="", headers=headers)
    return request.json()

def get_users(domain, api_key, device_id):
    url = ("https://" + str(domain) + ".okta.com/api/v1/devices/" + str(device_id) + "/users")
    headers = {
        "Authorization": ("SSWS " + str(api_key))
    }
    request = requests.get(url=url, headers=headers)
    return request.json()

def create_csv(data):
    file_path = './data.csv'
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
        print(f"CSV file '{file_path}' created successfully!")

def delete_file(filename, directory):
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
        print("Legacy data cleared")
    else:
        print(f"{filename} doesn't exist. No data to clear")

def delete_device(device_id, api_key, domain):
    headers = {
        "Authorization": ("SSWS " + str(api_key))
    }
    url = ("https://" + domain + ".okta.com/api/v1/devices/" + device_id)
    response = requests.delete(url=url, headers=headers)
    return response.json

def loading_animation(message):
    for i in range(4):
        print(f"{message}{'.' * i}", end='\r')
        time.sleep(0.5)
        print("\r" * (len(message) + i + 1), end="")

if __name__ == "__main__":
    #define some global vars 
    device_list = [['device_id', 'displayName', 'status', 'userName']]
    directory = './'
    filename = 'data.csv'
    print("Advisory Okta Device Manipulation Script")

    #get sensitive information
    credentials = {
        "api_key": input("Please paste in your Okta API key: "),
        "domain": input(f"Please enter your Okta domain (e.g., 'trial-8647798' for https://trial-8647798.okta.com/): ")
    }
    api_key = credentials["api_key"].strip()
    domain = credentials["domain"].strip()

    #get the devices and send user notification
    devices = get_devices(domain=domain, api_key=api_key)
    loading_animation("Scanning devices")

    #itterate through the device data
    for device in devices:
        device_id = device["id"]
        status = device["status"]
        displayName = device["profile"]["displayName"]

        #get each device's users 
        users = get_users(domain=domain, api_key=api_key, device_id=device_id)

        #itterate through the device users
        if users:
            for user in users:
                userName = (user["user"]["profile"]["firstName"] + " " + user["user"]["profile"]["lastName"])
                entry = (device_id, displayName, status, userName)
                device_list.append(entry)
        else:
            entry = (device_id, displayName, status, "No user associated with device")
            device_list.append(entry)

    #user interaction logic
    print(len(devices), "devices scanned")
    selection = input("What would you like to do:\n\t1. Write data to CSV\n\t2. Delete deactivated devices\n\t3. Delete devices with no users associated\n\t4. Quit\nSelection: ")
    if selection == "1":
        delete_file(filename, directory)
        create_csv(data=device_list)
        loading_animation("exiting")
    elif selection == "2":
        for device in devices:
            device_id = device["id"]
            status = device["status"]
            if status == "DEACTIVATED":
                delete_device(device_id, api_key, domain)
                print("Deleting device:", device_id)
        loading_animation("Exiting")
    elif selection == "3":
        loading_animation("feature coming soon")
    elif selection == "4":
        loading_animation("Exiting")
    else:
        loading_animation("Invalid selection. Exiting")
