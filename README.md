# functions-from-zero

[![Python application test with Github Actions](https://github.com/eyamao/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/eyamao/functions-from-zero/actions/workflows/main.yml)


### To call Microservice

Somethig like this
´´´bash
curl -X 'POST' \
  'https://eyamao-reimagined-cod-qpjwjp74rrgf9v6x-8080.preview.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
´´´

### Build container

'docker build .'
'docker image ls'
