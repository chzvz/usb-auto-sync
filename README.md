# USB Auto Sync for Linux

A simple, reliable tool that automatically syncs a folder on your computer
to a USB drive whenever the drive is plugged in. Uses:

- Python
- rsync
- systemd (user services)

Designed for Debian/KDE but should work on most Linux systems with systemd and automounting.

---

## 🚨 Important Note: USB Filesystem

**Your USB must be formatted to EXT4.**

- EXT4 is reliable, fast, and preserves file permissions.  
- FAT32 has a 4 GB max file size and no permissions.  
- NTFS works but is slower and less reliable on Linux.  

If your USB is not EXT4, you can format it with:
```
sudo mkfs.ext4 /dev/sdX1
# Replace /dev/sdX1 with your USB device. This will erase all data on the drive.
