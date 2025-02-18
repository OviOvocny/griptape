from pytest import fixture
from griptape.config import OpenAiStructureConfig


class TestOpenAiStructureConfig:
    @fixture(autouse=True)
    def mock_openai(self, mocker):
        return mocker.patch("openai.OpenAI")

    @fixture
    def config(self):
        return OpenAiStructureConfig()

    def test_to_dict(self, config):
        assert config.to_dict() == {
            "type": "OpenAiStructureConfig",
            "prompt_driver": {
                "type": "OpenAiChatPromptDriver",
                "base_url": None,
                "model": "gpt-4o",
                "organization": None,
                "response_format": None,
                "seed": None,
                "temperature": 0.1,
                "max_tokens": None,
                "stream": False,
                "user": "",
            },
            "conversation_memory_driver": None,
            "text_to_speech_driver": {"type": "DummyTextToSpeechDriver"},
            "embedding_driver": {
                "base_url": None,
                "model": "text-embedding-3-small",
                "organization": None,
                "type": "OpenAiEmbeddingDriver",
            },
            "image_generation_driver": {
                "api_version": None,
                "base_url": None,
                "image_size": "512x512",
                "model": "dall-e-2",
                "organization": None,
                "quality": "standard",
                "response_format": "b64_json",
                "style": None,
                "type": "OpenAiImageGenerationDriver",
            },
            "image_query_driver": {
                "api_version": None,
                "base_url": None,
                "image_quality": "auto",
                "max_tokens": 256,
                "model": "gpt-4-vision-preview",
                "organization": None,
                "type": "OpenAiVisionImageQueryDriver",
            },
            "vector_store_driver": {
                "embedding_driver": {
                    "base_url": None,
                    "model": "text-embedding-3-small",
                    "organization": None,
                    "type": "OpenAiEmbeddingDriver",
                },
                "type": "LocalVectorStoreDriver",
            },
        }

    def test_from_dict(self, config):
        assert OpenAiStructureConfig.from_dict(config.to_dict()).to_dict() == config.to_dict()
