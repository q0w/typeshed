from _typeshed import Incomplete, StrOrBytesPath
from configparser import RawConfigParser
from typing import NamedTuple, AnyStr, Any
from typing_extensions import Literal

from ansible.config.data import ConfigData


class Plugin(NamedTuple):
    name: Incomplete
    type: Incomplete

class Setting(NamedTuple):
    name: Incomplete
    value: Incomplete
    origin: Incomplete
    type: Incomplete

INTERNAL_DEFS: dict[str, tuple[str]]

def ensure_type(
    value: object,
    value_type: Literal[
        "boolean",
        "bool",
        "integer",
        "int",
        "float",
        "list",
        "none",
        "path",
        "temppath",
        "tmp",
        "pathlist",
        "pathspec",
        "dict",
        "dictionary",
        "str",
        "string",
    ],
    origin: StrOrBytesPath | None = ...,
) -> str: ...
def resolve_path(path: str, basedir: AnyStr | None = ...) -> str: ...
def get_config_type(cfile: StrOrBytesPath | None) -> Literal["ini", "yaml"] | None: ...
def get_ini_config_value(p: RawConfigParser, entry: Incomplete) -> str | None : ...
def find_ini_config_file(warnings: set[str] | None = ...) -> str | None: ...

class ConfigManager:
    DEPRECATED: list[tuple[str, dict[str, str]]]
    WARNINGS: set[str]
    data: ConfigData
    def __init__(self, conf_file: StrOrBytesPath | None = ..., defs_file: AnyStr | None = ...) -> None: ...
    def get_plugin_options(
        self,
        plugin_type: str,
        name,
        keys: Incomplete | None = ...,
        variables: Incomplete | None = ...,
        direct: Incomplete | None = ...,
    ): ...
    def get_plugin_vars(self, plugin_type: str, name): ...
    def get_plugin_options_from_var(self, plugin_type: str, name, variable): ...
    def get_configuration_definition(self, name: str, plugin_type: str | None = ..., plugin_name: str | None = ...): ...
    def get_configuration_definitions(
        self, plugin_type: str | None = ..., name: str | None = ..., ignore_private: bool = ...
    ) -> dict[str, Any]: ...
    def get_config_value(
        self,
        config: str,
        cfile: StrOrBytesPath | None = ...,
        plugin_type: str | None = ...,
        plugin_name: str | None = ...,
        keys: Incomplete | None = ...,
        variables: Incomplete | None = ...,
        direct: Incomplete | None = ...,
    ): ...
    def get_config_value_and_origin(
        self,
        config: str,
        cfile: StrOrBytesPath | None = ...,
        plugin_type: str | None = ...,
        plugin_name: Incomplete | None = ...,
        keys: Incomplete | None = ...,
        variables: Incomplete | None = ...,
        direct: Incomplete | None = ...,
    ): ...
    def initialize_plugin_configuration_definitions(self, plugin_type: str, name: str, defs: Any) -> None: ...
    def update_config_data(self, defs: Incomplete | None = ..., configfile: Incomplete | None = ...) -> None: ...
