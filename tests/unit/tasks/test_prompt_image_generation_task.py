from unittest.mock import Mock

from griptape.artifacts import TextArtifact
from griptape.engines import PromptImageGenerationEngine
from griptape.structures import Agent
from griptape.tasks import BaseTask, PromptImageGenerationTask
from tests.mocks.mock_image_generation_driver import MockImageGenerationDriver


class TestPromptImageGenerationTask:
    def test_string_input(self):
        task = PromptImageGenerationTask("string input", image_generation_engine=Mock())

        assert task.input.value == "string input"

    def test_callable_input(self):
        input_artifact = TextArtifact("some text input")

        def callable_input(task: BaseTask) -> TextArtifact:
            return input_artifact

        task = PromptImageGenerationTask(callable_input, image_generation_engine=Mock())

        assert task.input == input_artifact

    def test_config_image_generation_engine_engine(self):
        task = PromptImageGenerationTask("foo bar")
        Agent().add_task(task)

        assert isinstance(task.image_generation_engine, PromptImageGenerationEngine)
        assert isinstance(task.image_generation_engine.image_generation_driver, MockImageGenerationDriver)
