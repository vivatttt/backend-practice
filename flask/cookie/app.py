from flask import Flask, json, redirect, render_template, request, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    return render_template('index.html', cart=cart)


# BEGIN (write your solution here)
@app.post('/cart-items')
def add_in_cart():
    item = request.form.to_dict()

    item_id = item['item_id']
    item_name = item['item_name']

    cart = json.loads(request.cookies.get('cart', json.dumps({})))

    '''
    cart = {
      id :
      { 
        name :
        count :
      }
    }
    '''

    if item_id in cart.keys():
      cart[item_id]['count'] += 1
    else:
      cart[item_id] = {
        'name' : item_name,
        'count' : 1
      }

    encoded_сart = json.dumps(cart)

    response = make_response(redirect('/'))
    response.set_cookie('cart', encoded_сart)
    return response

@app.post('/cart-items/clean')
def clear_cart():
  response = make_response(redirect('/'))
  response.set_cookie('cart', json.dumps({}))
  return response




# END
