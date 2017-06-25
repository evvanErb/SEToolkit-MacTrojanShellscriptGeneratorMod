# SEToolkit-MacTrojanShellscirptGeneratorMod
This SET module creates a python/meterpreter/reverse_tcp payload with msfvenom and integrates it with curl-ing of a trojan file to create shell script that will curl the trojan file and open it, while executing the python payload in the background. NOTE: This will only generate the script ... you must turn it into an applet and change the icon your self.

Dependecies: SET, metasploit (msfvenom)

Once downloaded please move Mac_shell_script_payload_generator.py and Mac_shell_script_payload_generator.pyc to your SET modules directory (Example: /usr/share/setoolkit/modules)
