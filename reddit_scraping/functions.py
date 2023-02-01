# %%
import requests
from datetime import datetime
import traceback
import time
import json
import gzip

# %%
def downloadFromUrl(filename, subreddit, endpoint='comment'):
	url = "https://api.pushshift.io/reddit/{}/search/?limit=1000&sort=desc&subreddit={}&before="
	start_time = datetime.utcnow()

	print(f"saving {endpoint} to {filename}")
	count = 0

	previous_epoch = int(start_time.timestamp())

	with gzip.open(filename, 'w') as f:
		while True:
			new_url = url.format(endpoint, subreddit) + str(previous_epoch)
			json_text = requests.get(new_url, headers={'User-Agent': "comment collector by lean.yao"})
			time.sleep(1)

			try:
				json_data = json_text.json()
			except json.decoder.JSONDecodeError:
				time.sleep(1)
				continue
			
			if 'data' not in json_data:
				break

			comments = json_data['data']
			if len(comments)==0:
				break

			previous_epoch = comments[-1]['created_utc'] - 1 # move back one second from last comment
			for comment in comments:
				count+=1
				try:
					jsonString = json.dumps(comment)
					jsonString = jsonString + '\n'
					f.write(jsonString.encode("utf-8"))

				except Exception as err:
					print(f"Couldn't print {endpoint}: https://www.reddit.com{object['permalink']}")
					print(traceback.format_exc())
					
			print("Saved {} {}s through {}".format(count, endpoint, datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))

	print(f"Saved {count} {endpoint}")
	# handle.close()

