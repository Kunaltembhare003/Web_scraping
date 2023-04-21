# Web Scraping

We will retrieve allelic frequency data for Indian population using Selenium and BeautifulSoup from the following website: <a href="http://www.allelefrequencies.net/pop6001b.asp?pop_polyreg=HLA&pop_type_data=&pop_geog_region=South+Asia">Allele Frequency Net Database</a>

## Data Retrieval Steps
To retrieve the data, we will follow these three steps:

1. Retrieve all the links from table 2 where Indian population data is given.
1. For each retrieved link, go to the next page and extract another link.
1. Retrieve all the data given in table format.
