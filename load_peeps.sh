#!/bin/bash

# loads peeps.ttl, mypeeps.ttl and associated namespaces into a
# Stardog database.  Assumes that Stardog is installed and set up
# properly

PORT="5820"
SERVER="http://localhost:$PORT"
DBNAME="mypeeps"
DBURL="$SERVER/$DBNAME"

# stop server in case one is already running
stardog-admin --server $SERVER server stop

# start server
stardog-admin server start --port $PORT --disable-security 

# drop database named $DBNAME in case it exists already
stardog-admin --server $SERVER db drop -n $DBNAME

# create database named $DBNAME with reasoning and search enabled
stardog-admin --server $SERVER db create -o reasoning.sameas=FULL -o search.enabled=true -n $DBNAME

# load ontology and data
stardog data add $DBURL peeps.ttl mypeeps.ttl 

# add namespace prefixes for the query system to use
stardog namespace import --verbose $DBURL prefixes.ttl

