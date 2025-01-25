from flask import Flask, render_template, request, redirect, url_for
#from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

# MySQL database connection configuration

def get_db_connection():
    conn = mysql.connector.connect(
        host="172.17.0.3",      # Change this to your MySQL host (use "localhost" for local DB)
        user="root",           # Replace with your MySQL username
        password="redhat",  # Replace with your MySQL password
        database="user_data"   # Replace with your database name
    )
    return conn

#app.config['MYSQL_HOST'] = '172.17.0.3'  # MySQL server address (use 'localhost' if it's on your machine)
#app.config['MYSQL_USER'] = 'root'  # MySQL username
#app.config['MYSQL_PASSWORD'] = 'redhat'  # MySQL password (set this to your password)
#app.config['MYSQL_DB'] = 'user_data'  # The database you created earlier

# Initialize MySQL
#mysql = MySQL(app)

# Route for Home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for About page
#@app.route('/about')
#def about():
 #   return render_template('about.html')

# Route for Contact page (displays the form and handles form submission)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        conn = get_db_connection()
        cur = conn.cursor()
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert into the MySQL database
        #cur = mysql.connection.cursor()
        cur.execute('''
            INSERT INTO contacts (name, email, message) 
            VALUES (%s, %s, %s)
        ''', (name, email, message))
        #mysql.connection.commit()
        conn.commit()
        conn.close()

        # Redirect to a thank you page (or show a success message)
        return redirect(url_for('thank_you'))

    return render_template('contact.html')

# Route for the thank you page (after form submission)
@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# Route to view all contact submissions (for testing)
@app.route('/about')
def about():
    conn = get_db_connection()
    cur = conn.cursor()
    #cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    contacts = cur.fetchall()
    conn.close()
    return render_template('about.html', contacts=contacts)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

