from flask import Blueprint, render_template, redirect, url_for, request, flash
from kemistry.models.post import Post
from kemistry.models.comment import Comment
from kemistry.forms.form import BlogPostForm, EditBlogPostForm
from flask_security import current_user
from kemistry import db
from kemistry.forms.form import CommentForm
from flask_security import auth_required

post = Blueprint("post1", __name__)


@post.route("/write", methods=["GET", "POST"])
@auth_required()
def write():
    """
    Define a new write view function that enable users to
    write their blog posts(title, content, post image etc)
    and persist the data to the db.

    They will then be redirected to the homepage which
    will have their new post rendered as the 1st post
    on the homepage.
    """

    form = BlogPostForm()

    if form.validate_on_submit():
        # If the form is submitted and passes validation
        # Create a new Post object and save it to the database
        new_post = Post(
            title=form.title.data, content=form.content.data, user_id=current_user.id
        )

        db.session.add(new_post)
        db.session.commit()

        # Redirect to a success page or the homepage
        return redirect(url_for("user1.home"))

    return render_template("write_post.html", form=form)


@post.route("/post/<string:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    """
    Render a page displaying an individual blog post.

    Args:
        post_id (int): The ID of the post to display.

    Returns:
        A rendered template of the individual post page.
    """
    post = Post.query.get_or_404(post_id)
    form = CommentForm()

    if request.method == "POST" and form.validate_on_submit():
        comment_name = form.name.data
        comment_email = form.email.data
        comment_message = form.message.data

        new_comment = Comment(
            name=comment_name,
            email=comment_email,
            message=comment_message,
            post_id=post_id,
        )

        db.session.add(new_comment)
        db.session.commit()

        # Flash sucess message and refresh page
        flash("Your comment has been submitted successfully!", "success")
        return redirect(url_for("post1.show_post", post_id=post_id))

    return render_template("post.html", post=post, form=form, comments=post.comments)


@post.route("/edit/<string:post_id>")
@auth_required()
def edit_post():
    """
    Allow post authors to edit their post title and content.
    """
    form = EditBlogPostForm()

    return render_template("edit_post.html", form=form)


@post.route("/delete/<string:post_id>")
@auth_required()
def delete_post():
    """
    Allow post authors to delete their post.
    """

    return redirect(url_for("/"))