""" An example of calling a sparql endpoint from Python """

from SPARQLWrapper import SPARQLWrapper, JSON

# sparql endpoint URL
peeps = "http://localhost:5820/mypeeps/query/"
default_endpoint = peeps

person_query = """
# find persons and their givenNames 
PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
PREFIX peeps: <https://raw.githubusercontent.com/UMBC-CMSC-491-691-F18-Knowledge-Graphs/peeps/master/peeps.ttl#> 
SELECT * WHERE {?p a peeps:Person; foaf:givenName ?n .} """

class_query = """
# find classes and their number of instances
SELECT ?class (count(?instance) as ?instances) WHERE {?instance a ?class}
GROUP BY ?class 
ORDER BY desc(?instances)"""

def ask(query, endpoint=default_endpoint):
    """ returns a list of tuples with the query results """
    tuples = []
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat('json')
    sparql.addParameter('reasoning', 'true')  # special for Stardog
    sparql.setQuery(query)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        tuples.append(tuple([str(v['value']) for v in result.values()]))
    return tuples

def main():
    print('Query to find people and the classes to which they belong')
    for obj,name in ask(person_query):
        print(obj, name)
    print('\n\nQuery to find classes and the number of their instances')
    for n, cls in ask(class_query):
        print(n, cls)

if __name__ == "__main__":
    # if called from command-line, call main() as an example
    main()
    
