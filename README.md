# Handoff for the evaluation machine

Temporary repo. Varun deletes it once you have everything.

## 1. Download the models (about 2.2 GB, from Hugging Face)

```powershell
git clone https://github.com/Varun18-hub-dev/practice.git handoff
cd handoff
powershell -ExecutionPolicy Bypass -File .\download_models.ps1
```

It ends with `ALL OK` when every file matches Varun's copies exactly, including the Qwen file's
SHA-256. If it says `SOMETHING DIFFERS`, stop and tell him.

Afterwards `C:\models` contains:
- `qwen2.5-3b-instruct-q4_k_m.gguf`
- `bge-small-en-v1.5\` (with `PIN.json` copied in)

## 2. The dev data

When Varun has pushed `dev_data.zip` here, unzip it into the project:

```powershell
git pull
Expand-Archive dev_data.zip -DestinationPath C:\adaptive_memory\data\longmemeval -Force
```

(`C:\adaptive_memory` is your clone of the project repo, branch `phase2-meaning-based-memory`.)

## 3. Run

Follow `RUN_BENCHMARK.md` in the project repo, from section 1.
