import os
import subprocess
import time

var = os.system("ls -l")

print("=====")
subprocess.run(["ls","-l"])
subprocess.run(["cat","1-hello-world.py"])

# Perbedaan os vs subprocess
# 1. Subprocess menggunakan parameter tanpa spasi untuk mengurangi resiko error
# 2. OS itu async, berpotensi menyebabkan async-race
# 3. OS tidak bisa menangkap error sebagai error, error maupun success akan selalu dianggap string
# 4. Subprocces sync
# 5. OS akan decontinue di versi python kedepan
# Kesimpulan: Gunakan Subprocess sebagai replacement dari os