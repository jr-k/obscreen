import json
import time

from typing import Optional, Union
from src.model.enum.VariableType import VariableType
from src.utils import str_to_enum


class Variable:

    def __init__(self, name: str = '', description: str = '', type: Union[VariableType, str] = VariableType.STRING,
                 value: Union[int, bool, str] = '', editable: bool = True, id: Optional[str] = None,
                 plugin: Optional[str] = None):
        self._id = id if id else None
        self._name = name
        self._type = str_to_enum(type, VariableType) if isinstance(type, str) else type
        self._description = description
        self._value = value
        self._editable = editable
        self._plugin = plugin

    @property
    def id(self) -> Union[int, str]:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def type(self) -> VariableType:
        return self._type

    @type.setter
    def type(self, value: VariableType):
        self._type = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def editable(self) -> bool:
        return self._editable

    @editable.setter
    def editable(self, value: bool):
        self._editable = value

    @property
    def value(self) -> Union[int, bool, str]:
        return self._value

    @value.setter
    def value(self, value: Union[int, bool, str]):
        self._value = value

    @property
    def plugin(self) -> Optional[str]:
        return self._plugin

    @plugin.setter
    def plugin(self, value: Optional[str]):
        self._plugin = value

    def __str__(self) -> str:
        return f"Variable(" \
               f"id='{self.id}',\n" \
               f"name='{self.name}',\n" \
               f"value='{self.value}',\n" \
               f"type='{self.type}',\n" \
               f"description='{self.description}',\n" \
               f"editable='{self.editable}',\n" \
               f"plugin='{self.plugin}',\n" \
               f")"

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "type": self.type.value,
            "description": self.description,
            "editable": self.editable,
            "plugin": self.plugin,
        }

    def as_bool(self) -> bool:
        return bool(int(self._value))

    def as_string(self) -> str:
        return str(self._value)

    def as_int(self) -> int:
        return int(self._value)

    def as_ctime(self):
        return time.ctime(self._value)

    def display(self):
        if self.type == VariableType.INT:
            return self.as_int()
        elif self.type == VariableType.BOOL:
            return self.as_bool()
        elif self.type == VariableType.TIMESTAMP:
            return self.as_ctime()

        return self.as_string()

    def is_from_plugin(self):
        return self.plugin