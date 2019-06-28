from functools import reduce


class NFA:

    def __init__(self, initialState):
        self.initialState = initialState
        self.states = {}
        self.powerSet = []

    def addState(self, input, state, pointingState):
        if state not in self.states:
            x = {0: [], 1: []}
            if len(pointingState) == 0:
                x[input] = []
                self.states[state] = x
            else:
                x[input].append(pointingState)
                self.states[state] = x

        else:
            if len(pointingState) == 0:
                self.states[state][input] = []
            else:
                self.states[state][input].append(pointingState)

    def getDFA(self):
        self.powerSet = self.getPowerSet()
        dfa = {}
        for set in self.powerSet:
            dfa[str(set)] = {0: self.getPointer(set, 0), 1: self.getPointer(set, 1)}
        return dfa

    def getPointer(self, set, input):
        pointer = []
        for s in set:
            x = self.states[s]
            y = x[input]
            for yy in y:
                if yy not in pointer:
                    pointer.append(yy)
        return pointer

    def getPowerSet(self):
        return reduce(lambda result, x: result + [subset + [x] for subset in result], self.states, [[]])


def main():
    file = input("Escribe el nombre del archivo a leer: ")
    archivo=open(file, 'r')
    arhivoN=archivo.readlines()
    archivo.close()
    lineaSinLlave=arhivoN[0].replace("{","")
    lineaSinLlave2=lineaSinLlave.replace("}","")
    lineaSinLlave3=lineaSinLlave2.replace("(","|")
    lineaSinLlave4=lineaSinLlave3.replace(")","|")
    arhivoN2=lineaSinLlave4.split("|")


    for i in range(1, len(arhivoN2),2):

        lineaSinTab=arhivoN2[i]
        lineaSeparada=lineaSinTab.split(",")

        if(i==1):
            nfa=NFA(str(lineaSeparada[0]))
        else:
            nfa.addState(int(lineaSeparada[0]),str(lineaSeparada[1]),str(lineaSeparada[2]))

    # EJEMPLO
    #nfa = NFA("q0")
    #nfa.addState(1, "q0", "q0")
    #nfa.addState(0, "q0", "q0")
    #nfa.addState(0, "q0", "q1")
    #nfa.addState(1, "q1", "q2")
    #nfa.addState(0, "q2", "")
    #nfa.addState(1, "q2", "")

    x = nfa.getDFA()

    #Escribir
    archivoNuevo=open("DFA",'w')
    archivoNuevo.write("Resultant NFA\n")
    archivoNuevo.write("Q ")
    archivoNuevo.write(str(x)+"\n")
    archivoNuevo.write("∑: {0,1}\n")
    archivoNuevo.write("q: "+nfa.initialState)
    archivoNuevo.write("∂: \n")

    archivoNuevo.write(
        '{3}{0:<20}{3} {3}{1:<15}{3} {3}{2:<15}{3}'.format("Estado", str(1), 0, '|') + "\n")

    for i in x:
        archivoNuevo.write('{3}{0:<20}{3} {3}{1:<15}{3} {3}{2:<15}{3}'.format(str(i), str(x[i][0]), str(x[i][1]), '|')+"\n")


        archivoNuevo.write("")



main()
