import openai, numpy as np

response = openai.embeddings.create(
    input=["cat friends say", "woof"], 
    model="text-embedding-3-small",
)

embedding_a = response.data[0].embedding
embedding_b = response.data[1].embedding

similarity_score = np.dot(embedding_a, embedding_b)
print(similarity_score)
