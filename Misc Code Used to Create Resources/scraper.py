file = open('notes.txt')

lines = file.readlines()
for line in lines:
    if line == '\n':
        lines.remove('\n')
    if line.startswith("%"):
        lines.remove(line)

def envfinder(envname):
    env_beg = []
    env_end = []
    for i in range(len(lines)):
        if '\\begin{' + envname + '}' in lines[i]:
            env_beg.append(i)
        if '\end{' + envname + '}' in lines[i]:
            env_end.append(i)
    return(env_beg,env_end)

envs = ['proof','thm','defn','prop','lemma','corollary','remark','notation','remarks']
s_e = []
for i in envs:
   s_e.append(envfinder(i))

def readBetween(l1,l2):
    out = ''
    for line in range(l1,l2+1):
        out += lines[line]
    return out
out = [[] for i in range(len(envs))]
for e in s_e:
    for l in range(len(e[0])):
        out[s_e.index(e)].append(readBetween(e[0][l],e[1][l]))
for i in envs:       
        outfile = open(i+'.txt','w')
        j = out[envs.index(i)]     
        for l in j:
            outfile.write(l)
            outfile.write('\n')

        
#def LenOrder(inList):
#    ordList = inList.copy()
#    ordList.sort()
#    outList = []
#    for i in ordList:
#        outList.append(inList.index(i))
#    return outList
