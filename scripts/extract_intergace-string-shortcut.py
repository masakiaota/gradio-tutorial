# %% 
import re

# File reading
with open("docs.txt", "r") as file:
    txt = file.read()

# %%
# Extracting the block
matches = re.findall(
    r"Interface String Shortcut(.*?)Methods", txt, re.DOTALL
)

if matches:
    for i, match in enumerate(matches, 1):
        print(f"Match {i}:")
        print(match)
        print('-' * 50)
else:
    print("No matches found in the text.")

# %%
