from importlib import import_module
from types import ModuleType
from typing import Optional


INSTALL_MAPPING = {
    "huggingface_hub": "huggingface-hub",
    "pinecone": "pinecone-client",
    "opensearchpy": "opensearch-py",
    "google.generativeai": "google-generativeai",
}


def import_optional_dependency(name: str) -> Optional[ModuleType]:
    """Import an optional dependency.

    If a dependency is missing, an ImportError with a nice message will be raised.

    Args:
        name: The module name.
    Returns:
        The imported module, when found.
        None is returned when the package is not found and `errors` is False.
    """

    package_name = INSTALL_MAPPING.get(name)
    install_name = package_name if package_name is not None else name

    msg = f"Missing optional dependency: '{install_name}'. " f"Use poetry or pip to install '{install_name}'."
    try:
        module = import_module(name)
    except ImportError:
        raise ImportError(msg)

    return module


def is_dependency_installed(name: str) -> bool:
    """Check if an optional dependency is available.

    Args:
        name: The module name.
    Returns:
        True if the dependency is available.
        False if the dependency is not available.
    """
    try:
        import_optional_dependency(name)
    except ImportError:
        return False

    return True
