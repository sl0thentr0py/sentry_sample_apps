#!/usr/bin/env python3
"""
Minimal reproduction case for Sentry isolation_scope + async generator bug.

Bug: Using sentry_sdk.isolation_scope() as a context manager around an async
generator that yields causes "Token was created in a different Context" error
when the generator exits early (via break, exception, or garbage collection).
"""

import asyncio
import sentry_sdk
from sentry_sdk.integrations.asyncio import AsyncioIntegration


sentry_sdk.init(
    dsn=None,  # No DSN needed to reproduce
    integrations=[AsyncioIntegration()],
    # debug=True,
)


async def inner_generator():
    """Simple async generator that yields values"""
    for i in range(3):
        print(f"  Inner generator yielding: {i}")
        yield i


async def problematic_async_generator():
    """
    This pattern causes the context error.
    The isolation_scope wraps yield statements in an async generator.
    """
    with sentry_sdk.isolation_scope() as scope:
        scope.set_user({"id": "test-user-123"})
        scope.set_tag("example", "value")

        async for value in inner_generator():
            # THIS YIELD INSIDE ISOLATION_SCOPE IS THE PROBLEM
            yield value


async def main():
    async for val in problematic_async_generator():
        print(f"Received: {val}")
        if val == 1:
            print("Breaking early...")
            break  # This causes the context error

    # Give time for error to appear in output
    await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(main())
