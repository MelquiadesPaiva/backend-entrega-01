from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-dev.db'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config["JSON_SORT_KEYS"] = False


db = SQLAlchemy(app)


class User(db.Model):
    
    __tablename__ = 'users'

    
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(20), nullable=False)

    email = db.Column(db.String(20), unique=True, nullable=False)
    
    idade = db.Column(db.Integer, default=0)

    
    def json(self):
        user_json = {'id': self.id,
                     'name': self.name,
                     'email': self.email,
                     'idade': self.idade}
        return user_json
     



@app.route('/users/', methods=['POST'])
def create():

    data = request.json  
    name = data.get('name')
    email = data.get('email')
    idade = data.get('idade')


    if not name or not email:
        
        return {'error': 'Dados insuficientes'}

    if email not unique:

        return {'error: 'email ja existente'}, 400z    

     
    user = User(name=name, email=email, idade=idade)

    
    db.session.add(user)
    db.session.commit()

    
    return user.json(), 200


@app.route('/users/', methods=['GET'])
def index():

   
    data = request.args

   

    idade = data.get('idade')  

    if not idade: 
        users = User.query.all()  
    else:

       
        idade = idade.split('-')

        
        if len(idade) == 1:
            
            users = User.query.filter_by(idade=idade[0])
        else:
          
            users = User.query.filter(
                db.and_(User.idade >= idade[0], User.idade <= idade[1]))

    
    return jsonify([user.json() for user in users]), 200



@app.route('/users/<int:id>', methods=['GET'])
def user_detail(id):
    if request.method == 'GET':
    
        user = User.query.get_or_404(id)
    
        return user.json(), 200




@app.route('/users/<collection>/<member>', methods=['PATCH'])
def patch_users_db(collection,member):
    req = request.get_json()

    if colection in users:
        for email, name, idade in req.items():
            user(name=name,idade=idade,email=email)

            res = make_response(jsonify({'message': 'collection updated'}), 200)

    user[collection] = req 

res = make_response(jsonify({'message': 'collection created'}), 200)
return res , 









if __name__ == '__main__':
    app.run(debug=True)