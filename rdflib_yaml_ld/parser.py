import yaml
from boltons.iterutils import remap
from pyld import jsonld
from rdflib.parser import Parser
from rdflib_pyld_compat.convert import (
    _pyld_term_to_rdflib_term,
)

from rdflib_yaml_ld.errors import MappingKeyError


class YAMLLDParser(Parser):
    def parse(self, source, sink, **kwargs):
        yaml_data = self.validate(yaml.safe_load(source.file))
        default_graph = jsonld.to_rdf(yaml_data)['@default']

        for triple in default_graph:
            s = _pyld_term_to_rdflib_term(triple['subject'])
            p = _pyld_term_to_rdflib_term(triple['predicate'])
            o = _pyld_term_to_rdflib_term(triple['object'])
            sink.add((s, p, o))

    def _validator(self, path, key, value):
        if not isinstance(key, str):
            raise MappingKeyError(key=key, value=value)

        return key, value

    def validate(self, yaml_data):
        remap(yaml_data, self._validator)
        return yaml_data
