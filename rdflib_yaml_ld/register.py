import rdflib
from rdflib.parser import Parser
from rdflib.serializer import Serializer


rdflib.plugin.register(
    name='yaml-ld',
    kind=Serializer,
    module_path='rdflib_yaml_ld',
    class_name='YAMLLDSerializer',
)


rdflib.plugin.register(
    name='yaml-ld',
    kind=Parser,
    module_path='rdflib_yaml_ld',
    class_name='YAMLLDParser',
)
