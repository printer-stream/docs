# Task 1 - Complete re-write

We've had a poorly designed process. Now it's time to re-build it completely.

Please, thoroughly plan the action items. Follow the best practices, keep in mind known caveats so we can either reconsider the design or do a workaround with notes.

Look at the README.md in the subdirs.

## Data extraction from PDFs

We need to choose the toolset carefully to be able to provide the best results. Since the data extraction is a single time process, we don't really target minimal resource usage. Although, we can't afford passing each page thru OpenAI's top models. If default GitHub runners is not enough, we can setup an optimally sized VPS for example.

The quality of the produced data must be verified. If this require manual steps, please advice.

The nature of the PDF documents is rather niche. We have ESC/POS language specifications, HPGL language specifications, etc. These documents and knowledge is somewhat not common knowledge, and preserving meaning is crucial. Being able to find the needed term is crucial. Not missing anything during search is crucial.

Should be implemented in docker so we could run it locally or such. 
Keep in `./data-extraction/jpeg` and `./data-extraction/markdown`

## Indexing

Should be implemented in docker so we could run it locally or such. 
Keep in `./data-extraction/search-index` or `./data-extraction/fulltext-search-index` or use a better name for the dir. The idea is to see the difference between the types of index. 

## MCP Server

* Python 3.13
* Thorough logging of each step so we can troubleshoot easier (no prints, only logging)
* Keep app version in version.py
* No emojis, only ascii-compatible characters.
* At first we plan to bake the md, md-bulk, jpegs into the mcp-server image, and serve it from there.
* It's planned to have the search index pre-generated, and baked into the mcp-server image as well.
* We need to have a basic index page to give out more details for clients (search engine robots and any random guests)
* Possibly we also need a swagger-like ui if such thing exists for MCP servers

