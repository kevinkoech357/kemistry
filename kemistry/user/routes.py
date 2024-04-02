from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from kemistry.forms.form import ContactForm, EditProfileForm, RecoverAccountForm
from kemistry.models.post import Post
from kemistry.models.user import User
from flask_security import current_user, auth_required, url_for_security, logout_user
import json
from kemistry import db
import markdown


user = Blueprint("user1", __name__)


@user.route("/", methods=["GET"])
def home():
    """
    Render the homepage with all published blog posts.

    Returns:
        A rendered template of the homepage.
    """
    page = request.args.get("page", 1, type=int)

    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=6)

    total_posts = Post.query.count()

    return render_template("index.html", posts=posts, total_posts=total_posts)


@user.route("/profile", methods=["GET"])
@auth_required()
def profile():
    """
    Render the profile with the current user's
    profile image, bio, qualifications, and all the posts they have ever written.

    Returns:
        A rendered template of the profile.
    """
    # Retrieve the current user's information
    # If user is anonymous, request login
    user = current_user

    if not user:
        return redirect(url_for_security("login"))

    # Retrieve all posts written by the current user
    posts = Post.query.filter_by(author=user).order_by(Post.created_at.desc()).all()

    # Process Markdown content for each post
    for post in posts:
        post.content = markdown.markdown(post.content)

    return render_template("profile.html", user=user, posts=posts)


@user.route("/settings", methods=["GET", "POST"])
@auth_required()
def settings():
    """
    Render the settings page and handle profile updates.

    If the request method is GET, renders the settings page with the current user's data.
    If the request method is POST and the form is valid,
    updates the user's profile data and commits changes to the database.
    Redirects to the profile page after successful update.
    """
    user = current_user

    # Check if a user is logged in
    if not user:
        abort(404)

    # Ensure that only the associated user can access the settings page
    if user.id != current_user.id:
        abort(403)

    form = EditProfileForm()

    # Handle form submission
    if form.validate_on_submit():
        # Update user profile data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.university = form.university.data
        user.qualification = form.qualification.data
        user.bio = form.bio.data

        # Commit changes to the database
        db.session.commit()

        # Flash message to indicate successful profile update
        flash("Profile updated successfully.", "success")

        # Redirect to the settings page to display the updated information
        return redirect(url_for("user1.profile"))

    # Render settings page with form and user data
    return render_template("settings.html", form=form, user=current_user)


@user.route("/suspend-account", methods=["POST"])
@auth_required()
def suspend_account():
    """
    Suspend the current user's account.

    If the request method is POST, suspends the current user's account by setting the 'active' attribute to False.
    Logs out the user after suspending the account.
    Redirects the user to the home page after performing the action.
    """
    user = current_user

    # Check if a user is logged in
    if not user:
        abort(404)

    # Ensure that only the associated user can suspend their account
    if user.id != current_user.id:
        abort(403)

    # Deactivate the user's account
    user.active = False
    db.session.commit()

    # Log out the user
    logout_user()

    flash("Your account has been suspended. You have been logged out.", "warning")
    return redirect(url_for("user1.home"))


@user.route("/delete-account", methods=["POST"])
@auth_required()
def delete_account():
    """
    Delete the current user's account.

    If the request method is POST, deletes the current user's account.
    Logs out the user after deleting the account.
    Redirects the user to the home page after performing the action.
    """
    user = current_user

    # Check if a user is logged in
    if not user:
        abort(404)

    # Ensure that only the associated user can delete their account
    if user.id != current_user.id:
        abort(403)

    # Delete the user's account
    db.session.delete(user)
    db.session.commit()

    # Log out the user
    logout_user()

    flash("Your account has been deleted. You have been logged out.", "danger")
    return redirect(url_for("user1.home"))


@user.route("/recover", methods=["GET", "POST"])
def recover_account():
    """
    Render the recover account page and handle account recovery.

    GET: Renders the recover account form.
    POST: Handles form submission, validates input, and processes account recovery.
    """
    form = RecoverAccountForm()

    if form.validate_on_submit():
        email = form.email.data
        # Check if the email exists in the database
        user = User.query.filter_by(email=email).first()

        if user:
            if user.active:
                # If the account is already active, redirect to login
                flash("Account is already active. Please proceed to login.", "info")
                return redirect(url_for_security("login"))

            # Update the account status to active
            user.active = True
            db.session.commit()
            flash("Account recovered successfully. You can now login.", "success")
            return redirect(url_for_security("login"))
        else:
            # If email does not exist in the database, display an error message
            form.email.errors.append("Email does not exist")

    return render_template("recover.html", form=form)


@user.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Render the contact page and handle contact form submissions.

    GET:
        Renders the contact form.

    POST:
        Validates and processes the contact form data, saves it to a JSON file,
        and redirects the user to the homepage.

    Returns:
        For GET requests: A rendered template of the contact form.
        For POST requests: A redirect to the homepage after form submission.
    """
    form = ContactForm()

    if form.validate_on_submit():
        form_data = {
            "name": form.name.data,
            "email": form.email.data,
            "message": form.message.data,
        }
        save_data_to_json(form_data)
        flash("Message sent successfully! We'll get back to you soon.", "success")
        return redirect(url_for("user1.home"))

    return render_template("contact.html", form=form)


def save_data_to_json(data):
    """
    Save contact form data to a JSON file.

    Args:
        data: A dictionary containing contact form data (name, email, message).

    Returns:
        None
    """
    try:
        with open("contact.json", "a") as json_file:
            json.dump(data, json_file, indent=3)
            json_file.write("\n")

    except Exception as e:
        print(f"Error saving data to JSON file: {str(e)}")
