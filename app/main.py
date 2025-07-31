import uvicorn

from core.config import settings
from create_fastapi_app import create_app

main_app = create_app(
    create_custom_static_urls=True,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
