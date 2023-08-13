from pathlib import Path

from rdflib import Graph, URIRef, BNode, Literal


def test_parse():
    from rdflib_yaml_ld import register
    # https://github.com/zimeon/rdflib-pyld-compat
    g = Graph()
    triples = list(g.parse(
        Path(__file__).parent / 'data/simple.yaml',
        format='yaml-ld',
        base=URIRef('https://example.org'),
    ))

    assert triples == [(
        BNode('_:b0'),
        URIRef('https://example.org/foo'),
        Literal('bar'),
    )]
