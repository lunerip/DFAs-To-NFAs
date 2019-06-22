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

    # EJEMPLO
    nfa = NFA("q0")
    nfa.addState(1, "q0", "q0")
    nfa.addState(0, "q0", "q0")
    nfa.addState(0, "q0", "q1")
    nfa.addState(1, "q1", "q2")
    nfa.addState(0, "q2", "")
    nfa.addState(1, "q2", "")

    x = nfa.getDFA()

    print("Resultant NFA")
    print("Q: ",x)
    print("∑: {0,1}")
    print("q: "+nfa.initialState)
    print("∂: ")
    for i in x:
        print(" Estado " + i)
        print("  0: ", x[i][0])
        print("  1: ", x[i][1])
        print("")


main()
