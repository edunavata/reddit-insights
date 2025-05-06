# app/db/models.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()


class Post(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, index=True)  # Reddit post ID
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author = Column(String)
    created_utc = Column(DateTime, default=datetime.datetime.utcnow)
    url = Column(String)
    permalink = Column(String)
    subreddit = Column(String)
    flair = Column(String, nullable=True)
    score = Column(Integer)
    upvote_ratio = Column(Float)
    num_comments = Column(Integer)
    is_self = Column(Boolean)
    nsfw = Column(Boolean)
    subreddit_subscribers = Column(Integer)

    analysis = relationship("PostAnalysis", back_populates="post", uselist=False)


class PostAnalysis(Base):
    __tablename__ = "post_analyses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(String, ForeignKey("posts.id"), unique=True)
    opportunity = Column(String)
    type = Column(String)
    market_or_niche = Column(Text)
    potential_competitors = Column(Text)
    notes = Column(Text)
    confidence = Column(Float)

    post = relationship("Post", back_populates="analysis")
