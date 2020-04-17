import os
import time
#colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[40m'
   END = '\033[0m'
   CWHITE  = '\33[37m'

#check_connectio
os.system("pip2 install requests")

import requests
try:
  requests.get("https://m.facebook.com")
except requests.exceptions.ConnectionError:
	print"[+]CHECK YOUR CONNECTION INTERNET RE RUN PORGRAM"




clear="clear"
os.system(clear)


print color.BLUE
os.system("figlet F-tools")
print """
     {}
     ---------------------------------------------
     ===>\033[1;35;40m FOUNDERNAME:\033[1;34;40m   MZOIR_ZAKARIYA
     --------------------------------------------
     ===>\033[1;36;40mContact:\033[1;34;40         evenfantom@gmail.com
     ---------------------------------------------
     ===>\033[1;33;40mToolname:\033[1;34;40        Tools_for_teemux
     ---------------------------------------------
     ===>\033[1;32;40mrefer:https://github.com/mzoir
     ---------------------------------------------

[notice]:I'm not respomsable for any illegal work u do 
[notice]:don't hesate send me if u want
{}[notice]:tool is not complete yet, we have just random tools and wifi_hacking 

\n""".format(color.RED,color.RED)
def option():
   print """ {}=>Menu: 
         {} [1] Random Tools
         {} [2] Wifi_hacking 
         {} [3] Facebook_hacking
         {} [4] sms and call trick
         {} [5] Web scanning
         {} [6] Intagram hacking
         {} [7] TOR AND PROXY_CHECK
         {} [8] Brutefore (needed tor and root)
          [9] HACKING PHONE AND COMPUTERS
          [10]GO TO DARKWEB AND DARKNET
	 {} [00] exit
	  [99] BACK TO MAIN
         """.format(color.RED,color.PURPLE,color.GREEN,color.YELLOW,color.BOLD,color.UNDERLINE,color.CYAN,color.CWHITE,color.RED,color.PURPLE)
   print color.END
   x=raw_input("What's your choice: ")
   randomy(x)
   ex(x)
   WIFI(x)





def ex(x):
  if x=="99":
	print"[+]YOUR IN THE MENU"
	option()
  elif x=="00":
          print color.RED
          print"[>] the program will exit....."
          time.sleep(2)
          exit




 
def randomy(x):
   if x=="1": 
      print color.BOLD
      print """THIS LIST OF RANOM TOOLS:
	     {} [1]: CUPP
	     {} [2]: IPGEOLOCATION
	     {} [3]: old-yahoo-account-extracted
	     {} [4]: facebook-hacker
	     {} [5]: email-spammer
	     {} [6]: CrackFlix
             {} [99]:BACK TO MAIN
""".format(color.RED,color.PURPLE,color.GREEN,color.YELLOW,color.PURPLE,color.CWHITE,color.BLUE)
      print color.END
      y=raw_input("CHOICE ONE ACTOIN:")
      if y =="1":
	print color.YELLOW
	print"INSTALLING........CUPP"
        time.sleep(2)
	print color.BLUE				
	print"     =>THIS TOOL FOR MAKE PASSWORD LIST"
	print color.GREEN
	os.system("cd ..")					
        os.system("git clone https://github.com/Mebus/cupp")
        print"Go to the tool type ./cupp"
        option()
      elif y=="99":
       		option()
      elif y=="00":
          print color.RED
   	  print"[>] the program will exit....."
	  time.sleep(2)
	  exit
      elif y=="2":
         print color.YELLOW 
         print"INSTALLING...'\033[96m'IPGEOLOCATION"
	 time.sleep(2)		      			     	
	 print color.BLUE
	 print" ===>THIS TOOL FOR TRACK IP (NOT SPICIFIC)"
	 print color.GREEN
         os.system("cd ..")
         os.system("git clone https://github.com/maldevel/IPGeoLocation")
         os.system("apt-get install python")
	 os.system("pip3 install termcolor colorama")
         print color.RED
	 print" ==>RUN TOOL BY TYPE ./ip2geolocation.py"
	 option()					
      elif y=="3":
          print color.YELLOW
          print"INSTALLING......'\033[0;37;41m'old-yahoo-extracted"
	  print color.END
          time.sleep(2)
	  print color.BLUE
          print" ===>THIS TOOL FOR HACK OLD FACEBOOK ACCOUNT"
          print color.GREEN
	  os.system("cd ..")
	  os.system("git clone https://github.com/mzoir/old-yahoo-account-extracted")
          os.system("apt-get install python2")
	  os.system("pip2 install cookielib mechanize")
	  print color.RED
          print" ==>RUN TOOL BY TYPE python2 newt.py"
	  option()
      elif y=="4":
          print "\033[0:37:44m"
	  print"INSTALLING.........FACEBOOK-HACKING"
	  time.sleep(2)
	  print color.YELLOW
	  print" ===>THIS TOOL FOR HACK TARGET ACCOUNT"
    	  print color.GREEN
          os.system("cd ..")      
	  os.system("git clone https://github.com/V4N654T/fb-hacker")
	  print color.PURPLE
          print" ==<RUN TOOL BY TYPE python2 fb.py"
	  option()
      elif y=="5":
	   print color.BLUE
	   print "INSTALLING.........EMAIL_SPAMMER"
	   time.sleep(2)
	   print "THIS TOOL FOR SPAM ANY ONE EMAIL NOT MY RESPANSABLITY"
	   print color.CYAN
	   time.sleep(2)
	   os.system("cd ..")
	   os.system("git clone https://github.com/Juniorn1003/Email-Spammer")
	   os.system("cd Email-Spammer")
	   os.system("bash install.sh")
	   print color.PURPLE
	   print" ===<RUN TOOL BY TYPE python2 Email-Spam.py"
	   option()
      elif y=="6":
	  print color.BLUE
          print "INSTALLING........{}CrackFlix".format(color.YELLOW)
	  time.sleep(2)
	  print color.BOLD
	  print "==<THIS SCRIPT FOR CRACK NETFLIX ACCOUNT"
	  print color.GREEN
	  os.system("cd ..")
	  os.system("git clone https://github.com/1337r00t/CrackFlix")
	  print" ==>RUN TOOL BY TYPE python2 netflix.py"
	  option()
      else:
	  print"NOTHING TO DO..."
	  time.sleep(2) 
          print"BACK TO MAIN MENU......"
          time.sleep(2)
 	  option()



