Steps
1. pip install virtualenv
2. cd extract_data/
3. virtualenv venv
4. source venv/bin/activate
5. pip install requirements.txt
scrapy crawl television -o data/television.csv -t csv