from . import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    phonenumber = db.Column(db.String, unique = True)
    cart = db.Column(db.Text, nullable =  False, default = "{}")
    orders = db.Column(db.Text, default = "{}")

    def get_id(self):
        return int(self.id)
    
class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable = False)

    def get_id(self):
        return int(self.id)

class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)
    products = db.relationship("Product", backref = "category")

    def get_id(self):
        return int(self.id)