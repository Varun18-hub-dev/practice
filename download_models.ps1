# Downloads the exact model files used in the project into C:\models (about 2.2 GB).
# Run in PowerShell from this folder:   powershell -ExecutionPolicy Bypass -File .\download_models.ps1
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force C:\models | Out-Null
pip install -q "huggingface_hub>=0.23,<1.0"

# Qwen2.5-3B-Instruct, GGUF Q4_K_M (official Qwen repository)
huggingface-cli download Qwen/Qwen2.5-3B-Instruct-GGUF qwen2.5-3b-instruct-q4_k_m.gguf --local-dir C:\models

# BGE-small-en-v1.5 at the pinned revision used by the project
huggingface-cli download BAAI/bge-small-en-v1.5 --revision 5c38ec7c405ec4b44b94cc5a9bb96e735b38267a --local-dir C:\models\bge-small-en-v1.5

python verify_downloads.py --models C:\models
