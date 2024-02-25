from kemistry import db
from kemistry.models.basemodel import BaseModel


class Post(BaseModel):
    """
    A class to represent a post in the database.

    Attributes:
        title (str): The title of the post.
        content (str): The main content of the post.
        user_id (str): The ID of the user who authored the post.
        author (User): The user object representing the author of the post.
    """

    __tablename__ = "post"

    user_id = db.Column(db.String(), db.ForeignKey("user.id"))
    title = db.Column(db.String(100), nullable=False, index=True)
    content = db.Column(db.Text, nullable=False)
    author = db.relationship("User", back_populates="posts")

    def __init__(self, title, content, user_id):
        """
        Initializes a new Post object.

        Args:
            title (str): The title of the post.
            content (str): The main content of the post.
            user_id (str): The ID of the user who authored the post.
        """
        super().__init__()
        self.title = title
        self.content = content
        self.user_id = user_id

    def generate_excerpt(self, max_length=75):
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
            return self.content[:excerpt_end] + "..."

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
