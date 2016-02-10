
# jspark module for IBM Bluemix Spark Notebooks

This notebook is used to quickly install helper functions derived from the experiences of the IBM jStart team


### Installing the shared module


    import os.path
    if (os.system("[! -f /gpfs/global_fs01/sym_shared/YPProdSpark/user/$USER/.local/lib/python2.7/site-packages/jspark/coremagic.py ]")):
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

    Sweet, someone on your team has already installed the jspark module.
    Checking remote jspark repo for updates ...
    Done


### Pulling in all of module references


    # Pull in all functions present in coremagic
    from jspark import coremagic
    from jspark import objstormagic
    from jspark import teachmagic
    from jspark import dfmagic
    from jspark.coremagic import *
    from jspark.objstormagic import *
    from jspark.teachmagic import *
    from jspark.dfmagic import *

### Enabling automatic reload of helper modules


    # Run by Everyone once in their respective notebook
    # This loads the autoreload extension into your notebook
    %load_ext autoreload
    # Reload all modules imported with %aimport every time before executing the Python code typed. (ref: https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
    %autoreload 1
    # Import module ‘jspark.coremagic’ and mark it to be autoreloaded for %autoreload 1
    %aimport jspark.coremagic
    %aimport jspark.objstormagic
    %aimport jspark.teachmagic
    %aimport jspark.dfmagic
    %aimport

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload
    Modules to reload:
    jspark.coremagic jspark.dfmagic jspark.objstormagic jspark.teachmagic
    
    Modules to skip:
    


### Removing parenthesis ( ) requirement for function calls


    # Empty or 1 == Smart.  2 == Full  0 == Disabled (ref: https://ipython.org/ipython-doc/3/interactive/magics.html#magic-autocall)
    %autocall 2

    Automatic calling is: Full

