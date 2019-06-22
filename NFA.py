class NFA:

    def __init__(self, initialState):
        self.initialState = initialState
        self.states = {initialState: {0: [], 1: []}}

    def addState(self, input, state, pointingState):
        self.states[state][input].append(pointingState)
