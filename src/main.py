import subprocess

# ওয়াই-ফাই প্রোফাইলগুলির তালিকা পান
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split("\n")
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# প্রোফাইলগুলির মধ্যে লুপ চালিয়ে পাসওয়ার্ড পান
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        # পাসওয়ার্ড বের করুন
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{:<30} | {:<}".format(i, "ENCODING ERROR"))

input("Press Enter to exit...")