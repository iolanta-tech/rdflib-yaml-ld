import yaml
from pyld import jsonld
from rdflib import Graph
from rdflib.parser import Parser
from rdflib_pyld_compat.convert import (
    rdflib_graph_from_pyld_jsonld,
    _rdflib_graph_from_pyld_dataset, _pyld_term_to_rdflib_term,
)


class YAMLLDParser(Parser):
    def parse(self, source, sink, **kwargs):
        yaml_data = yaml.safe_load(source.file)
        default_graph = jsonld.to_rdf(yaml_data)['@default']

        for triple in default_graph:
            s = _pyld_term_to_rdflib_term(triple['subject'])
            p = _pyld_term_to_rdflib_term(triple['predicate'])
            o = _pyld_term_to_rdflib_term(triple['object'])
            sink.add((s, p, o))
