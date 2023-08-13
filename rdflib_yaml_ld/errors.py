from dataclasses import dataclass
from typing import Any

from documented import DocumentedError


@dataclass
class MappingKeyError(DocumentedError):
    """
    Mapping key is not a `string`.

    Relevant fragment:

    ```yaml
    {self.key}: {self.value}
    ```

    The key must be a `string` as required by YAML-LD specification but is
    in fact `{self.key_type}`.
    """

    key: Any
    value: Any

    @property
    def key_type(self):
        return type(self.key).__name__
