# My thoughts on Neum

## Documentation
* [+] Main uses cases and examples in the landing page are well structured and well documented. 
* [--] Once you start exploring the APIs and documentation more it starts to become harder to follow and most of the blocks under ["Supported Blocks"](https://docs.tryneum.com/docs/blocks#supported-blocks) lack good documentation. They seem very intersting but I need more concrete examples on how to set them up and how they can be used in a workflow. I'm thinking [this](https://docs.tryneum.com/docs/qa-with-a-document) level of detail but for each block would be ideal.
* [-] Very minimal but... the JSON in some examples[[1]](https://docs.tryneum.com/docs/qa-with-a-document)[[2]](https://docs.tryneum.com/docs/qa-with-a-document) is not properly formatted and this can bring a bad experience for developers who are trying to get started quickly and are simply copy pasting the examples you give
* [++] The integrated tooltip que tienen en estas paginas [[1]](https://docs.tryneum.com/reference/run-workflow)[[2]](https://docs.tryneum.com/reference/create-workflow)esta increible. Idk if that is out of the box or what but being able to generate the starter code for various languages is really cool. 
    * If at some point you guys create wrapper libraries for Neum fuera bien cool si ese widget tambien pudiera dar ejemplos de como correr los workflows etc con el wrapper o con raw http requests.
* [--] For a fair amount of your examples specifically when there is a "Request"/"Response" section, the request body and the response body don't go together/don't make sense. This can be very confusing for your users and can be off putting. Ex: https://docs.tryneum.com/reference/create-workflow 
    * Obvio entiendo que estan un "beta testing" phase y getting features out y likely a lot more important than making sure there are no mistakes in your docs pero I thought I would point it out anyways. Al final del dia aunque sea un beta test entre amigos the website is publicly hosted and there is nothing stopping people from actually stumbling across your product.
* [++] In total I made around 10-15 API calls across both endpoints and never had a availability issue. Responses always came as expected and latency was never too crazy.
    * [-] When first trying to run workflows I thought that the session_id parameter was optional and so I was getting back some BAD_REQUEST responses. It would've been real nice to have a bit more context added to error responses in order to help the users better understand what they are doing wrong (or maybe you already have this and I'm just a dumb dumb).

## Actually using Neum
### Summarize Latest News Workflow
General gist of this workflow is to use the query serp block and configure the model to think that it is a news anchor. Then chain the query serp block with a summarize text one. Once the workflow is up I'll try to hook up the workflow with a simple CLI that asks you what news you want to learn about and provides you a sumamry of the latest news.

* Seems like the query_serp block only returns the first snippet of the serp result. It'd be really nice if it came back with the full result so that the chaining with summarize_text actually has a chance to summarize various results into a concise response.
* [news_summary_workflow.py](https://github.com/gugibugy/try_neum/blob/main/news_summary_workflow.py) has my initial attempt at creating a workflow that achieves the idea above. Running the workflow works and seems to do what I asked to but the result of the query_serp block is too restrictive (see point above) and so the summarize_text block can't shine since the text that it is summarizing is too small.

### Chat bot con las reglas de Truco
Title is pretty self explanatory, make a workflow using query_doc that has the truco rule book as the data_source and that users can query for questions about the rules. In an ideal world Mau me da el repo de https://truco.fly.dev/ y puedo hacer un pull request para usar el workflow para responder preguntas de las reglas.

## Ideas
### Parallel Blocks
Main idea behind this is being able to have blocks that run multiple operations in parallel before feeding the result into the next block in the sequence. Simple example of this would be having mulitple query_doc blocks run together before I pass the results into a sumamrize_text block. Or many I want to search for various things using the query_serp block and I want to have all those results joined before passing it into a summarize_text block. I think having blocks that can do various actions in parallel before moving on would enable users to create much more complex and useful workflows.

### Drag-n-Drop GUI for Workflow Creation
This is clearly low in the priority given that it is a quality of life improvement and not really a infrastructure/bug/feature request buuuuut it would be really cool if there was a GUI that you could use to drag and drop blocks in order to create your workflows.

### Workflow Variables
Idea behind this is being able to create your workflow using generic variables so that you can use one workflow for various different applications. Simple example would be to be able to create a workflow in which the "data_source" field of my query_doc block is a variable. Then when the time comes to run my workflow I can pass in a value for this data_source variable and not have to make the same workflow for every data source that I might have.