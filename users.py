import argparse
import sys
import os
import requests


if __name__ == '__main__':
    example = 'Examples:\n\n'
    example += "$ python3 users.py -w names.txt -o outfile"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=example)
    sgroup = parser.add_argument_group("Main Arguments")
    sgroup.add_argument("-w", metavar="[NAMES LIST]", dest='names', default=False, type=str, help="Wordlist of First and Last Names: \n Format: [First Name] [Last Name] for each line in the file", required=True)
    sgroup.add_argument("-o", metavar="[OUT FILE]", dest='outfile', default="pineapple.txt", type=str, help="Output file", required=False)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    try:
        os.remove("pineapple.txt")
    except:
        pass

    fin = []
    with open(args.names,"r") as names:
        for name in names:
            n = name.strip()
            try:
                fn = n.split(" ")[0].lower()
                ln = n.split(" ")[1].lower()
                combos = [fn, ln, fn+ln, ln+fn, fn + "." + ln, ln + "." + fn, fn + "_" + ln, ln + "_" + fn, fn[0] + ln, fn + ln[0], 
                ln[0] + fn, ln + fn[0], fn[0] + "." + ln, ln[0] + "." + fn, fn[0] + "_" + ln, ln[0] + "_" + fn, fn + "." + ln[0], ln + "." + fn[0], fn + "_" + ln[0], ln + "_" + fn[0]]
            except Exception as e:
                print(e)
                continue
            for c in combos:
                fin.append(c)

        names.close()

    with open(args.outfile, "w") as outfile:
        for f in fin:
            outfile.write(f + "\n")
        outfile.close()

