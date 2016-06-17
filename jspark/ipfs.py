

############################################################################
#                                                                         ##
# IMPORTANT:  RERUN THIS CELL AFTER executing the above load command      ##
#                                                                         ##
############################################################################

# Useful Reading
#   -   https://ipfs.io/ipfs/QmNhFJjGcMPqpuYfxL62VVB9528NXqDNMFXiqN5bgFYiZ1/its-time-for-the-permanent-web.html
#   -   https://netninja.com/2015/09/30/ipfs_interplanetary_file_system/

# Purpose:  Installation of IPFS (InterPlanetary File System) within Jupyter
#           IPFS is a peer-to-peer distributed file system that seeks to 
#           connect all computing devices with the same system of files.
#           In some ways, IPFS is similar to the World Wide Web, but IPFS 
#           could be seen as a single BitTorrent swarm, exchanging objects 
#           within one Git repository. IPFS has no single point of failure,
#           and nodes do not need to trust each other.
#           The filesystem can be accessed in a variety of ways, including 
#           via FUSE and over HTTP. A local file can be added to the IPFS 
#           filesystem, making it available to the world. Files are identified 
#           by their hashes, so it's caching-friendly. They are distributed 
#           using a BitTorrent-based protocol. (source: Wikipedia)
# Status:  Alpha (Experimental)
# Use Case Possibilities:  
#   1. Easier sharing of data analysis result sets
#   2. Easier access to popular open data sets via a permanent url
#   3. Easier transfer of assets between notebook servers on different infra
# Author:  Sanjay Joshi  joshisa (at) us(dot)ibm(dot)com
# License: Apache 2.0
# Organization:  IBM jStart (http://ibm.com/jstart)

import sys
import os
import subprocess as sub
import signal
import time
import IPython.display
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


# Print Working Directory
prefix = os.getcwd()
proposed = os.sep.join(prefix.split(os.sep)[:-2])
if os.access(proposed, os.W_OK):
    print("Prefix proposal accepted")
    prefix = proposed
elif os.access(prefix, os.W_OK):
    print("Prefix original accepted")
    prefix = prefix
else:
    sys.exit("No writeable directory found")

# Let's setup useful paths
localDir = prefix + "/.local"
shareDir = prefix + "/.local/share"
packageDir = localDir
workSpaceDir = shareDir + "/work_ipfs"
ipfsDir = shareDir + "/ipfs"
ipfsHomeDir = ipfsDir + "/go-ipfs"
ipfsRepoDir = shareDir + "/ipfsrepo"
goDir = shareDir + "/go-download"
goHomeDir = goDir + "/go"

# Let's make sure all of the paths are created if they don't exist
!mkdir $localDir 2> /dev/null
!mkdir $shareDir 2> /dev/null
!mkdir $packageDir 2> /dev/null
!mkdir $ipfsDir 2> /dev/null
!mkdir $goDir 2> /dev/null
!mkdir $workSpaceDir 2> /dev/null
!mkdir $ipfsRepoDir 2> /dev/null

# Let's now define some IMPORTANT env vars
os.environ["GOROOT"] = goHomeDir
os.environ["PATH"] += os.pathsep + goHomeDir + "/bin"
os.environ["PATH"] += os.pathsep + ipfsHomeDir
os.environ["GOPATH"] = ipfsDir
os.environ["IPFS_PATH"] = ipfsRepoDir

print("prefix = " + prefix)
print("shareDir = " + shareDir)
print("Python packageDir = " + packageDir)
print("ipfs Dir = " + ipfsDir)
print("Go Install Dir = " + goDir)
print("IPFS Repo Dir = " + ipfsRepoDir) 

# Define an IPFS Helper Class
class ipfs():
    def __init__(self):
        cmd = ['ipfs', 'version']
        p = sub.Popen(cmd, stdout=sub.PIPE,
                   stderr=sub.PIPE)
        out, err = p.communicate()
        try:
            out = out.decode("utf-8")
            err = err.decode("utf-8")
        except:
            pass
        print(err)
        print(out)
        
    def daemonStart(self):
        p = sub.Popen("nohup ipfs daemon > nohup.out 2>&1 &", shell=True)
        (result, err) = p.communicate()
        time.sleep(5)
        output = !cat nohup.out
        log = '\n'.join(str(x) for x in output)
        print(log)

    def daemonStop(self):
        PID = !ps -ef | grep "\bipfs daemon\b" | awk '{print $2}'
        os.kill(int(PID[0]), signal.SIGTERM)
        time.sleep(5)
        log = !cat nohup.out
        log = '\n'.join(str(x) for x in output)
        print(log)
    
    def help(self):
        cmd = ['ipfs']
        p = sub.Popen(cmd, stdout=sub.PIPE,
                   stderr=sub.PIPE)
        out, err = p.communicate()
        try:
            out = out.decode("utf-8")
            err = err.decode("utf-8")
        except:
            pass
        print(err)
        print(out)
    
    def cmd(self, arg):
        !ipfs $arg > log.txt
        time.sleep(1)
        self.printfile("log.txt")
        
    def printfile(self, filename):
        with open(filename, 'r') as myfile:
            contents=myfile.read()
            try:
                contents = contents.decode("utf-8")
            except:
                pass
        print(contents)


# Let's test to see if ipfs already exists in this notebook workspace
isIPFSInstalled = os.path.isfile(ipfsHomeDir + "/ipfs")
isGOInstalled = os.path.isfile(goHomeDir + "/bin/go")
if isIPFSInstalled:
    print("Congratulations! IPFS is already installed within your notebook user space")
else:
    print("IPFS is NOT installed within this notebook's user space")
    print("Initiating installation sequence ...")
    if isGOInstalled:
        print("Congratulations! GO is already installed within your notebook user space")
    else:
        print("GO is NOT installed within this notebook's user space")
        print("    Downloading and Installing the Go binary")
        !wget https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz -O $goDir/go1.6.2.linux-amd64.tar.gz
        !tar -zxvf $goDir/go1.6.2.linux-amd64.tar.gz -C $goDir >/dev/null
        # Retest go existence
        isGOInstalled = os.path.isfile(goHomeDir + "/bin/go")
    print("    Downloading and Installing the IPFS binary")
    !wget https://dist.ipfs.io/go-ipfs/v0.4.2/go-ipfs_v0.4.2_linux-amd64.tar.gz -O $ipfsDir/go-ipfs_v0.4.2_linux-amd64.tar.gz
    !tar -zxvf $ipfsDir/go-ipfs_v0.4.2_linux-amd64.tar.gz -C $ipfsDir >/dev/null
    # Retest ipfs existence
    isIPFSInstalled = os.path.isfile(ipfsHomeDir + "/ipfs")
    print("Congratulations!! IPFS is now installed within your notebook")
    print("To validate, run the following command within a cell:")
    print("")
    print("        ipfs = ipfs()")
    print("        ipfs.help()")

