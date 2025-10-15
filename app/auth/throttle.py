import time
from collections import defaultdict
from exc.exceptions import raise_requests_exception

# Authenticated users constants
AUTH_RATE_LIMIT = 5
AUTH_TIME_WINDOW_SECONDS = 60

# Unauthenticated 'global' users constants
GLOBAL_RATE_LIMIT = 3
GLOBAL_TIME_WINDOW_SECONDS = 60

# In-memory storage for user requests
user_requests = defaultdict(list)

# Throttling dependency
def apply_rate_limit(user_id: str):
  current_time = time.time()

  if user_id == 'global_unauthenticated_user':
    rate_limit = GLOBAL_RATE_LIMIT
    time_window = GLOBAL_TIME_WINDOW_SECONDS
  else:
    rate_limit = AUTH_RATE_LIMIT
    time_window = AUTH_TIME_WINDOW_SECONDS

  # Filter out requests older than time window
  user_requests[user_id] = [
    t for t in user_requests[user_id] if t > current_time - time_window
  ]

  if len(user_requests[user_id]) >= rate_limit:
    raise_requests_exception()
  else:
    current_usage = len(user_requests[user_id])
    print(f'User {user_id}: {current_usage + 1}/{rate_limit} Requests Used!')

  user_requests[user_id].append(current_time)
  return True