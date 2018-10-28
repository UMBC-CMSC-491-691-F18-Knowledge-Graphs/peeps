# peeps.own

An simple example ontology for people with some data

Note that peeps.owl ontology

* specifies an ontology URI as http://ebiq.org/ontologies/peeps/
* assigns peeps as a prefix to that URI
* asserts that the peeps:Person concept is equivalent to the Person concepts in both the foaf and schema.org ontologies w/o importing them
* includes several SWRL rules, which you can see and edit by adding the SWRLTab tab

## on importing ontologies

If we want to use any of the vocabulary terms of foaf in this ontology, the 'proper' thing to do is to import the ontology so that reasoners will understand and use information about those terms.

A downside is that Protege will load the entire ontology, most of which may not need needed.  There are techniques and best practices for modularizing ontologies to address this problems.

# mypeeps.owl

The mypeeps.owl file creates four individuals and asserts some facts about them.  It was created in protege by importing the peeps.owl ontology, creating the individuals and then saving it as mypeeps.owl.

* imports peeps.owl (and indirectly foaf.owl and schema.owl, if they are imported)
* creates for individuals (alan, bob, carol and clare) and makes various assertions about them.

If you select the Pellet reasoner (which does support SWRL rules) and start it you can see what additional facts are inferred.