def WIFI(x):
   if x=="2":
	 print color.BOLD
	 print """LIST TOOL FOR CRACKING WIFI:
		{} [1]: ONESHOT
         	{} [2]: REAVER-WPS
		{} [3]: WIFITE(ROOT)
		{} [4]: WIFI-BRUTE-FORCE
		 [99]:BACK TO MAIN
	 	 [00]:exit
                """.format(color.RED,color.END,color.YELLOW,color.CYAN)
	 print color.END
	 z=raw_input("CHOICE ONE ACTION:")
	 if z=="99":
		option()
	 elif z=="00":
       		  print color.RED
	          print"[>] the program will exit....."
        	  time.sleep(2)
	          exit
         elif z=="1":
		print color.BOLD
		print "INSTALLING ......ONSHOT"
 		time.sleep(2)
		print color.GREEN
		time.sleep(2)	
		os.system("cd ..")			      
		os.system("""pkg install wget build-essential 
pkg-config libnl openssl
wget https://www.w1.fi/releases/wpa_supplicant-2.9.tar.gz && tar xvf wpa_supplicant-2.9.tar.gz
cd wpa_supplicant-2.9/wpa_supplicant/
cp defconfig .config			      			
""")					
		os.system(".config")
	 	os.system("""make
cp wpa_supplicant $PREFIX/bin/
chmod +x $PREFIX/bin/wpa_supplicant
""")
		os.system("""wget https://github.com/wiire-a/pixiewps/archive/master.zip && unzip master.zip
cd pixiewps*/
make && make install""")
		os.system("""pkg install root-repo
pkg install tsu python iw
wget https://raw.githubusercontent.com/drygdryg/OneShot/master/oneshot.py
""")
		os.system("""wget https://raw.githubusercontent.com/drygdryg/OneShot/master/vulnwsc.txt
""")
		time.sleep(2)
		print color.DARKCYAN
		print "YOU NEED ROOT FOR START PROGRAM"
		print "RUN PROGRAM BY TYPE tsudo python oneshot.py -i wlan0 -K"
		os.system("clear")
	        WIFI(x)
		
	 elif z=="2":
	       print color.YELLOW
	       print "INSTALLING.....REAVER-WPS"
	       time.sleep(3)
	       print" ==>THIS TOOL FOR HACKING WIFI-WPS"
	       time.sleep(2)
	       os.system("cd ..")
	       os.system("""apt -y install build-essential libpcap-dev aircrack-ng pixiewps
""")
	       os.system("""git clone https://github.com/t6x/reaver-wps-fork-t6x""")
	       os.system("""cd reaver-wps-fork-t6x*
cd src""")
	       print color.RED
	       os.system("""./configure
make""")
	       os.system("""sudo make install""")
	       print "===>THIS TOOL   NEED ROOT AND SUDO"
	       WIFI(x)

         elif z=="3":	         
		print"INSTALLING '\033[1;33;40m'WIFITE2"
		time.sleep(2)
		print color.BOLD
		print"TOOL FOR HACKING WIFI NEED MONITOR"
		print color.PURPLE
		os.system("cd ..")
		os.system("git clone https://github.com/derv82/wifite2")
		os.system("cd wifite2")
		os.system("python setup.py install")
		print"==>TOOL WAS SUCCEFULLY  INSTALLED"
		WIFI(x)						
	 elif z=="4":
		print "INSTALLING WIFIBRUTEFORE....."
		time.sleep(2)
		os.system("git clone https://github.com/Squuv/WIFI-Brute-Force")
		WIFI(x)

	 else:
          print"NOTHING TO DO..."
          time.sleep(2)
          print"BACK TO MAIN MENU......"
          time.sleep(2)
          option()






option()
