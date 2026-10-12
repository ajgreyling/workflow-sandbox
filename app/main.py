from fastapi import FastAPI

app = FastAPI(title="Workflow Sandbox")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
