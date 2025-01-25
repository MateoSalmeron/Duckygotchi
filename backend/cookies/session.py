from pydantic import BaseModel
from fastapi import HTTPException, APIRouter, Response, Depends
from uuid import UUID, uuid4

from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters

class sessionData(BaseModel):
    username: str

cookie_params = CookieParameters()

# to the front
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

backend = InMemoryBackend[UUID, sessionData]()

class BasicVerifier(SessionVerifier[UUID, sessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, sessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: sessionData) -> bool:
        # If the session exists, it is valid
        return True


verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)

class SessionVerifications:
    router = APIRouter()

    # app.include_router(verificator.router) en main

    @router.post("/create_session/{name}")
    async def create_session(name: str, response: Response):

        session = uuid4()
        data = sessionData(username=name)

        await backend.create(session, data)
        cookie.attach_to_response(response, session)
        print(f"created session for {name}")

        return f"created session for {name}"

    # whoami muestra el nombre de usuario y el dominio actuales.
    @router.get("/whoami", dependencies=[Depends(cookie)])
    async def whoami(session_data: sessionData = Depends(verifier)):
        print(f"whoami shows session_data: {session_data}")
        return session_data


    @router.post("/delete_session")
    async def del_session(response: Response, session_id: UUID = Depends(cookie)):
        await backend.delete(session_id)
        cookie.delete_from_response(response)
        print(f"delete_session session_id: {session_id}")
        return "deleted session"
    