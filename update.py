import os
os.system ("clear")
def update (up) :
	mik = """"\033[1;32m
			 _       _         _____           _
 	\033[1;31m _   _ _ __   __| | __ _| |_ ___  |_   _|__   ___ | |
	\033[1;32m| | | | '_ \ / _` |/ _` | __/ _ \   | |/ _ \ / _ \| |
	\033[1;33m| |_| | |_) | (_| | (_| | ||  __/   | | (_) | (_) | |
 	\033[1;34m\_____| .__/ \__,_|\__,_|\__\___|   |_|\___/ \___/|_|
	      \033[1;35m|_|
	\033[1;32m
	"""
	print ("\033[1;35mplesse wite updateing Tool Tool-M")
	print (mik)
	os.system ("rm -rif Tool-M.py")
	os.system ("git clone https://github.com/michael-6086/Tool-M/Tool-M.py")
	print ("\033[1;33mend update")
	os.system ("python3 Tool-M.py")
update ("6999")
