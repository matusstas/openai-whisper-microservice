from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.model import router as Model
from src.routes.language import router as Language
from src.routes.miscellaneous import router as Miscellaneous

# # Add openAPI tags to Swagger
# openapi_tags = [
#     {
#         "name": "Post",
#         "description": "Endpoints are responsible for post operations.",
#     },
# ]

# Create FastAPI app
app = FastAPI(
    title="Server",
    # openapi_tags=openapi_tags,
)

# Add Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router
app.include_router(Model)
app.include_router(Language)
app.include_router(Miscellaneous)


@app.get("/", status_code=200, tags=["Root"])
async def root():
    """
    Return message from container to check if it is running.
    """
    return {"detail":"Container is running"}

# torch==2.0.0+cu117