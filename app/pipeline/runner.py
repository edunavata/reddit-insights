# app/pipeline/runner.py

from abc import ABC, abstractmethod
from typing import Any, Protocol
from app.db.session import SessionLocal
from app.utils.logger import get_logger

logger = get_logger(__name__)


class StepContext(Protocol):
    """Protocol for shared context passed to steps."""

    db: Any


class PipelineStep(ABC):
    """
    Abstract base class for a pipeline step.
    """

    @abstractmethod
    def process(self, data: Any, context: StepContext) -> Any:
        """
        Process a step with input and shared context.

        :param data: Input from previous step
        :param context: Shared context (e.g., DB)
        :return: Output for next step
        """
        pass


class Pipeline:
    """
    Orchestrates and runs the pipeline.
    """

    def __init__(self):
        self.steps: list[PipelineStep] = []

    def add_step(self, step: PipelineStep) -> None:
        """
        Add a step to the pipeline sequence.
        """
        self.steps.append(step)

    def run(self, initial_data: Any = None) -> Any:
        """
        Execute all steps in sequence.
        """
        db = SessionLocal()
        context = type("Context", (), {"db": db})()
        data = initial_data

        try:
            for step in self.steps:
                logger.info(f"Running step: {step.__class__.__name__}")
                data = step.process(data, context)
        except Exception as e:
            logger.error(f"Pipeline failed: {e}", exc_info=True)
            raise
        finally:
            db.close()

        return data

    @classmethod
    def run_default(cls) -> None:
        """
        Run the default pipeline.
        No steps defined yet.
        """
        logger.info("Starting default pipeline with no steps.")
        pipeline = cls()
        # app/pipeline/runner.py (en método run_default)

        from app.pipeline.steps.fetch import FetchRedditPosts
        from app.pipeline.steps.filter import FilterAndStoreNewPosts
        from app.pipeline.steps.analyze import AnalyzePosts
        from app.pipeline.steps.store_analysis import StoreAnalysis

        # futuras etapas se importarán aquí también

        pipeline.add_step(FetchRedditPosts(subreddits=["smallbusiness"], limit=25))
        pipeline.add_step(FilterAndStoreNewPosts())
        pipeline.add_step(AnalyzePosts())
        pipeline.add_step(StoreAnalysis())

        pipeline.run()
