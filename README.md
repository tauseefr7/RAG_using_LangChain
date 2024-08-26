## RAG project using LangChain

## Install dependencies

Install the dependencies found in `requirements.txt
```python
pip install -r requirements.txt
```

## Create database

Create the Chroma DB.

```python
python create_database.py
```

## Query the database

```python
python query_data.py "What does the Descartes say about scientific research?"
```

Example Output for when querying the data with "What does the Descartes say about scientific research?":

Database initialised.

Search Results: [(Document(metadata={'source': 'data\\books\\Discourse on the Method.md', 'start_index': 102467}, page_content='I remarked, moreover, with respect to experiments, that they become always more necessary the more one is advanced in knowledge; for, at the commencement, it is better to make use only of what is spontaneously presented to our senses, and of which we cannot remain ignorant, provided we bestow on it'), 0.795516177226544), (Document(metadata={'source': 'data\\books\\Discourse on the Method.md', 'start_index': 0}, page_content='Title: Discourse on the Method\n\nAuthor: Rene Descartes\n\nYear: 1637\n\nPREFATORY NOTE BY THE AUTHOR'), 0.7783615458722156), (Document(metadata={'source': 'data\\books\\Discourse on the Method.md', 'start_index': 53010}, page_content='After this I inquired in general into what is essential to the truth and certainty of a proposition; for since I had discovered one which I knew to be true, I thought that I must likewise be able to discover the ground of this certitude. And as I observed that in the words I think, therefore I am,'), 0.7636524221824591)]

Generated Prompt:
Human:
Answer the question based only on the following context:

I remarked, moreover, with respect to experiments, that they become always more necessary the more one is advanced in knowledge; for, at the commencement, it is better to make use only of what is spontaneously presented to our senses, and of which we cannot remain ignorant, provided we bestow on it

---

Title: Discourse on the Method

Author: Rene Descartes

Year: 1637

PREFATORY NOTE BY THE AUTHOR

---

After this I inquired in general into what is essential to the truth and certainty of a proposition; for since I had discovered one which I knew to be true, I thought that I must likewise be able to discover the ground of this certitude. And as I observed that in the words I think, therefore I am,

---

Answer the question based on the above context: What does the Descartes say about scientific research?

Response: content='Descartes emphasizes the importance of experiments in scientific research, stating that they become more necessary as one advances in knowledge. He suggests that at the beginning of a scientific inquiry, it is best to rely on what is directly observable through the senses, but as one progresses, experiments become crucial for further understanding and certainty.' response_metadata={'token_usage': {'completion_tokens': 63, 'prompt_tokens': 198, 'total_tokens': 261}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-4a80baab-509c-489c-94a4-4191a3ded140-0' usage_metadata={'input_tokens': 198, 'output_tokens': 63, 'total_tokens': 261}