# Convert your configurations to Singbox format easily

def remove_fragment_and_number(config):
    # Split the config into individual URLs based on newline characters
    urls = config.splitlines()
    cleaned_urls = []
    counter = 1  # Initialize a counter for numbering
    for url in urls:
        # Split the URL at '#' and take the part before it
        cleaned_url = url.split('#')[0]
        # Append the cleaned URL with the new fragment
        cleaned_urls.append(f"{cleaned_url}#{counter}")
        counter += 1  # Increment the counter for the next URL
    return cleaned_urls

# Input configuration as a single string with each URL on a new line
config = """
"""

# Remove fragments and number them
cleaned_urls = remove_fragment_and_number(config)

# Print cleaned URLs with numbers
for url in cleaned_urls:
    print(url)
