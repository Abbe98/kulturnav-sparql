# FornPunkt SPARQL

This repository contains various resources for serving Kulturnav datasets over SPARQL. It includes things such as editor configuration, query library, Graph Store HTTP Protocol utilities, and Caddy server configuration.

## Setup your editor

### Prerequisites

 - Fuseki running on `localhost:3030` using the `config.ttl` configuration
 - Caddy installed
 - Python (no third-party packages required)

### Setup

1. Clone this repository
2. Update `Caddyfile` with your domain or IP address
2. Run `caddy` from the root directory
3. Done!

## Getting RDF

The RDF data sources are configured in `scrips/download-export-files.py`.

## Graph Store HTTP Protocol utilities

The `scripts` folder contains several Shell scripts for working with the Graph Store HTTP Protocol and FornPunkt's Export API. The scripts only dependencies are `curl` and Bash 4+.

## Adding queries to the library

Add a new file to the `query-library/src` directory and format your file as shown below. Both a title and tags are mandatory:

```
#title: Count people by gender
#tags: person,gender

PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?gender (COUNT(?person) AS ?person_count) WHERE {
  ?person a <http://schema.org/Person> .
  ?person skos:prefLabel ?name .
  ?person foaf:gender ?gender .
} 

GROUP BY ?gender
```

You can generate a query library JSON file by running the following from the root directory:

```
python query-library/generate_query_lib.py
```
