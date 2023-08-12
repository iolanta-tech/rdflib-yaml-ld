from pathlib import Path

from rdflib import Graph


def test_parse():
    from rdflib_yaml_ld import register
    g = Graph()
    g.parse(Path(__file__).parent / 'data/simple.yaml', format='yaml-ld')
