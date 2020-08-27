import os
import pyttsx3

pyttsx3.speak("Welcome to my app")

print("\n*****************************************************************************************************")

print("   \t\t\t\tI am ready to help you   ")

print("*****************************************************************************************************")

pyttsx3.speak("what can I do for you ?")
print("")

while True:

	print("Tell me your requirement: ", end=' ')
	p=input()

	if (("run"  in  p) or ("open" in p) or ("execute" in p)) and   (("notepad"   in   p) or ("editor" in p)):
		os.system("notepad")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("chrome"   in   p) or ("browser"  in  p)):
		os.system("chrome")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("internet"   in   p) or ("explorer"  in  p)):
		os.system("iexplore")

	elif  (("run" in p) or ("tell" in p))  and ("date" in p):
		os.system("date")

	elif  (("run" in p) or ("tell" in p))  and ("time" in p):
		os.system("time")

	elif  (("run" in p) or ("open" in p))  and (("cal" in p) or ("calc" in p)  or ("calculator" in p)):
		os.system("calc")

	elif   (("run"  in  p) or ("open" in p) or ("play" in p)) and  (("palyer"   in   p) or ("media"  in p) or ("window media"  in  p)):
		os.system("wmplayer")


	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  ("power point"   in   p):
		os.system("POWERPNT")


	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("word"   in   p) or ("microsoft word"  in  p)):
		os.system("WINWORD")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  ("excel"   in   p):
		os.system("EXCEL")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("putty"   in   p) or ("ssh client"  in  p)):
		os.system("putty")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("virtualbox"   in   p) or ("vm"  in  p)):
		os.system("Virtualbox")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  (("Virtual studio code"   in   p) or ("code"  in  p) or ("vs code" in  p)):
		os.system("Code")

	elif   (("run"  in  p) or ("open" in p) or ("execute" in p)) and  ("paint"   in   p):
		os.system("mspaint")

	elif  ("exit" in p)  or ("quit" in p) or ("close" in p):
		print("Thanks for using my services")
		break

	else:
  		print("don't support  this option. \tPlease fill valid option")

	