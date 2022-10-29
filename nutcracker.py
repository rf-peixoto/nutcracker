import sys
import os
import subprocess

# ======================================================================== #
# nutcracker v0.1.0
# Basic fuzzing tool.
# ======================================================================== #

# Entry point:
print("\033[34m")
print("                    ▄                                   ▀██")
print("▄▄ ▄▄▄   ▄▄▄ ▄▄▄  ▄██▄    ▄▄▄▄  ▄▄▄ ▄▄   ▄▄▄▄     ▄▄▄▄   ██  ▄▄    ▄▄▄▄  ▄▄▄ ▄▄")
print(" ██  ██   ██  ██   ██   ▄█   ▀▀  ██▀ ▀▀ ▀▀ ▄██  ▄█   ▀▀  ██ ▄▀   ▄█▄▄▄██  ██▀ ▀▀")
print(" ██  ██   ██  ██   ██   ██       ██     ▄█▀ ██  ██       ██▀█▄   ██       ██")
print("▄██▄ ██▄  ▀█▄▄▀█▄  ▀█▄▀  ▀█▄▄▄▀ ▄██▄    ▀█▄▄▀█▀  ▀█▄▄▄▀ ▄██▄ ██▄  ▀█▄▄▄▀ ▄██▄\n")
print("\033[00m")

if len(sys.argv) != 3:
    print('\033[34m[*]\033[00m Usage: nutcracker [fuzzlist] ["command"]')
    sys.exit()
# ======================================================================== #
# Load fuzzlist:
print("\033[34m[>]\033[00m Loading fuzzlist.")
try:
    with open(sys.argv[1], "r") as wordlist:
        fuzz_list = wordlist.read().split("\n")
except Exception as error:
    print(error)
    sys.exit()

# ======================================================================== #
# Prepare logfile:
print("\033[34m[>]\033[00m Creating log file.")

# ======================================================================== #
# Fuzzing:
print("\033[34m[>]\033[00m Fuzzing!\n")
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
print("\n\033[34m[>]\033[00m Saving log.")
with open("nutcracker.log", "w") as fl:
    for entry in log:
        fl.write(entry + "\n")
# ======================================================================== #
print("\033[34m[>]\033[00m Done. Thank you for using nutcracker today. :)")
