application= Flask(__name__)
app=application

ridge_model=pickle.load(open('RLE/ridge.pkl','rb'))
scaler=pickle.load(open('RLE/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')