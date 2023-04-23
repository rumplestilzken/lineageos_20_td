#! /usr/bin/python3

import os


def uncomment(path, line):
    file = open(path, "r")
    file_lines = file.read().split("\n")
    file.close()

    if file_lines[line - 1].startswith("#"):
        file_lines[line - 1] = file_lines[line - 1].split("#")[1]

#    print(file_lines)
    filew = open(path, "w")
    output = "\n".join(file_lines)
    # print(output)
    filew.write(output)
    filew.close()


def main():
    uncomment("/home/rumplestilzken/git/lineage-20-build-td/system/sepolicy/vendor/hal_fingerprint_default.te", 1)
    uncomment("/home/rumplestilzken/git/lineage-20-build-td/system/sepolicy/vendor/hal_graphics_allocator_default.te", 1)
    uncomment("/home/rumplestilzken/git/lineage-20-build-td/system/sepolicy/vendor/hal_graphics_composer_default.te", 1)
    uncomment("/home/rumplestilzken/git/lineage-20-build-td/system/sepolicy/vendor/rild.te", 2)


if __name__ == '__main__':
    main()
