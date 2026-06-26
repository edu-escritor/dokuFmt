from dokufmt.config.configuration import Configuration
from dokufmt.rules.rule import Rule


class RuleMetadataTests:
    rule_class: type[Rule]
    expected_code: str
    expected_name: str
    expected_description: str

    def create_rule(self) -> Rule:
        config = Configuration()
        option = config.get_option(self.expected_code)
        rule = self.rule_class(option=option)

        return rule

    def test_rule_has_code(self) -> None:
        rule = self.create_rule()

        assert isinstance(rule.code, str)
        assert "" != rule.code.strip()
        assert self.expected_code == rule.code

    def test_rule_has_name(self) -> None:
        rule = self.create_rule()

        assert isinstance(rule.name, str)
        assert "" != rule.name.strip()
        assert self.expected_name == rule.name

    def test_rule_has_description(self) -> None:
        rule = self.create_rule()

        assert isinstance(rule.description, str)
        assert "" != rule.description.strip()
        assert self.expected_description == rule.description

    def test_rule_has_example(self) -> None:
        rule = self.create_rule()

        assert isinstance(rule.example, str)
        assert "" != rule.example.strip()
