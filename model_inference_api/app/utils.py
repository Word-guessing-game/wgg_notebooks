import torch
from scipy.spatial.distance import cosine
from sklearn.decomposition import PCA
from transformers import BertModel, BertTokenizer


def get_word_dict():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertModel.from_pretrained(
        "bert-base-uncased",
        output_hidden_states=True,  # Whether the model returns all hidden-states.
    )
    model.eval()

    word_embeddings = model.embeddings.word_embeddings.weight
    pca = PCA(n_components=15, random_state=42)
    emb_15d = pca.fit_transform(word_embeddings.detach().numpy())
    word_dict = dict(zip(tokenizer.vocab.keys(), emb_15d))

    return word_dict


def get_word_list_json(example_word, word_dict):
    distance_dict = {}
    for key in word_dict.keys():
        distance_dict[key] = 1 - cosine(word_dict[key], word_dict[example_word])

    sorted_distance_tuple = sorted(
        distance_dict.items(), key=lambda x: x[1], reverse=True
    )

    result_dict = []
    ind_num = 0
    for i in sorted_distance_tuple:
        if len(i[0]) > 2 and i[0][0].isalpha():
            result_dict.append({"word": i[0], "position": ind_num})
            ind_num += 1

    return result_dict
