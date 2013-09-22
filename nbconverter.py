#!/Users/adam/virtual-ipydev/bin/ipython
"""
Attempt to create a one-step ipynb -> rst converter
"""
from IPython.nbconvert.exporters import RSTExporter

def export(nbname, outfilename=None):
    exportRST = RSTExporter()
    # exclude default paths
    exportRST.template_path = ['.','/Users/adam/repos/blog'] 

    (body,resources) = exportRST.from_filename(nbname)

    if outfilename is None:
        outfilename = nbname.replace("ipynb","rst")

    with open(outfilename,'w') as f:
        f.write(body)

    return body,resources

if __name__ == "__main__":
    import sys

    print sys.argv

    body,resources = export(*sys.argv[1:])
