import shutil
import os
import subprocess

usb_drive_letter = "G:"  # Update with the appropriate drive letter of your USB drive
destination_folder = "pdf"  # Name of the destination folder to store the copied PDF files

def copy_pdf_files(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".pdf"):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copy(source_path, destination_path)

def monitor_usb_drive():
    command = f'WMIC LOGICALDISK WHERE "DriveType=2" GET DeviceID'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    drive_letters = [drive.decode().strip() for drive in output.split()[1:]]

    while True:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        new_output, _ = process.communicate()
        new_drive_letters = [drive.decode().strip() for drive in new_output.split()[1:]]

        # Check if any new drive has been inserted
        inserted_drives = list(set(new_drive_letters) - set(drive_letters))
        if inserted_drives:
            for drive_letter in inserted_drives:
                drive_path = os.path.join(drive_letter, "")
                if os.path.isdir(drive_path):
                    source_folder = drive_path
                    destination_folder_path = os.path.join(destination_folder, "")
                    if not os.path.exists(destination_folder_path):
                        os.makedirs(destination_folder_path)
                    copy_pdf_files(source_folder, destination_folder_path)
                    print(f"PDF files from {source_folder} have been copied to {destination_folder_path}")

        drive_letters = new_drive_letters

# Start monitoring the USB drive
monitor_usb_drive()
