import sys

def searchfrequencies(filename,whattosearch,id):
    global x
    y=[]
    searchfile = open(filename, "r")
    for line in searchfile:
       if whattosearch in line:
           x = line.split()
           for i in range(id,len(x)):
              y.append(float(x[i]))
    x=y
def displacement(filename):
    global totalx
    global totaly
    global totalz
    global Frozen
    global Numberofatoms


    numlines=0
    for num in open(filename):
        numlines = numlines+1

    searchfile = open(filename, "r")
    for j in range(0,int(numlines)):
      temp=""
      temp=searchfile.readline()
      if "IR Inten    --" in temp:
       temp = searchfile.readline()
       disx1 = []
       disy1 = []
       disz1 = []
       disx2 = []
       disy2 = []
       disz2 = []
       disx3 = []
       disy3 = []
       disz3 = []
       if Frozen == 0:
          for i in range(0, int(Numberofatoms)):
            temp = searchfile.readline()
            temp = temp.split()
            disx1.append(temp[2])
            disy1.append(temp[3])
            disz1.append(temp[4])
            disx2.append(temp[5])
            disy2.append(temp[6])
            disz2.append(temp[7])
            disx3.append(temp[8])
            disy3.append(temp[9])
            disz3.append(temp[10])
       if Frozen != 0:
           count=1
           for i in range(0, int(Numberofatoms-Frozen)):
             temp = searchfile.readline()
             temp = temp.split()
             while count != int(temp[0]):
                disx1.append(float("0.0"))
                disy1.append(float("0.0"))
                disz1.append(float("0.0"))
                disx2.append(float("0.0"))
                disy2.append(float("0.0"))
                disz2.append(float("0.0"))
                disx3.append(float("0.0"))
                disy3.append(float("0.0"))
                disz3.append(float("0.0"))
                count=count+1
             disx1.append(temp[2])
             disy1.append(temp[3])
             disz1.append(temp[4])
             disx2.append(temp[5])
             disy2.append(temp[6])
             disz2.append(temp[7])
             disx3.append(temp[8])
             disy3.append(temp[9])
             disz3.append(temp[10])
             count = count + 1
       totalx.append(disx1)
       totalx.append(disx2)
       totalx.append(disx3)
       totaly.append(disy1)
       totaly.append(disy2)
       totaly.append(disy3)
       totalz.append(disz1)
       totalz.append(disz2)
       totalz.append(disz3)
def search(filename,whattosearch):
    global x
    x = []
    searchfile = open(filename, "r")
    for line in searchfile:
       if whattosearch in line:
           x=line
           x = x.split()
    searchfile.close()
def geometry(filename):
    global Numberofatoms
    global atomsnames
    global cartesianx
    global cartesiany
    global cartesianz

    numlines = 0
    for num in open(filename):
        numlines = numlines + 1

    text="Proceeding to internal job step number"
    searchfile = open(filename, "r")
    for j in range(0, int(numlines)):
        temp = ""
        temp = searchfile.readline()
        if "NAtoms=" in temp:
            x= temp.split()
            Numberofatoms=int(x[1])
        if text in temp:
            count=j
            break
        if j == int(numlines-1):
            searchfile.close()
            count=0
            searchfile = open(filename, "r")
            break

    text = "Number     Number       Type             X           Y           Z"
    for j in range(count, int(numlines)):
        temp = ""
        temp = searchfile.readline()
        if text in temp:
            temp = searchfile.readline()
            for i in range(0, Numberofatoms):
                temp = searchfile.readline()
                x = temp.split()
                atomsnames.append(x[1])
                cartesianx.append(x[3])
                cartesiany.append(x[4])
                cartesianz.append(x[5])
            break

    symbol={"1":"H","2":"He","3":"Li","4":"Be","5":"B","6":"C","7":"N","8":"O","9":"F","10":"Ne","11":"Na","12":"Mg","13":"Al","14":"Si","15":"P","16":"S","17":"Cl","18":"Ar","19":"K","20":"Ca","21":"Sc","22":"Ti","23":"V","24":"Cr","25":"Mn","26":"Fe","27":"Co","28":"Ni","29":"Cu","30":"Zn","31":"Ga","32":"Ge","33":"As","34":"Se","35":"Br","36":"Kr","37":"Rb","38":"Sr","39":"Y","40":"Zr","41":"Nb","42":"Mo","43":"Tc","44":"Ru","45":"Rh","46":"Pd","47":"Ag","48":"Cd","49":"In","50":"Sn","51":"Sb","52":"Te","53":"I","54":"Xe","55":"Cs","56":"Ba","57":"La","58":"Ce","59":"Pr","60":"Nd","61":"Pm","62":"Sm","63":"Eu","64":"Gd","65":"Tb","66":"Dy","67":"Ho","68":"Er","69":"Tm","70":"Yb","71":"Lu","72":"Hf","73":"Ta","74":"W","75":"Re","76":"Os","77":"Ir","78":"Pt","79":"Au","80":"Hg","81":"Tl","82":"Pb","83":"Bi","84":"Po","85":"At","86":"Rn","87":"Fr","88":"Ra","89":"Ac","90":"Th","91":"Pa","92":"U","93":"Np","94":"Pu","95":"Am","96":"Cm","97":"Bk","98":"Cf","99":"Es","100":"Fm","101":"Md","102":"No","103":"Lr","104":"Rf","105":"Db","106":"Sg","107":"Bh","108":"Hs","109":"Mt","110":"Ds","111":"Rg","112":"Cn","113":"Uut","114":"Fl","115":"Uup","116":"Lv","117":"Uus","118":"Uuo"}
    for i in range(0,len(atomsnames)):
        atomsnames[i]=str(symbol[atomsnames[i]])

x=[]
atomsnames=[]
cartesianx=[]
cartesiany=[]
cartesianz=[]

geometry(sys.argv[1])

Frozen=0
search(str(sys.argv[1]),"atoms frozen in the vibrational analysis.")
if len(x) != 0:
    Frozen=int(x[0])

# Search Frequencies (cm-1)
searchfrequencies(str(sys.argv[1]),"Frequencies",2)
Frequencies=x

# Search Infrared Intensity
searchfrequencies(str(sys.argv[1]),"IR Inten ",3)
irintensity=x

totalx=[]
totaly=[]
totalz=[]

# Search Displacements
displacement(str(sys.argv[1]))

# Print all vibrations in molden format
bohr=1.8897161646320724
f = open(("vibration.molden"), "w+")
f.write('[MOLDEN FORMAT] \n')
f.write('[FREQ] \n')
for i in range(len(Frequencies)):
   f.write(str(round(Frequencies[i],2))+'\n')
f.write('[FR-COORD] \n')
for i in range(Numberofatoms):
   f.write(str(atomsnames[i])+' '+str(float(cartesianx[i])*bohr)+' '+str(float(cartesiany[i])*bohr)+' '+str(float(cartesianz[i])*bohr)+'\n')
f.write('[FR-NORM-COORD] \n')
for i in range(len(Frequencies)):
   f.write("vibration "+str(i+1)+'\n')
   for j in range(Numberofatoms):
     f.write(str(float(totalx[i][j])*bohr) + ' ' + str(float(totaly[i][j])*bohr) + ' ' + str(float(totalz[i][j])*bohr) + '\n')
f.write('[INT] \n')
for i in range(len(Frequencies)):
   f.write(str(round(irintensity[i], 2)) + '\n')
f.close()

