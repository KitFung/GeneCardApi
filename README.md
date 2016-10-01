# GeneCardApi
----

A simple api server to distribute the crawled data from genecard.


## Requirement
----

- monogodb

- python

## Usage

Install python package
```
pip install -r requirements.txt
```


Create admin user in mongodb
```
db.createUser({user:'admin', pwd:'password', roles:[{role:'userAdminAnyDatabase', db: 'admin'}]})

```
