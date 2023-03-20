import csv

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')


@app.route('/organization')
def organization():
    with open('static/organization.csv') as f:
        doc_list = list(csv.reader(f))
    return render_template('organization.html', doc_list=doc_list)


@app.route('/news')
def news():
    news_list = load_news_from_csv('static/news.csv')
    return render_template('news.html', news_list=news_list)


def load_news_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        news_list = []
        for row in reader:
            # title, date, content = row
            news_list.append((row[0], row[1], row[2], row[3], row[4]))
    return news_list


@app.route('/news/snowstorm')
def snowstorm():
    return render_template('snowstorm.html')


@app.route('/news/newart')
def newart():
    return render_template('newArt.html')


@app.route('/news/charity')
def charity():
    return render_template('charity.html')


@app.route('/careers')
def careers():
    jobs = [
        ('School Assistants (Lunch-Time Supervisors)',
         'https://network.applytoeducation.com/Applicant/AttJobPosting.aspx?JOB_POSTING_ID=bbc03222-f615-4e7e-a094-a8b9204bb29a',
         'The role of the school assistant is to provide supervisory support to teaching staff during peak or '
         'critical periods of the school day.'),
        ('Planner (Term)',
         'https://network.applytoeducation.com/Applicant/AttJobPosting.aspx?JOB_POSTING_ID=6c524205-2c34-4fb1-81fc-b3fb77ed9da5',
         'Interested staff members are required to complete the following on-line application to the attention of: '
         'The Recruitment Team.  This position is effective immediately and is ending on or about March 8, 2024.'),
        ('Systems Analyst, Information Technology Services',
         'https://network.applytoeducation.com/Applicant/AttJobPosting.aspx?JOB_POSTING_ID=522199fc-e7b6-4655-a477-44599b76fef9',
         'Interested applicants are required to complete the following on-line application to the attention of:  The '
         'Recruitment Team.  This permanent position is effective immediately.'),
        ('Payroll Accountant',
         'https://network.applytoeducation.com/Applicant/AttJobPosting.aspx?JOB_POSTING_ID=1f2d634d-fe45-430b-b1f8-e3a4e81ce3d5',
         'In compliance with Board policies and procedures, responsible for the accounting function as it relates to '
         'payroll transactions, the maintenance of appropriate records and the preparation of related journal '
         'entries, reconciliations.')
    ]
    return render_template('careers.html', jobs=jobs)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contact/response', methods=['POST'])
def response():
    return render_template('response.html', data=request.form)


if __name__ == '__main__':
    app.run()
