import numpy as np
import matplotlib.pyplot as plt
import os
from numpy import trapz 

#blank=[]
filename=[]
filename_n=[]
folder=[]
folder = os.listdir("./")

for i in range(len(folder)):
    if folder[i].endswith(".dat"):
        filename.append(folder[i])
for i in range(len(folder)):
    if folder[i].endswith(".txt") and "blank" not in folder[i] :
        filename_n.append(folder[i])
    elif "blank" in folder[i]:
        blank.append(folder[i])
#f_blank=open(blank[0],'r')   
#data_blank=f_blank.readlines()[16:]   
#photodiode_blank=[] 
#print blank,filename_n,filename
#for line in data_blank:
#    line=line.strip()
#    columns=line.split()
#    photodiode_blank.append(float(columns[8]))
   

#print filename_n
#print folder
#print blank
#print energy_blank
#Takes igor .dat files and extracts q and I, plots them, need to switch to log scale
print filename
def igor():
    
    for i in range(len(filename)):
        name=filename[i]
        
        f=open(filename[i],'r')
        data=f.readlines()[128:]
        #print data
        q=[]
        intensity=[]
        col=[]
        for line in data:
                line=line.strip()
                columns=line.split()
                col.append(columns)
        
        for i in range (1,499):
            #print col[i][0]
            q.append(float(col[i][0]))
            intensity.append(float(col[i][1]))
            
            
        sum=np.sum(intensity)
        area=.0002*sum
        print area
        #plot_all_q(q,intensity,name)
        #q_array=np.array(q) 
        #in_array=np.array(intensity)
        #wr_dat=np.array([q_array,in_array])
        #wr_dat=wr_dat.T
        #print wr_dat
        #datafile_id = open(name, 'w+')
        #np.savetxt(datafile_id, wr_dat, fmt=['%f','%f'])
        #datafile_id.close()
         
        ##Save for each file 
        #plot_q(q,intensity,name)
#Calculate and extract NEXAFS        
def nexafs(thickness,density):
    for i in range(len(filename_n)):
        f=open(filename_n[i],'r')
        f2=open(filename_n[i],'r')
        header=f.readlines()[:16]
        data=f2.readlines()[16:]
        time=[]
        seconds=[]
        energy=[]
        EPU_pol=[]
        CCD_temp=[]
        current=[]
        TEY_signal=[]
        I0=[]
        photodiode=[]
        for line in data:
                line=line.strip()
                columns=line.split()
                time.append((columns[0])) 
                seconds.append(float(columns[1]))
                energy.append(float(columns[2]))
                EPU_pol.append(float(columns[3]))
                CCD_temp.append(float(columns[4]))
                current.append(float(columns[5]))
                TEY_signal.append(float(columns[6]))
                I0.append(float(columns[7]))
                photodiode.append(float(columns[8]))
        #plots(q,intensity,filename[i])
        absorption=[]
        for i in range(len(energy)):
            absorption_item=float(np.log(photodiode_blank[i]/photodiode[i])/(density*thickness))
            absorption.append(absorption_item)
         
        stop_val=search(absorption,density)
        absorption_norm=absorption[0:stop_val]
        norm_value=sum(absorption_norm)/len(absorption_norm)
        e_array=np.array(energy)
        a_array=np.array(absorption)-float(norm_value)
        print norm_value
        
        plot_nexafs(e_array,a_array,"test")
        wr_dat=np.array([e_array,a_array])
        wr_dat=wr_dat.T
        print wr_dat
        datafile_id = open("test2.txt", 'w+')
        np.savetxt(datafile_id, wr_dat, fmt=['%f','%f'])
        datafile_id.close()
        
def plot_all_q(x,y,name):
    plt.loglog(x,y)
    plt.xlabel("q",fontsize=20)
    plt.ylabel("intensity",fontsize=20)
    plt.xlim([.0005,.01])
    plt.ylim([100,5000])
    plt.title("q v intensity",fontsize=22)
    plt.grid(True)
    
    plt.show()
    #plt.savefig(name[:-4]+".png")
    #plt.close()

def plot_q(x,y,name):
    plt.plot(x,y)
    plt.xlabel("q",fontsize=20)
    plt.ylabel("intensity",fontsize=20)
    plt.title("q v intensity",fontsize=22)
    plt.grid(True)
    
    plt.show()
    plt.savefig(name[:-4]+".png")
    plt.close()
    
def plot_nexafs(x,y,name):
    plt.plot(x,y)
    plt.xlabel("Energy",fontsize=20)
    plt.ylabel("absorption",fontsize=20)
    plt.title("NEXAFS",fontsize=22)
    plt.grid(True)
    plt.show()
    plt.savefig(name[:-4]+".png")
    plt.close()
def search(ar,density):
    for i in range(len(ar)):
        if ar[i+1]-ar[i]>(20/density) or ar[i+1]-ar[i]<(-20/density) :
            stop_num=i
            return stop_num

    
        