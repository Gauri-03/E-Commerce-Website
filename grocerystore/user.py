from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from hci.models import User, Product, Category
import json

user = Blueprint("user", __name__)

@user.route("/home/<int:user_id>")
def userdashboard(user_id):
    products = Product.query.all()
    user = User.query.filter_by(id=user_id).first()
    return render_template("userdashboard.html", user=user, products=products)

@user.route("/cart/<int:user_id>", methods=["POST", "GET"])
def cart(user_id):
    user = User.query.filter_by(id=user_id).first()
    cart = json.loads(user.cart)
    cart_products = []
    subtotal = 0
    for product_id, quantity in cart.items():
        product = Product.query.get(int(product_id))
        if product:
            cart_products.append((product, quantity))
            subtotal += product.price * quantity
    return render_template("cart.html", cart_products=cart_products, subtotal=subtotal, user=user)


@user.route("/home/<int:user_id>/addtocart/<int:product_id>", methods=["POST"])
def addtocart(user_id, product_id):
    if request.method == "POST":
        user = User.query.filter_by(id=user_id).first()
        quantity = 1
        cart = json.loads(user.cart)
        cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
        user.cart = json.dumps(cart)
        db.session.commit()
        return redirect(url_for('user.cart', user_id=user_id))
    
@user.route('/cart/<int:user_id>/<int:product_id>', methods = ['POST', 'GET'])
def remove_product(user_id, product_id):
    user = User.query.get(user_id)
    cart = json.loads(user.cart)

    if str(product_id) in cart:
        del cart[str(product_id)]

        user.cart = json.dumps(cart)
        db.session.commit()

    return redirect(url_for('user.cart', user_id = user_id))
    