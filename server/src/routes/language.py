import whisper
import collections

from fastapi import HTTPException, APIRouter

# Create FastAPI router
router = APIRouter(
    tags=["Language"],
)

@router.get("/languages", status_code=200)
async def get_available_languages():
    """
    Return all available languages.
    """
    languages = whisper.tokenizer.LANGUAGES
    languages_sorted = dict(collections.OrderedDict(sorted(languages.items())))
    return languages_sorted


@router.get("/language/{language_code}", status_code=200)
async def get_language(language_code: str):
    """
    Return an english language name.
    """
    languages = whisper.tokenizer.LANGUAGES
    if language_code not in languages:
        raise HTTPException(status_code=404, detail="Language not found")
    return languages[language_code]
