# NOTE

## **Windows setups** (run in Git CMD)

https://github.com/microsoftarchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.msi

- redis-stacks and rediSearch to search in redis:

        docker run -it --rm --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest

- redis-cli:

        docker exec -it redis-stack-server redis-cli

- conda env:    

        conda install -c anaconda redis 
        conda install -c anaconda redis-py

- default port: 6379
- check working: redis-cli ping
- redis-server: if Creating Server TCP listening socket *:6379:No such file or directory -> redis-cli -> shutdown



## **Getting Started**        

        git clone https://github.com/RediSearch/redisearch-getting-started

- data tests: 

        redis-cli -h localhost -p 6379 < ./sample-app/redisearch-docker/dataset/import_users.redis

*if install db .redis appears "The '<' operator is reserved for future use." just use cmd (wiwndow + r: cmd) instead powershell, ...*

- insert by hashes:

        HSET "name" field1 "value" field2 "value" ... 

  *- name include prefix (ex: movie:11002, embedding:1, ... => prefix is "movie:", "embedding:", ...)*

- creata index:

        FT.CREATE "name" ON hash PREFIX 1 "prefix:" SCHEMA field1 TEXT SORTABLE field2 NUMERIC SORTABLE field3 NUMERIC SORTABLE field4 TAG SORTABLE

  | Parameter	| Description |
  | --- | --- |
  | `name` | the name of the index|
  | `ON hash` | the type of data structure to be indexed |
  | `PREFIX 1 "prefix:"`| the prefix of the keys that should be indexed. This is a list, so since you want to only index movie:* keys, the number is 1. With two key prefixes, your definition would look like this: PREFIX 2 "movie:" "tv_show:"|
  |`SCHEMA ...	`|defines the fields, their types, and whether the index should be sortable. As you can see in the command, possible types are TEXT, NUMERIC and TAG. SORTABLE is an additional parameter.|

- info : 

        FT.INFO idx:movie

- remove all key: 

        redis-cli flushall


## **Query data**

        FT.SEARCH index_name "info"
        FT.SEARCH index_name "info" RETURN 2 field1 field2

        *query on a specific field*
        FT.SEARCH index_name "@field:info" RETURN 2 field1 field2

        ...
## Reference
https://redis-py.readthedocs.io/en/stable/examples/search_vector_similarity_examples.html#OpenAI-Embeddings
https://github.com/RediSearch/redisearch-getting-started/tree/master