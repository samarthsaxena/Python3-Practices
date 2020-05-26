#!/usr/bin/env3 python3

from flaskblog import app

# @app.route("/test")
# def testpage():
#     return render_template('testpage.html', title='Test Page')


if __name__ == '__main__':
    app.run(debug=True)
