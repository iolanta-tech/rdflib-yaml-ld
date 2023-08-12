import yaml
from pyld import jsonld
from rdflib import Graph
from rdflib.parser import Parser


class YAMLLDParser(Parser):
    def parse(self, source, sink, **kwargs):
        yaml_data = yaml.safe_load(source.file)
        # Convert YAML to JSON-LD if needed
        triples = jsonld.to_rdf(yaml_data)
        raise ValueError(triples)
        # Add triples to the sink (rdflib Graph)
        for triple in jsonld_data['@graph']:
            sink.add(triple)
