import sys
import importlib

try:
    import browser_use
    print(f"Successfully imported browser_use")
    print(f"Version: {getattr(browser_use, '__version__', 'Unknown')}")
    print(f"Location: {browser_use.__file__}")
    
    # Try to import specific modules
    from browser_use import Agent
    print("Successfully imported Agent class")
    
    from browser_use import Browser
    print("Successfully imported Browser class")
    
except ImportError as e:
    print(f"Error importing browser_use: {e}")

print("\nPython version:")
print(sys.version)
print("\nPython path:")
for path in sys.path:
    print(f"- {path}")
