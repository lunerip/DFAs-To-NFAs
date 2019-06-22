from functools import reduce


class NFA:

    def __init__(self, initialState):
        self.initialState = initialState
        self.states = {initialState: {0: [], 1: []}}
        self.powerSet = []


    def addState(self, input, state, pointingState):
        self.states[state][input].append(pointingState)


    def getDFA(self):
        self.powerSet = self.getPowerSet()
        dfa = {}
        for set in self.powerSet:
            dfa[set]={0:self.getPointer(set, 0), 1:self.getPointer(set, 1)}
        return dfa


    def getPointer(self, set, input):
        pointer = []



    def getPowerSet(self):
        return reduce(lambda result, x: result + [subset + [x] for subset in result], self.states,[[]])

