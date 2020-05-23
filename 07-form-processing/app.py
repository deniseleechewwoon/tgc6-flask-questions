from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.template.html')

@app.route('/book')
def book():
    return render_template('book.template.html')


@app.route('/book', methods=['POST'])
def process_form():
    print(request.form)
    customer_name = request.form.get('customer_name')
    sitting_type = request.form.get('sitting_type')
    time = request.form.get('time')
    services = request.form.getlist('services')
    how_did_you_hear_about_us = request.form.get('how_did_you_hear_about_us')


    return render_template('processbooking.template.html',
                           customer_name=customer_name,
                           sitting_type=sitting_type,
                           time=time,
                           services=", ".join(services),
                           how_did_you_hear_about_us=how_did_you_hear_about_us)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)