import subprocess
cmdCommand = "shutdown -s"
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)//it is for shutdown
