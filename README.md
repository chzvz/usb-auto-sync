# USB Auto Sync for Linux

A simple, reliable tool that automatically syncs a folder on your computer
to a USB drive whenever the drive is plugged in. Designed for Debian/KDE but 
should work on most Linux systems with systemd and automounting.

**NOTE: Your USB must be formatted to EXT4 or NTFS.**

---

# Format if needed (erases all data from drive!)

To find USB NAME and FSTYPE:
```
lsblk -f
```
Format to EXT4 (best on linux):
```
sudo umount /dev/sda1    # Replace sda1 with name of your USB
sudo mkfs.ext4 -L MYBACKUP /dev/sda1    # -L sets label to 'MYBACKUP'
```
Format to NTFS (better if you need to access files on windows machine):
```
sudo umount /dev/sda1    # Replace sda1 with name of your USB
sudo mkfs.ntfs -f -L MYBACKUP /dev/sda1    # -L sets label to 'MYBACKUP'
```

# Installation

**1. Clone the repository**

```
git clone https://github.com/chzvz/usb-auto-sync.git
cd usb-auto-sync
```

**2. Edit the Python script**

Open the file:

```
nano usb_sync.py
```

Look for:

```
SOURCE = "/home/YOURUSER/projectfolder"
dest = os.path.join(mount, "projectfolder")
```

Edit these paths to match the folder you are backing up. 

Ctrl + O, Enter, Ctrl + X

**3. Copy the script into place**

```
sudo cp usb_sync.py /usr/local/bin/usb_sync.py
sudo chmod +x /usr/local/bin/usb_sync.py
```

**4. Edit the systemd path file**

This tells systemd which directory to watch.

Open:

```
nano systemd/usb-sync.path
```

Find:

```
PathModified=/home/YOURUSER/YourFolder
```

Change it to the same folder you set in the Python script:

**5. Install the systemd units**

```
mkdir -p ~/.config/systemd/user/
cp systemd/usb-sync.service ~/.config/systemd/user/
cp systemd/usb-sync.path ~/.config/systemd/user/
```

**6. Reload & enable systemd**

```
systemctl --user daemon-reload
systemctl --user enable --now usb-sync.path
```

Syncing will now automatically run whenever:

- your source folder changes  
- the USB is plugged in and mounted  

**Verify**

```
systemctl --user status usb-sync.path
systemctl --user status usb-sync.service
```

Both should show **active**.

# Uninstallation

```
systemctl --user disable --now usb-sync.path
systemctl --user disable --now usb-sync.service
rm ~/.config/systemd/user/usb-sync.service
rm ~/.config/systemd/user/usb-sync.path
systemctl --user daemon-reload
sudo rm /usr/local/bin/usb_sync.py
```

**Optional: remove logs**

```
rm -rf ~/usb_sync_logs/
```
