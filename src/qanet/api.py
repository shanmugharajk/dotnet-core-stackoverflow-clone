from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html
from fastapi.params import Depends
from starlette.responses import JSONResponse
from fastapi.openapi.utils import get_openapi

from qanet.auth.service import set_current_user
from qanet.auth.views import auth_router
from qanet.post_tag.views import authenticated_post_tags_router
from qanet.question.views import questions_router, authenticated_questions_router

# public routes
api_router = APIRouter(default_response_class=JSONResponse)

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(questions_router, prefix="/questions", tags=["questions"])

# authenticated routes
authenticated_api_router = APIRouter(default_response_class=JSONResponse)

authenticated_api_router.include_router(
    authenticated_post_tags_router, prefix="/tags", tags=["tags"]
)
authenticated_api_router.include_router(
    authenticated_questions_router, prefix="/questions", tags=["questions"]
)

# doc routes
doc_router = APIRouter()


@doc_router.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(
        get_openapi(
            title="Qanet Docs", servers=[{"url": "/api/v1"}], version=1, routes=api_router.routes
        )
    )


@doc_router.get("/", include_in_schema=False)
async def get_documentation():
    return get_redoc_html(openapi_url="/api/v1/docs/openapi.json", title="Qanet Docs")


api_router.include_router(doc_router, prefix="/docs")


@api_router.get("/healthcheck", include_in_schema=False)
def healthcheck():
    return {"status": "ok"}


# aggregating authenticated routes into api_router to make all routes available
# via '/api/v1' with only 'authenticated_api_router' will be checked for JWT.
api_router.include_router(authenticated_api_router, dependencies=[Depends(set_current_user)])