import click
from SPARQLWrapper import SPARQLWrapper, JSON
import json


def get_json(endpoint, query):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return json.dumps(
        results['results']['bindings'],
        ensure_ascii=False, indent=2, sort_keys=True)


@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('query_file', type=click.Path(file_okay=True, dir_okay=False))
@click.option('--dist', default='dist.json', type=click.STRING)
def ja(query_file, dist):
    json_string = get_json('http://ja.dbpedia.org/sparql', open(query_file).read())
    with open(dist, 'w') as fp:
        fp.write(json_string)


@cmd.command()
@click.argument('query_file', type=click.Path(file_okay=True, dir_okay=False))
@click.option('--dist', default='dist.json', type=click.STRING)
def en(query_file, dist):
    json_string = get_json('http://dbpedia.org/sparql/', open(query_file).read())
    with open(dist, 'w') as fp:
        fp.write(json_string)


@cmd.command()
@click.argument('result_file', type=click.Path(file_okay=True, dir_okay=False))
def num(result_file):
    data = json.load(open(result_file))
    click.echo(len(data))


if __name__ == '__main__':
    cmd()
