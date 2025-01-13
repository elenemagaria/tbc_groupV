from flask import render_template, redirect, url_for
from ext import app, db
from forms import UploadForm, RegistrationForm, LoginForm
from models import Product, User
from os import path
from flask_login import login_user, logout_user, login_required, current_user

profiles = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pets")
def pets():
    return render_template("pets.html")


from flask_login import current_user

@app.route('/added_products')
def products():
    if current_user.is_authenticated:
        role = current_user.role
    else:
        role = 'Guest'

    products = Product.query.all()
    return render_template('pets.html', products=products, role=role)



@app.route("/upload_post", methods=["GET", "POST"])
@login_required
def create_post():
        form = UploadForm()
        if form.validate_on_submit():
            print("form submitted successfully")
            new_product = Product(
                name=form.name.data,
                breed=form.breed.data,
                description=form.description.data,
                img=form.img.data
            )
            image = form.img.data
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)

            new_product.img = image.filename


            new_product.create()
            return redirect("/added_products")
        else:
            print("Form validation failed:", form.errors)


        return render_template("post.html", form=form)





@app.route("/Sign_up", methods=["GET", "POST"])
def create_user():
        form = RegistrationForm()
        if form.validate_on_submit():
            print("elenemagaria")
            new_user = User(
                name=form.name.data,
                username=form.username.data,
                email=form.email.data,
                number=form.number.data,
                password=form.password.data,
                img=form.img.data)

            image = form.img.data
            directory = path.join(app.root_path, "static", "images", image.filename)

            new_user.img = image.filename
            img = image.filename

            new_user.create()
        else:
            print("buuuuuuuuuuuuuu", form.errors)


        return render_template("new_user.html", form=form)










@app.route("/dogs")
def dogs():
    return render_template("dogs.html")

@app.route("/parrots")
def parrots():
    return render_template("parrots.html")

@app.route("/cats")
def cats():
    return render_template("cats.html")

@app.route("/hamsters")
def hamsters():
    return render_template("hamsters.html")


@app.route("/about_us")
def about():
    return render_template("about_us.html")

@app.route("/product_detail/<int:product_id>")
def product(product_id):
    product= Product.query.get(product_id)
    return render_template("product_detail.html", product=product)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("login successfull")
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            print("failed", form.errors)
    return render_template("login1.html", form=form)
@app.route("/Logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete()
    return redirect("/pets")