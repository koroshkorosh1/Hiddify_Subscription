# Convert your configurations to Singbox format easily

def remove_fragment(config):
    # Split the config into individual URLs based on newline characters
    urls = config.splitlines()
    cleaned_urls = []
    for url in urls:
        # Split the URL at '#' and take the part before it
        cleaned_url = url.split('#')[0]
        cleaned_urls.append(cleaned_url)
    return cleaned_urls

# Input configuration as a single string with each URL on a new line
config = 
"""

"""

# Remove fragments
cleaned_urls = remove_fragment(config)

# Print cleaned URLs
for url in cleaned_urls:
    print(url)
