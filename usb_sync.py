#!/usr/bin/env python3
import time
import os
import subprocess
import sys

SOURCE = "/mnt/4020D7E120D7DBCA/30DaysOfPython"
USB_LABEL = "MYBACKUP"
SYNC_INTERVAL = 5  # seconds

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
        "rsync", "-a", "--delete", src + "/", dest + "/"
    ])

def main():
    while True:
        mount = get_mount_point(USB_LABEL)
        if not mount:
            print("USB removed. Exiting.")
            sys.exit(0)

        dest = os.path.join(mount, "30DaysOfPythonBackup")
        os.makedirs(dest, exist_ok=True)

        print("Syncing...")
        rsync_folder(SOURCE, dest)

        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    main()
