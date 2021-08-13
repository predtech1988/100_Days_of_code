from flask import (
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user

from market import app, db
from market.forms import LoginForm, PurchaseItemForm, RegisterForm, SellItemForm
from market.models import Item, User


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    items = Item.query.all()
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        # Buying item 
        purchased_item = request.form.get("purchased_item")
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.bye_item(current_user)
                flash(f"Congrats! You are purchased item {p_item_object.name}")
            else:
                flash("Not enough money")
        # Selling items
        sold_item = request.form.get("sold_item")
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congrats! You are sold item {s_item_object.name}")
            else:
                flash(f"Sorry! You can't sell item {s_item_object.name}")
        return redirect(url_for("market_page"))
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id).all()
        return render_template(
            "market.html",
            items=items,
            purchase_form=purchase_form,
            owned_items=owned_items,
            selling_form=selling_form,
        )


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            user_name=form.user_name.data,
            email_address=form.email_address.data,
            password=form.password1.data,
        )
        db.session.add(new_user)
        db.session.commit()
        # db.session.close()
        login_user(new_user)
        flash(f"Welcome {new_user.user_name} you are registered.", category="success")
        return redirect(url_for("market_page"))
    if form.errors:
        for error in form.errors.items():
            flash(f"There was an error with creating user: {error} ", category="danger")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name=form.user_name.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f"You are logged in as {attempted_user.user_name}", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Login or password is incorrect.", category="danger")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You are Logged out", category="info")
    return redirect(url_for("home_page"))
