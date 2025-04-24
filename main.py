#!/usr/bin/env python3
# vim: set et ft=python fileencoding=utf_8 ts=4 sw=4:
# -*- coding: utf_8 -*-
r"""Main execution module.

Typical usage example:

    system = MultiAgentSystem()

    user_input = \"\"\"
    datapath:
    Use machine learning to perform data analysis on this historical price data
    for various symbols and determine whether a symbol will rise or fall in
    price.
    \"\"\"

    system.run(user_input)
"""

import os
from typing import Dict, Any
from logger import setup_logger
from langchain_core.messages import HumanMessage

from load_cfg import OPENAI_API_KEY, LANGCHAIN_API_KEY, WORKING_DIRECTORY
from core.workflow import WorkflowManager
from core.language_models import LanguageModelManager


class MultiAgentSystem:
    """A class to represent the main execution system agent."""

    def __init__(self):
        """Initialize class members variables."""
        self.logger = setup_logger()
        self.setup_environment()
        self.lm_manager = LanguageModelManager()
        self.workflow_manager = WorkflowManager(
            language_models=self.lm_manager.get_models(),
            working_directory=WORKING_DIRECTORY
        )

    def setup_environment(self):
        """Initialize environment variables."""
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = "Multi-Agent Data Analysis System"

        if not os.path.exists(WORKING_DIRECTORY):
            os.makedirs(WORKING_DIRECTORY)
            self.logger.info("Created working directory: %s", WORKING_DIRECTORY)

    def run(self, user_input: str) -> None:
        """Run the multi-agent system with user input."""
        graph = self.workflow_manager.get_graph()
        events: Dict[
            str,
            Any] = graph.stream({
                "messages": [HumanMessage(content=user_input)],
                "hypothesis": "",
                "process_decision": "",
                "process": "",
                "visualization_state": "",
                "searcher_state": "",
                "code_state": "",
                "report_section": "",
                "quality_review": "",
                "needs_revision": False,
                "last_sender": "",
            },
                                {
                                    "configurable": {
                                        "thread_id": "1"
                                    },
                                    "recursion_limit": 3000
                                },
                                stream_mode="values",
                                debug=False)

        for event in events:
            message = event["messages"][-1]
            if isinstance(message, tuple):
                print(message, end="", flush=True)
            else:
                message.pretty_print()


def main():
    """Main entry point."""
    system = MultiAgentSystem()

    # Example usage
    user_input = """
    datapath:
    Use machine learning to perform data analysis on this historical price data
    for various symbols and determine whether a symbol will rise or fall in
    price.
    """
    system.run(user_input)


if __name__ == "__main__":
    main()
