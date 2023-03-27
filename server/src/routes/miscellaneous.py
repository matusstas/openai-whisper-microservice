import torch

from fastapi import APIRouter

# Create FastAPI router
router = APIRouter(
    tags=["Miscellaneous"],
)

@router.get("/cuda", status_code=200)
async def check_cuda():
    """
    Check whether a GPU with CUDA support is available on the current system. Return boolean value.
    """
    result = torch.cuda.is_available()
    return result
