import time
from functools import wraps

def throttle(delay):
    """
    Throttle decorator that limits function execution to once per delay period.
    
    Args:
        delay (float): Time in seconds between allowed function calls
    """
    def decorator(func):
        last_called = [0]  # Using list to make it mutable in closure
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called[0] >= delay:
                last_called[0] = current_time
                return func(*args, **kwargs)
            else:
                print(f"Function {func.__name__} throttled - called too frequently")
                return None
        return wrapper
    return decorator

# Example usage with API calls
@throttle(2.0)  # Allow only one call per 2 seconds
def api_call(endpoint):
    print(f"Making API call to: {endpoint}")
    time.sleep(0.1)  # Simulate API processing time
    return f"Response from {endpoint}"

@throttle(1.0)  # Allow only one call per second
def search_api(query):
    print(f"Searching for: {query}")
    time.sleep(0.1)  # Simulate search processing
    return f"Search results for: {query}"

@throttle(3.0)  # Allow only one call per 3 seconds
def user_profile_api(user_id):
    print(f"Fetching profile for user: {user_id}")
    time.sleep(0.1)  # Simulate database query
    return f"Profile data for user: {user_id}"

# Test cases for API throttling
def test_api_throttling():
    print("Testing API Call Throttling:")
    print("=" * 50)
    
    # Test 1: Multiple rapid API calls
    print("\nTest 1: Multiple rapid API calls (should throttle):")
    for i in range(5):
        result = api_call(f"/api/users/{i}")
        if result:
            print(f"✓ {result}")
        else:
            print(f"✗ Call {i+1} throttled")
        time.sleep(0.5)  # Wait 0.5 seconds between calls
    
    # Test 2: Search API with different queries
    print("\nTest 2: Search API calls (should throttle):")
    queries = ["python", "javascript", "react", "node.js", "django"]
    for query in queries:
        result = search_api(query)
        if result:
            print(f"✓ {result}")
        else:
            print(f"✗ Search for '{query}' throttled")
        time.sleep(0.3)  # Wait 0.3 seconds between calls
    
    # Test 3: User profile API with longer throttle
    print("\nTest 3: User profile API calls (3-second throttle):")
    user_ids = [1001, 1002, 1003, 1004, 1005]
    for user_id in user_ids:
        result = user_profile_api(user_id)
        if result:
            print(f"✓ {result}")
        else:
            print(f"✗ Profile fetch for user {user_id} throttled")
        time.sleep(1.0)  # Wait 1 second between calls

# Alternative implementation using a class
class ThrottleFunction:
    def __init__(self, func, delay):
        self.func = func
        self.delay = delay
        self.last_called = 0
    
    def __call__(self, *args, **kwargs):
        current_time = time.time()
        if current_time - self.last_called >= self.delay:
            self.last_called = current_time
            return self.func(*args, **kwargs)
        else:
            print(f"Function {self.func.__name__} throttled")
            return None

# Test class-based throttle
def test_class_based_throttle():
    print("\nTesting Class-based Throttle:")
    print("=" * 50)
    
    def payment_api(amount):
        print(f"Processing payment: ${amount}")
        time.sleep(0.1)
        return f"Payment processed: ${amount}"
    
    # Create throttled version
    throttled_payment = ThrottleFunction(payment_api, 1.5)  # 1.5 seconds between calls
    
    # Test multiple payment calls
    amounts = [10, 25, 50, 100, 200]
    for amount in amounts:
        result = throttled_payment(amount)
        if result:
            print(f"✓ {result}")
        else:
            print(f"✗ Payment of ${amount} throttled")
        time.sleep(0.4)  # Wait 0.4 seconds between calls

if __name__ == "__main__":
    print("🚀 Starting Throttle Function Tests")
    print("=" * 60)
    
    # Run all test cases
    test_api_throttling()
    test_class_based_throttle()
    
    print("\n" + "=" * 60)
    print("✅ All throttle tests completed!")
    print("\nKey Observations:")
    print("- API calls are throttled based on their delay settings")
    print("- Only the first call in each throttle period is executed")
    print("- Subsequent calls within the throttle period are blocked")
    print("- Different functions can have different throttle delays")
