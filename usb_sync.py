#!/usr/bin/env python3
import time
import os
import subprocess
import sys

SOURCE = "/home/USER/projectfolder"  # IMPORTANT: PATH TO FOLDER YOU ARE SYNCING GOES HERE
USB_LABEL = "MYBACKUP"
SYNC_INTERVAL = 3  # Lower values sync faster but use more resources

def get_mount_point(label):
    result = subprocess.run(
        ["lsblk", "-o", "LABEL,MOUNTPOINT"], stdout=subprocess.PIPE, text=True
    )
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[0] == label:
            return parts[1]
    return None

def rsync_folder(src, dest):
    subprocess.run([
        "rsync", "-au", src + "/", dest + "/"
    ])

def main():
    while True:
        mount = get_mount_point(USB_LABEL)
        if not mount:
            print("USB removed. Exiting.")
            sys.exit(0)

        dest = os.path.join(mount, "projectfolder")  # IMPORTANT: NAME OF FOLDER YOU ARE SYNCING
        os.makedirs(dest, exist_ok=True)

        print("Syncing...")
        rsync_folder(SOURCE, dest)

        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    main()
