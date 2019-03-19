#  Django + +REST + Couch Example

By James Ravenscroft

## Installation

First make sure you have Apache CouchDB running on your system or another
machine. The file `icml/settings.py` has a `COUCHDB_SERVER` value which is used
to point Django to the correct location if it isn't installed locally.

Run the following code to install and run the django server:

```

## create virtualenv
virtualenv env
source env/Scripts/activate[windows]
source env/bin/activate[[linux/mac]

## run this file
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

Use something like [Postman](https://www.getpostman.com/docs/introduction) to
test the API endpoints.

### POST /create

You can post a JSON object to this URL to create a blogpost in Couchdb:

```json
{
  "title" : "Latent Dirichlet Allocation",
  "abstract" : "We describe latent Dirichlet allocation (LDA), a generative...",
  "type" : "journal"
}
```

The response will be a carbon copy of your input data plus the relevant ID

```json
{
    "id": "aca829985ae176a11a1b996ae900253b",
    "title": "Latent Dirichlet Allocation",
    "abstract": "We describe latent Dirichlet allocation (LDA), a generative...",
    "type": "journal"
}"type" : "journal"
}
```

### GET /blogdetail/<id>

Given an ID, return JSON representation of that blog post from CouchDB.

```
GET /blogdetail/aca829985ae176a11a1b996ae900253b
```

...

```json
{
    "id": "aca829985ae176a11a1b996ae900253b",
    "title": "Latent Dirichlet Allocation",
    "abstract": "We describe latent Dirichlet allocation (LDA), a generative...",
    "type": "journal"
}
```
