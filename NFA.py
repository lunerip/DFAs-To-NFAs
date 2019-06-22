class NFA:

    def __init__(self, initialState):
        self.initialState = initialState
        self.states = {initialState: {0: [], 1: []}}

    def addState(self, input, state, pointingState):
        self.states[state][input].append(pointingState)

    def getDFA(self):
        self.completeDFAsStates()




    def completeDFAsStates(self):
        for s in self.states:
            for i in s:
                if len(i) == 0:
                    i.append("ø")

