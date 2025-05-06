# cli.py

from app.pipeline.runner import run_pipeline


def main():
    """
    Entry point to execute the Reddit insights pipeline.
    """
    run_pipeline()


if __name__ == "__main__":
    main()
