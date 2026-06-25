from dokufmt.config.configuration_loader import ConfigurationLoader


def test_load_applies_file_overrides_to_default_configuration(tmp_path) -> None:
    path = tmp_path / ".dokufmtrc"
    path.write_text(
        """
[DR-001]
enabled = false

[DR-003]
max-blank-lines = 999
""",
        encoding="utf-8",
    )

    configuration = ConfigurationLoader(path=path).load()

    dr001 = configuration.get_option(key="DR-001")
    dr002 = configuration.get_option(key="DR-002")
    dr003 = configuration.get_option(key="DR-003")

    assert dr001.enabled is False

    assert dr002.enabled is True

    assert dr003.enabled is True
    assert 999 == dr003.values["max-blank-lines"]
