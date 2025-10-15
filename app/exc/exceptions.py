from fastapi import HTTPException, status

def raise_bad_request_exception(detail: str = 'Invalid Request!'):
  raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def raise_unauthorized_exception(detail: str = 'Invalid Credentials!'):
  raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=detail,
    headers={'WWW-Authenticate': 'Bearer'},
  )

def raise_forbidden_exception(detail: str = 'Not Authorized!'):
  raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

def raise_not_found_exception(detail: str = 'Resource Not Found!'):
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

def raise_conflict_exception(detail: str = 'Conflict!'):
  raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)

def raise_requests_exception(detail: str = 'Too many requests. Please try again later!'):
  raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=detail)