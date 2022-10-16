import os



class Syscall():
    def calcCpuUsage(self):
        while True:    
            CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
            print("\r CPU Usage = " +"{}%".format(CPU_Pct),end=" ") 

    