import re
import copy

image_url = re.compile('\.\. \|(image\d*)\| image:: (http.*)')
image_ref = re.compile('`\|(image\d*)\|`_')
imagefmt = ".. image:: {0}\n"
rawhtml = re.compile("\.\. raw:: html")


def fix_lines(fn):

    with open(fn) as f:
        lines = f.readlines()

    imdict = {}
    removelines = []
    newlines = copy.copy(lines)
    for ln,line in enumerate(lines):
        if image_url.match(line):
            imno,url = image_url.search(line).groups()
            imdict[imno] = url
            removelines.append(line)
        elif rawhtml.match(line):
            removelines.append(line)
            removelines.append(lines[ln+2])


    for ln,line in enumerate(lines):
        if image_ref.match(line):
            refs = image_ref.findall(line)
            newline=""
            for ref in refs:
                if ref in imdict:
                    newline += imagefmt.format(imdict[ref])
            newlines[ln] = newline

    for line in lines:
        if line in removelines:
            newlines.remove(line)

    d = {'last':''}
    def filterfunc(thing,d):
        if thing == d['last']:
            d['last'] = thing
            return False
        else:
            d['last'] = thing
            return True
    newlines = [line for line in newlines if filterfunc(line,d)]

    with open(fn,'w') as f:
        f.writelines(newlines)

    return newlines

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Fix some docs.')
    parser.add_argument('filenames',  type=str, nargs='+',
            help='things')
    
    args = parser.parse_args()

    for arg in args.filenames:
        fix_lines(arg)
    
