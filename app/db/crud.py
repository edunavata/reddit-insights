# app/db/crud.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db import models
from typing import Dict, Optional
from datetime import datetime


def get_post(db: Session, post_id: str) -> Optional[models.Post]:
    """
    Retrieve a post by its Reddit ID.
    """
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def create_post(db: Session, post_data: Dict) -> models.Post:
    """
    Insert a new post into the database.

    :param db: SQLAlchemy session
    :param post_data: Dict containing post fields
    :return: Created Post object
    """
    if isinstance(post_data.get("created_utc"), (int, float)):
        post_data["created_utc"] = datetime.utcfromtimestamp(post_data["created_utc"])

    post = models.Post(**post_data)
    db.add(post)
    try:
        db.commit()
        db.refresh(post)
    except IntegrityError:
        db.rollback()
        raise ValueError("Post already exists")
    return post


def create_post_analysis(
    db: Session, post_id: str, analysis_data: Dict
) -> models.PostAnalysis:
    """
    Store LLM analysis result for a given post.

    :param db: SQLAlchemy session
    :param post_id: Reddit post ID
    :param analysis_data: Dict with LLM analysis fields
    :return: Created PostAnalysis object
    """
    analysis = models.PostAnalysis(post_id=post_id, **analysis_data)
    db.add(analysis)
    try:
        db.commit()
        db.refresh(analysis)
    except IntegrityError:
        db.rollback()
        raise ValueError("Analysis for this post already exists")
    return analysis
