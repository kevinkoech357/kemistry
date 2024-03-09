from kemistry import db
from kemistry.models.basemodel import BaseModel


class Comment(BaseModel):
    """
    A class to represent a comment in the database.

    Attributes:
        name (str): The title of the post.
        email (str): The main content of the post.
        message (str): The ID of the user who authored the post.
        post_id (str): ForeignKey of the post id.
        post (Post): The post object representing post's related comments.
    """

    __tablename__ = "comment"

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.String(10), db.ForeignKey("post.id"), nullable=False)

    post = db.relationship("Post", back_populates="comments")

    def __init__(self, name, email, message, post_id):
        """
        Initializes a new Comment object.

        Args:
            name (str): Name of the commentor.
            email (str): Email of the commentor.
            message (str): The comment details.
        """
        super().__init__()
        self.name = name
        self.email = email
        self.message = message
        self.post_id = post_id

    def __repr__(self):
        """
        Returns a string representation of the Comment object
        """
        return f"{self.name} of email {self.email} says {self.message}"

    def __str__(self):
        """
        Returns a human readable representation of Comment object
        """
        return f"{self.name} says {self.message}"
