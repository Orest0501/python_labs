import re
from zipfile import ZipFile


def main():
    with ZipFile("access.log.zip") as zip:
        zip.extractall()


with open("access.log.txt", "r") as zip_file:
    logs_file = zip_file.read().split("\n")

    allRequest = re.findall(".*\[23/Mar/2009:0[2-5]:[0-5][0-9]:[0-9][0-9] \+0100].*php.* HTTP/1\.[0-9]\" 3[0-9][0-9].*",
                            str(logs_file))
    print(len(allRequest))


