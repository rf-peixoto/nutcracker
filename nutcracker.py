import sys
import os
import subprocess

# ======================================================================== #
# nutcracker v0.1.0
# Basic fuzzing tool.
# ======================================================================== #

# Entry point:
print("                    ▄                                   ▀██")
print("▄▄ ▄▄▄   ▄▄▄ ▄▄▄  ▄██▄    ▄▄▄▄  ▄▄▄ ▄▄   ▄▄▄▄     ▄▄▄▄   ██  ▄▄    ▄▄▄▄  ▄▄▄ ▄▄")
print(" ██  ██   ██  ██   ██   ▄█   ▀▀  ██▀ ▀▀ ▀▀ ▄██  ▄█   ▀▀  ██ ▄▀   ▄█▄▄▄██  ██▀ ▀▀")
print(" ██  ██   ██  ██   ██   ██       ██     ▄█▀ ██  ██       ██▀█▄   ██       ██")
print("▄██▄ ██▄  ▀█▄▄▀█▄  ▀█▄▀  ▀█▄▄▄▀ ▄██▄    ▀█▄▄▀█▀  ▀█▄▄▄▀ ▄██▄ ██▄  ▀█▄▄▄▀ ▄██▄\n")

if len(sys.argv) != 3:
    print('[>] Usage: nutcracker [fuzzlist] ["command"]')
    sys.exit()
# ======================================================================== #
# Load fuzzlist:
print("[>] Loading fuzzlist.")
try:
    with open(sys.argv[1], "r") as fzlst:
        fuzz_list = fzlst.read().split("\n")
except Exception as error:
    print(error)
    sys.exit()

# ======================================================================== #
# Prepare logfile:
print("[>] Creating log file.")

# ======================================================================== #
# Fuzzing:
print("[>] Fuzzing!\n")
log = []
for input in fuzz_list:
    tmp = "{0} {1}".format(sys.argv[2], input).split(" ")
    #print("    ... {0}".format(tmp))
    try:
        subprocess.run(tmp, capture_output=True, shell=False, check=True)
    except Exception as error:
        print(error)
        log.append(str(error))

# ======================================================================== #
# Logging:
print("\n[>] Saving log.")
with open("nutcracker.log", "w") as fl:
    for entry in log:
        fl.write(entry + "\n")
# ======================================================================== #
print("[>] Done. Thank you for using nutcracker today. :)")
