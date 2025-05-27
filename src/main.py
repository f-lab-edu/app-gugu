from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model.app_interface import GeneralResponse, GuguCalculateRequest
from service.gugu import Gugu


def init_app() -> FastAPI:
    app = FastAPI()
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = init_app()


@app.get("/health", response_model=GeneralResponse)
async def health_check() -> GeneralResponse:
    return GeneralResponse(
        status="ok",
        is_error=False,
        result=None,
    )


@app.post("/gugu", response_model=GeneralResponse)
async def gugu(request: GuguCalculateRequest) -> GeneralResponse:
    gugu_svc = Gugu()
    gugu_results = gugu_svc.calculate(request.n)
    display_text = Gugu.get_stringified_results(gugu_results)
    return GeneralResponse(
        status="ok",
        is_error=False,
        result=display_text,
    )
