# jspark install 
!pip install --user nothing
if (os.system("test -r /gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages/jspark/coremagic.py") == 0):
    print "Sweet, someone on your team has already installed the jspark module."
else:
    # Run by somebody in the group to update the common package
    print "Initializing and populating a local jspark git repo ..."
    !git --git-dir=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages/jspark.git --work-tree=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages init --shared=all jspark.git > /dev/null 2>&1
    !git --git-dir=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages/jspark.git --work-tree=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages remote add origin https://github.com/joshisa/jspark.git > /dev/null 2>&1
    print "Done"
print "Checking remote jspark repo for updates ..."
!git --git-dir=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages/jspark.git --work-tree=/gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages pull origin master > /dev/null 2>&1
print "Done"
# Pull in all functions present in coremagic
from jspark.coremagic import *
from jspark.objstormagic import *
from jspark.howdoi import *
from jspark.dfmagic import *
from jspark import coremagic
from jspark import objstormagic
from jspark import howdoi
from jspark import dfmagic
# Run by Everyone once in their respective notebook
# This loads the autoreload extension into your notebook
%load_ext autoreload
# Reload all modules imported with %aimport every time before executing the Python code typed. (ref: https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
%autoreload 1
# Import module ‘jspark.coremagic’ and mark it to be autoreloaded for %autoreload 1
%aimport jspark.coremagic
%aimport jspark.objstormagic
%aimport jspark.howdoi
%aimport jspark.dfmagic
%aimport
# Empty or 1 == Smart.  2 == Full  0 == Disabled (ref: https://ipython.org/ipython-doc/3/interactive/magics.html#magic-autocall)
%autocall 2
coremagic.setup()
