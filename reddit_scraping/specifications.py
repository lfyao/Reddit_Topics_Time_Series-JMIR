# %%
from pathlib import Path
import os

# %%
home_dir = Path("/home/is/leanfranzl-y/Python/")

working_dir = home_dir / f"Data/Working/Reddit_RD/" 
output_dir = home_dir / f"Data/Output/Reddit_RD/reddit_data"

os.makedirs(working_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)
