#!/Users/adam/virtual-ipydev/bin/ipython
"""
Attempt to create a one-step ipynb -> rst converter
"""
import os
from nbconvert import RSTExporter

def export(nbname, outfilename=None):
    exportRST = RSTExporter()
    # exclude default paths
    exportRST.template_path = ['.',os.path.expanduser('~/repos/blog')]

    (body,resources) = exportRST.from_filename(nbname)

    if outfilename is None:
        outfilename = nbname.replace("ipynb","rst")

    with open(outfilename,'w') as f:
        f.write(body)

    return body,resources

if __name__ == "__main__":
    import sys

    print(sys.argv)

    body,resources = export(*sys.argv[1:])

    keys = sorted(resources['outputs'].keys())
    for key in keys:
        print(key)
        with open(key, 'wb') as fh:
            fh.write(resources['outputs'][key])
