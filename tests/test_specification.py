import operator
from pathlib import Path
from typing import Iterable

import funcy
import pytest
from iolanta.iolanta import Iolanta
from iolanta.namespaces import LOCAL
from rdflib import Graph, ConjunctiveGraph, Namespace

from json_ld_tests.models import TestCase

tests = Namespace('https://w3c.github.io/json-ld-api/tests/vocab#')


def load_tests() -> Iterable[TestCase]:
    # Load the JSON-LD tests from the test suite
    # Return a list of test cases
    manifest_path = Path(__file__).parent.parent / 'yaml-ld-spec/tests/basic-manifest.jsonld'

    # FIXME: Use `iolanta.add()`.
    #   At this point, we can't do that: `iolanta` does not resolve the
    #   `context.jsonld` file.
    graph = ConjunctiveGraph()
    graph.parse(manifest_path)
    iolanta = Iolanta(graph=graph)

    iolanta.add({
        '$id': tests.ExpandTest,
        'iolanta:facet': {
            '$id': 'python://json_ld_tests.JSONLDTests',
            'iolanta:supports': LOCAL.test,
        },
        'iolanta:hasInstanceFacet': {
            '$id': 'python://json_ld_tests.JSONLDTest',
            'iolanta:supports': LOCAL.test,
        },
    })

    return funcy.first(
        iolanta.render(
            node=tests.ExpandTest,
            environments=[LOCAL.test],
        ),
    )


@pytest.mark.parametrize(
    "test_case",
    load_tests(),
    ids=operator.attrgetter('test'),
)
def test_jsonld_spec(test_case: TestCase):
    if isinstance(test_case.result, Path) and test_case.result.suffix == '.yamlld':
        raise ValueError('Expansion test is not applicable.')

    Graph().parse(
        test_case.input,
        format='yaml-ld',
    )
