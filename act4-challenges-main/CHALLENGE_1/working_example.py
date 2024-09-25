from __future__ import print_function
import argparse
from datetime import datetime as dt
import os
import sys

__authors__ = ["Destor", "Gonzales", "Kuan", "Martinez", "Tribunsay"]
__date__ = 20240925
__description__ = "Gather filesystem metadata of provided file and store it in the same file with enhanced design and formatting"


parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {} on {}".format(", ".join(__authors__), __date__)
)
parser.add_argument("FILE_PATH",
                    help="Path to the blank text file where metadata will be written")
args = parser.parse_args()

file_path = args.FILE_PATH

if not os.path.exists(file_path):
    print(f"[-] The file {file_path} does not exist.")
    sys.exit(1)


stat_info = os.stat(file_path)
metadata_lines = []


metadata_lines.append("**********************************")
metadata_lines.append("*                                *")
metadata_lines.append("*             RIZZISM          ***")
metadata_lines.append("*                                 ")
metadata_lines.append("********************************\n")


metadata_lines.append("=====================================================")
metadata_lines.append("                FILE METADATA INFORMATION             ")
metadata_lines.append("=====================================================\n")

if "linux" in sys.platform or "darwin" in sys.platform:
    metadata_lines.append(">> Change time          : {}".format(dt.fromtimestamp(stat_info.st_ctime)))
elif "win" in sys.platform:
    metadata_lines.append(">> Creation time        : {}".format(dt.fromtimestamp(stat_info.st_ctime)))
else:
    metadata_lines.append("[-] Unsupported platform {} detected. Cannot interpret creation/change timestamp.".format(sys.platform))


metadata_lines.append(">> Modification time    : {}".format(dt.fromtimestamp(stat_info.st_mtime)))
metadata_lines.append(">> Access time          : {}".format(dt.fromtimestamp(stat_info.st_atime)))
metadata_lines.append(">> File mode            : {}".format(stat_info.st_mode))
metadata_lines.append(">> File inode           : {}".format(stat_info.st_ino))
metadata_lines.append(">> Device ID            : {}".format(stat_info.st_dev))
metadata_lines.append(">> Number of hard links : {}".format(stat_info.st_nlink))
metadata_lines.append(">> Owner User ID        : {}".format(stat_info.st_uid))
metadata_lines.append(">> Group ID             : {}".format(stat_info.st_gid))
metadata_lines.append(">> File Size (bytes)    : {}".format(stat_info.st_size))
metadata_lines.append(">> Is a symlink         : {}".format(os.path.islink(file_path)))
metadata_lines.append(">> Absolute Path        : {}".format(os.path.abspath(file_path)))
metadata_lines.append(">> File exists          : {}".format(os.path.exists(file_path)))
metadata_lines.append(">> Parent directory     : {}".format(os.path.dirname(file_path)))
metadata_lines.append(">> Parent dir & file    : {} | {}".format(*os.path.split(file_path)))


metadata_lines.append("\n=====================================================")
metadata_lines.append("                 END OF FILE METADATA                 ")
metadata_lines.append("=====================================================\n")

metadata_lines.append("*****************************************************")
metadata_lines.append("*                                                   *")
metadata_lines.append("*        FILE METADATA HAS BEEN SUCCESSFULLY SAVED   *")
metadata_lines.append("*                                                   *")
metadata_lines.append("*****************************************************")

with open(file_path, 'w') as f:
    for line in metadata_lines:
        f.write(line + "\n")

print(f"Metadata with enhanced design has been written inside: {file_path}")
