from attrs import Factory, define, field

from griptape.config import StructureConfig
from griptape.drivers import (
    BaseEmbeddingDriver,
    BaseImageGenerationDriver,
    BaseImageQueryDriver,
    BasePromptDriver,
    BaseVectorStoreDriver,
    LocalVectorStoreDriver,
    OpenAiChatPromptDriver,
    OpenAiEmbeddingDriver,
    OpenAiImageGenerationDriver,
    OpenAiVisionImageQueryDriver,
)


@define
class OpenAiStructureConfig(StructureConfig):
    prompt_driver: BasePromptDriver = field(
        default=Factory(lambda: OpenAiChatPromptDriver(model="gpt-4o")), metadata={"serializable": True}, kw_only=True
    )
    image_generation_driver: BaseImageGenerationDriver = field(
        default=Factory(lambda: OpenAiImageGenerationDriver(model="dall-e-2", image_size="512x512")),
        kw_only=True,
        metadata={"serializable": True},
    )
    image_query_driver: BaseImageQueryDriver = field(
        default=Factory(lambda: OpenAiVisionImageQueryDriver(model="gpt-4-vision-preview")),
        kw_only=True,
        metadata={"serializable": True},
    )
    embedding_driver: BaseEmbeddingDriver = field(
        default=Factory(lambda: OpenAiEmbeddingDriver(model="text-embedding-3-small")),
        metadata={"serializable": True},
        kw_only=True,
    )
    vector_store_driver: BaseVectorStoreDriver = field(
        default=Factory(
            lambda: LocalVectorStoreDriver(embedding_driver=OpenAiEmbeddingDriver(model="text-embedding-3-small"))
        ),
        kw_only=True,
        metadata={"serializable": True},
    )
