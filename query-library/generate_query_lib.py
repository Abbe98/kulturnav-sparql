import os
import json

"""
#defaultView:PieChart
#title: Könsfördelning som cirkeldiagram


PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?label (COUNT(?person) AS ?count) WHERE {
  ?person a <http://schema.org/Person> .
  ?person skos:prefLabel ?name .
  ?person foaf:gender ?label .
}
GROUP BY ?label
"""


queries = list()
for filename in os.listdir('query-library/src'):
    with open('query-library/src/' + filename, 'r') as f:
        content = f.read()
        title = ''
        for line in content.split('\n'):
            if line.startswith('#title'):
                title = line
                title = title.split(':')[1].strip()
                break

        query = {}
        query['title'] = title
        query['body'] = content
        queries.append(query)

with open('thor-configuration/queries.json', 'w') as outfile:
    json.dump(queries, outfile)

print('Done generating JSON')
