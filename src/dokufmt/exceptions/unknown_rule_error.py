class UnknownRuleError(Exception):
    def __init__(self, key: str) -> None:
        self.key = key

        super().__init__(f"Rule does not exist: {key}")
