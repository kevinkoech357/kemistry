from kemistry import db, admin
from kemistry.models.basemodel import BaseModel
from kemistry.super_admin.view_models import PostView
from kemistry.models.comment import Comment


class Post(BaseModel):
    """
    A class to represent a post in the database.

    Attributes:
        title (str): Blog title
        content (str): The main content of the post.
        user_id (str): The ID of the user who authored the post.
        author (User): The user object representing the author of the post.
        tag (str): The tag associated with the post
    """

    __tablename__ = "post"

    user_id = db.Column(db.String(32), db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tag = db.Column(db.String(255), nullable=False)

    # Relationships
    author = db.relationship("User", back_populates="posts")
    comments = db.relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan"
    )

    def __init__(self, title, content, user_id, tag):
        """
        Initializes a new Post object.

        Args:
            title (str): Blog title
            content (str): The main content of the post.
            user_id (str): The ID of the user who authored the post.
            tag (str): The tag associated with the post
        """
        super().__init__()
        self.title = title
        self.content = content
        self.user_id = user_id
        self.tag = tag

    def generate_excerpt(self, max_length=250):
        """
        Generates an excerpt from the post content.

        Args:
            max_length (int): Maximum length of the excerpt.

        Returns:
            str: The generated excerpt.
        """
        if len(self.content) <= max_length:
            return self.content
        else:
            # Find the nearest word boundary before max_length
            excerpt_end = self.content.rfind(" ", 0, max_length)
            if excerpt_end == -1:
                # If there's no space before max_length, truncate at max_length
                excerpt_end = max_length
            return self.content[:excerpt_end] + " ..."

    def __repr__(self):
        """
        Returns a string representation of the Post object.
        """
        return f"Post(title='{self.title}', content='{self.content[:20]}...', user_id='{self.user_id}')"

    def __str__(self):
        """
        Returns a human-readable string representation of the Post object.
        """
        return f"Title: {self.title}\nExcerpt: {self.generate_excerpt()}"


admin.add_view(PostView(Post, db.session))
