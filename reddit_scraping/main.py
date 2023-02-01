# %%
from specifications import *
from functions import *


# %%
# subreddit = 'CysticFibrosis'
print(f'Scraping data from the subreddit {subreddit}')
filename = output_dir / f'{subreddit}_comments.json.gz'
downloadFromUrl(filename, subreddit, endpoint='comment')
filename = output_dir / f'{subreddit}_submissions.json.gz'
downloadFromUrl(filename, subreddit, endpoint='submission')