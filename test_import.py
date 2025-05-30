import browser_use
from browser_use import Agent, Browser

# Print version information
print(f"Browser-use version: {browser_use.__version__}")
print("Successfully imported browser-use components!")

# List available methods of the Agent class
print("\nAgent class methods:")
for method_name in dir(Agent):
    if not method_name.startswith("_"):
        print(f"- {method_name}")

# List available methods of the Browser class
print("\nBrowser class methods:")
for method_name in dir(Browser):
    if not method_name.startswith("_"):
        print(f"- {method_name}")

print("\nInstallation test complete!")
