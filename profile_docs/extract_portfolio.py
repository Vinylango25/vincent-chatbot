import requests
from bs4 import BeautifulSoup

# Portfolio URL
url = "https://vinylango25.github.io"

# Get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract visible text
text_elements = soup.find_all(text=True)
visible_text = [t.strip() for t in text_elements if t.strip()]

# Join all text into one string
full_text = "\n".join(visible_text)

# Save to file
with open("portfolio_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("✅ Portfolio text saved to portfolio_text.txt")
