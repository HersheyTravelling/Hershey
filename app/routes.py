from flask import render_template, request, redirect, url_for

from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'country': request.form['country'],
            'city': request.form['city'],
            'town': request.form['town'],
            'dob': request.form['dob'],
            'pob': request.form['pob'],
            'contact': request.form['contact'],
            'signature': request.form['signature'],
            'form': request.form['job']
        }
        from .email import send_email
       
        body = f"""
        Name: {data['name']}
        Country: {data['country']}
        City: {data['city']}
        Town: {data['town']}
        Date of Birth: {data['dob']}
        Place of Birth: {data['pob']}
        Contact: {data['contact']}
        Job: {data['form']}
        Signature: {data['signature']}
        """
        send_email(body)

        print(data)
        return redirect(url_for('main.contactus'))

    return render_template('form.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contactus')
def contactus():
    return render_template('contactus.html')