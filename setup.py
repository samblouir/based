from setuptools import setup, find_packages

# ensure that torch is installed, and send to torch website if not
try:
    import torch
except ModuleNotFoundError:
    raise ValueError("Please install torch first: https://pytorch.org/get-started/locally/")

_REQUIRED = [
    "packaging",
    "protobuf",
    "fsspec",
    "datasets",
    "aiohttp",  # https://github.com/aio-libs/aiohttp/issues/6794
    "dill",
    "multiprocess",
    "huggingface-hub",
    "transformers",
    "einops",
    "ftfy",
    "opt-einsum",
    "pydantic",
    "pydantic-core",
    "pykeops",
    "python-dotenv",
    "sentencepiece",
    "tokenizers",
    "six",
    "scikit-learn",
    "lm-eval",
    "ninja",
    "flash-attn",
    "causal-conv1d",
]

_OPTIONAL = {
    "train": [
        "rich",
        "hydra-core",
        "hydra_colorlog",
        "wandb",
        "lightning-bolts",
        "lightning-utilities",
        "pytorch-lightning",
        "timm",
    ],
    "dev": [
        "pytest",
    ],
}

setup(
    name='based',
    version="0.0.1",
    packages=find_packages(include=['based', 'based.*']),
    author="Based",
    author_email="",
    description="",
    python_requires=">=3.8",
    install_requires=_REQUIRED,
    extras_require=_OPTIONAL,
)
