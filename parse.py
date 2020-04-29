import requests
import xml.etree.ElementTree as ET
import pandas as pd

url_file = "https://www.denvergov.org/media/gis/DataCatalog/site_development_plans/metadata/site_development_plans.xml"
xml_file = requests.get(url_file).content

def xml2df(xml_file):
    root = ET.XML(xml_file)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

df = xml2df(xml_file)
df.shape
df.head()

print(df)