import time
from fastapi import HTTPException
from functools import wraps


def rate_limit(max_calls: int, time_frame: int):
    def decorator(func):
        calls = []

        @wraps(func)
        async def wrapper(*args, **kwargs):
            now = time.time()
            calls_in_time_frame = [call for call in calls if call > now - time_frame]
            if len(calls_in_time_frame) >= max_calls:
                raise HTTPException(status_code=429, detail="Rate limit exceeded")
            calls.append(now)
            return await func(*args, **kwargs)

        return wrapper

    return decorator
