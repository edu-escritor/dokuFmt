from dokufmt.config.configuration import Configuration
from dokufmt.config.option import Option


def test_configuration_starts_with_default_options() -> None:
    configuration = Configuration()

    assert configuration.has_option(key="DR-001")
    assert configuration.has_option(key="DR-002")
    assert configuration.has_option(key="DR-003")


def test_default_dr003_has_max_blank_lines() -> None:
    configuration = Configuration()

    option = configuration.get_option(key="DR-003")

    assert option.enabled is True
    assert 1 == option.values["max-blank-lines"]


def test_get_unknown_option_returns_default_option() -> None:
    configuration = Configuration()

    option = configuration.get_option(key="UNKNOWN")

    assert option.enabled is True
    assert {} == option.values


def test_options_setter_overrides_existing_default_option() -> None:
    configuration = Configuration()

    configuration.options = {
        "DR-003": Option(
            values={
                "max-blank-lines": 30,
            },
        ),
    }

    option = configuration.get_option(key="DR-003")

    assert option.enabled is True
    assert 30 == option.values["max-blank-lines"]


def test_options_setter_can_disable_existing_default_option() -> None:
    configuration = Configuration()

    configuration.options = {
        "DR-001": Option(enabled=False),
    }

    option = configuration.get_option(key="DR-001")

    assert option.enabled is False


def test_options_setter_preserves_existing_default_values_when_disabling() -> None:
    configuration = Configuration()

    configuration.options = {
        "DR-003": Option(enabled=False),
    }

    option = configuration.get_option(key="DR-003")

    assert option.enabled is False
    assert 1 == option.values["max-blank-lines"]


def test_set_option_adds_unknown_option() -> None:
    configuration = Configuration()

    configuration.set_option(
        key="output",
        option=Option(
            values={
                "replace-file": True,
            },
        ),
    )

    option = configuration.get_option(key="output")

    assert option.enabled is True
    assert option.values["replace-file"] is True


def test_disable_preserves_option_values() -> None:
    configuration = Configuration()

    configuration.options = {
        "DR-003": Option(
            values={
                "max-blank-lines": 30,
            },
        ),
    }

    configuration.disable(key="DR-003")

    option = configuration.get_option(key="DR-003")

    assert option.enabled is False
    assert 30 == option.values["max-blank-lines"]


def test_enable_preserves_option_values() -> None:
    configuration = Configuration()

    configuration.options = {
        "DR-003": Option(
            enabled=False,
            values={
                "max-blank-lines": 30,
            },
        ),
    }

    configuration.enable(key="DR-003")

    option = configuration.get_option(key="DR-003")

    assert option.enabled is True
    assert 30 == option.values["max-blank-lines"]
