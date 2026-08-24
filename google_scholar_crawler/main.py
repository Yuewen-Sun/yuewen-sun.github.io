from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

# author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
author: dict = scholarly.search_author_id('LboR1toAAAAJ')
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
# always write next to this script, no matter where it is invoked from
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)
with open(os.path.join(RESULTS_DIR, 'gs_data.json'), 'w', encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(os.path.join(RESULTS_DIR, 'gs_data_shieldsio.json'), 'w', encoding="utf-8") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
