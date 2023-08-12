import rdflib
import yaml
from pyld import jsonld
from rdflib.serializer import Serializer


class YAMLLDSerializer(Serializer):
    def serialize(self, stream, base=None, encoding=None, **kwargs):
        # Convert rdflib Graph to JSON-LD
        jsonld_data = jsonld.to_rdf(self.store)
        # Convert JSON-LD to YAML if needed
        yaml_data = yaml.safe_dump(jsonld_data)
        stream.write(yaml_data)
