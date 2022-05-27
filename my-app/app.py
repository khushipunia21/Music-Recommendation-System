from initialise import*
from spotify_api import get_urls
from weekly import *

model=KNeighborsClassifier()
try:
    AUTH_URL = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': "aba68a7c20a14bd89fea91da58bde342",
        'client_secret': "587a8071c09e446e9d857154ef83c95c",
    })

    auth_response_data = auth_response.json()
except Exception as e:
    print("error in auth")
    print(e)

# save the access token

try:
    access_token = auth_response_data['access_token']

    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }


    BASE_URL = 'https://api.spotify.com/v1/'
except Exception as e:
    print("error getting access token")
    print(e)


app=Flask(__name__)

@app.route('/')
def man():
    return render_template('main.html')

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('main.html')

@app.route('/discover_page',methods=['GET','POST'])
def discover_page():
    return render_template('discover_weekly.html')

@app.route('/recommend_page',methods=['GET','POST'])
def recommend_page():
    return render_template('slider.html')
    
@app.route('/recommend',methods=['GET','POST'])
def recommend():
    model.fit(X_train,Y_train)
    input=str(request.form["song1"])
    ind=tempo[tempo['song_name']==input].index
    ind=ind[0]
    arr=model.recommend(X[ind])
    final=[]
    for i in range(10):
        link_list=get_urls(str(arr[i][1]))
        final.append(link_list)
    return render_template('slider.html',data=final)

@app.route('/weekly_recom',methods=['GET','POST'])
def weekly_recom():
    my_id="b80344d063b5ccb3212f76538f3d9e43d87dca9e"
    madeforu=weekly_rec(my_id)
    final=[]
    for i in range(20):
        link_list=get_urls(str(madeforu[i]))
        final.append(link_list)
    return render_template('discover_weekly.html',data=final)

@app.route('/changed',methods=['GET','POST'])
def changed():
    model.fit(X_train,Y_train)
    input='Born 2 Live'
    arr=get_values(str(input))
    val1=float(request.form["val1"])
    val2=float(request.form["val2"])
    val3=float(request.form["val3"])
    new_inp=arr
    new_inp[0]=val1
    new_inp[6]=val2
    new_inp[7]=val3
    ans=model.recommend(new_inp)
    final=[]
    for i in range(10):
        link_list=get_urls(str(ans[i][1]))
        final.append(link_list)
    return render_template('slider.html',data=final)


if __name__=="__main__":
    app.run(debug=True)