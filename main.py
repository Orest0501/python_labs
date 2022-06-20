import re
from zipfile import ZipFile


def main():
    with ZipFile("access.log.zip") as zip:
        zip.extractall()


with open("access.log.txt", "r") as zip_file:

    RE_PATTERN = re.compile(
        ".*\[23/Mar/2009:0[2-5]:[0-5][0-9]:[0-9][0-9] \+0100].*php.* HTTP/1\.[0-9]\" 3[0-9][0-9].*")

    if __name__ == "__main__":
        qty = 0

        for line in zip_file.readlines():
            matcher = RE_PATTERN.findall(line)
            qty += len(matcher)
    print("Result: {}".format(qty))


