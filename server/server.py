from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

app.url_map.merge_slashes = False
app.url_map.strict_slashes = False


def get_json(endpoint):
    with open(f'jsons/{endpoint}.json', encoding='utf8') as f:
        return json.load(f)

@app.route('/')
def index():
    return 'lol'

@app.route('/api//health')
def health():
    return 'OK'

@app.route('/api//login', methods=['GET', 'POST'])
def login():
    d = jsonify(get_json('login'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/', methods=['GET', 'POST'])
def api():
    return jsonify(get_json('api'))

@app.route('/api/accounts/membership/login', methods=['POST'])
def membership_login():
    print('login' + request.data.decode('utf8'))
    return 'lol'

@app.route('/api/v1/configs/type/events')
def events():
    d = jsonify(get_json('events'))
    return d
    
@app.route('/api/v1/configs/type/infocasts')
def infocasts():
    d = jsonify(get_json('infocasts'))
    return d


@app.route('/api/v1/configs/type/trm_wartable')
def wartable():
    d = jsonify(get_json('wartable'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/v1/configs/type/trm_events')
def tm_events():
    d = jsonify(get_json('tm_events'))
    d.headers['Connection'] = 'keep-alive'
    return d


@app.route('/api/v1/me/component/entitlements/path/membership')
def membership():
    d = jsonify(get_json('membership'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/v1/me/component/progressions')
def progressions():
    d = jsonify(get_json('progressions'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/v1/configs/type/progression')
def progerssion():
    d = jsonify(get_json('progression'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/v1/me/component/presences/key/Player')
def player():
    d = jsonify(get_json('player'))
    d.headers['Connection'] = 'keep-alive'
    return d


@app.route('/api/v1/configs/type/trm_warzones/id/<war_id>')
def warzone_id(war_id):
    d = jsonify(get_json(f'missions/{war_id}'))
    d.headers['Connection'] = 'keep-alive'
    return d


@app.route('/api/v1/configs/type/itemOffers')
def itemOffers():

    n = request.args.get('continue')
    d = None
    if n == None:
        d = jsonify(get_json(f'itemsOffers'))
    else:
        d = jsonify(get_json(f'itemsOffers_{n}'))
    d.headers['Connection'] = 'keep-alive'
    return d

@app.route('/api/v1/me/component/items')
def item():

    d = jsonify(get_json(f'items'))
    d.headers['Connection'] = 'keep-alive'
    return d


@app.errorhandler(405)
def whygod(e):
    if 'trm_warzones' in request.url:
         return warzone_id(request.url.split('/')[-1])

    return login()

if __name__ == '__main__':
    app.run('127.0.0.1', 443, debug=True, ssl_context='adhoc')
