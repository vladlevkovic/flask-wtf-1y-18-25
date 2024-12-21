from flask import Flask, render_template, request, redirect
from forms import SubscribeForm, IceCreamForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/dosearch/')
def do_search():
    s = request.args.get('s')
    return f'Відбувається пошук по запиту {s}'

@app.route('/getsearch/')
def get_search():
    print(request.args)
    mail = request.args.get('mail')
    return f'Передача параметра {mail} з методом {request.method}'

@app.route('/postsearch/', methods=['POST'])
def post_search():
    print(request.form)
    mail = request.form.get('mail')
    return f'Передача параметра {mail} з методом {request.method}'

@app.route('/subscribe/', methods=['GET', 'POST'])
def subscribe():
    form = SubscribeForm()
    return render_template('subscribe.html', form=form)

@app.route('/subscribe-result/', methods=['GET', 'POST'])
def form_result():
    return 'Форма відправлена'

@app.route('/ice/', methods=['GET', 'POST'])
def ice():
    form = IceCreamForm()
    form.tastes.choices = [('vanilla', 'vanilla'), ('choko', 'choko'), ('mango', 'mango')]
    form.topping.choices = [('coffe', 'coffe'), ('strawberry', 'strawberry')]
    form.cup_size.choices = [('little', 'little'), ('medium', 'medium'), ('big', 'big')]
    if request.method == 'GET':
        return render_template('ice.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
