import logging
from flask import Blueprint, render_template, request
from kemistry.models.user import User
from kemistry.models.post import Post
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc
import markdown

search_bp = Blueprint("search1", __name__)

logger = logging.getLogger(__name__)


@search_bp.route("/search", methods=["GET"])
def search():
    """
    Search for posts based on post tag or post author, and order them by date created in descending order.
    """
    query = request.args.get("query", "")

    try:
        # Search for posts based on tags
        tag_posts = (
            Post.query.filter(Post.tag.ilike(f"%{query}%"))
            .order_by(desc(Post.created_at))
            .all()
        )

        for tag_post in tag_posts:
            tag_post.content = markdown.markdown(tag_post.content)

        # Search for posts by author name
        author_posts = (
            Post.query.join(User)
            .filter(
                (User.first_name.ilike(f"%{query}%"))
                | ((User.first_name + " " + User.last_name).ilike(f"%{query}%"))
            )
            .filter(Post.user_id == User.id)
            .order_by(desc(Post.created_at))
            .all()
        )

        for author_post in author_posts:
            author_post.content = markdown.markdown(author_post.content)

        # Combine the results
        search_results = tag_posts + author_posts

        return render_template("search.html", query=query, posts=search_results)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        return render_template("500.html"), 500
