from __future__ import annotations

from abc import ABC

from attr import define

from griptape.mixins import RuleMixin, BlobArtifactFileOutputMixin
from griptape.tasks import BaseTask


@define
class BaseAudioGenerationTask(BlobArtifactFileOutputMixin, RuleMixin, BaseTask, ABC): ...
