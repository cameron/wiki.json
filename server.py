import wikipedia
from flask import Flask, make_response, request
import functools
import json
import os


app = Flask(__name__)


def respond_with_headers(headers={}):
  def decorator(original_handler):
    @functools.wraps(original_handler)
    def new_handler(*args, **kwargs):
      res = make_response(original_handler(*args, **kwargs))
      h = res.headers
      for header, value in headers.items():
        h[header] = value
      return res
    return new_handler
  return decorator


def api(handler):
  @functools.wraps(handler)
  @respond_with_headers({'Content-type': 'application/json'})
  def api_handler(*args, **kwargs):
    error_msg = None
    res_code = 200
    result = handler(*args, **kwargs)
    if isinstance(result, tuple) and len(result) == 2:
      (error_msg, res_code), result = result
    return make_response(json.dumps({'error': error_msg, 'data': result}), res_code)
  return api_handler


@app.route('/')
@api
def index():
  return ('Invalid path %s. Try %s' % (path, doc_str), 400), None


@app.route('/<str:method>/<str:arg')
@api
def wiki(method, arg):
  result = getattr(wikipedia, path)(request.args['query'])
  if method == 'page'
    result = {'url': result.url, 'content': result.content, 'title': result.title, 'links': result.links}
  return result


if __name__ == "__main__":
  app.run(host='0.0.0.0', 
          debug=os.environ.get('DEBUG', False), 
          port=os.environ.get(int('PORT'), 80))
