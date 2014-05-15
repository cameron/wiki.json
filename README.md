# wiki.json

A python webserver serving wikipedia via JSON.

# quick

```
> docker run -p 40080:80 -d camron/wiki.json
> curl '$DOCKER_HOST:40080/pages/Buddhism'
{ "data": {
    "content": "...",
    "title": "...",
    "url": "...",
    "links": ["<page-title>", ]
  },
  "error": null }
```
