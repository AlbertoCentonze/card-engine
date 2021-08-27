from observers import BooleanExpression


class Turn:
    def __init__(self, phases: tuple):
        self.__phases = phases


class Phase:
    def __init__(self, bool_expr: BooleanExpression):
        self.can_enter = bool_expr

    def can_enter(self) -> bool:
        return bool(self.can_enter)


class GlobalPhase:
    pass
