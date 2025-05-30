# Test if all the required modules can be imported
print("Testing imports...")

try:
    from browser_use import Agent
    print("✓ Successfully imported browser_use.Agent")
except ImportError as e:
    print(f"✗ Failed to import browser_use.Agent: {e}")

try:
    from langchain_openai import ChatOpenAI
    print("✓ Successfully imported langchain_openai.ChatOpenAI")
except ImportError as e:
    print(f"✗ Failed to import langchain_openai.ChatOpenAI: {e}")

try:
    import playwright
    print(f"✓ Successfully imported playwright {playwright.__version__}")
except ImportError as e:
    print(f"✗ Failed to import playwright: {e}")

print("Import test complete.")
