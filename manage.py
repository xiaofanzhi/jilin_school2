from flask import Flask,render_template,jsonify
from flask_cors import CORS
from gexf import Gexf
app = Flask(__name__,static_folder='', static_url_path='')







@app.route('/chanye_zhuanye_bneke')
def chanye_zhuanye_bneke():
    return render_template('chanye_zhuanye_bneke.html')

@app.route('/school_chanye')
def school_chanye():
    return render_template('school_chanye.html')


@app.route('/school_xuke')
def school_chanye():
    return render_template('school_xuke.html')







if __name__=='__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
    CORS(app)