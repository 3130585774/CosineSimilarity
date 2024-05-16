import math

import jieba


# Define a function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    sum, sq1, sq2 = 0, 0, 0
    for i in range(len(vec1)):
        sum += vec1[i] * vec2[i]
        sq1 += pow(vec1[i], 2)
        sq2 += pow(vec2[i], 2)

    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 10)
    except ZeroDivisionError:
        result = 0.0
    return result


# Define a function to convert text into vector representation using bag-of-words model
def text_to_vector(word_dict, text):
    text_cut_code = [0] * len(word_dict)
    for word in text:
        text_cut_code[word_dict[word]] += 1
    return text_cut_code


def text_to_word_dict(text2_cut, text1_cut):
    word_set = set(text2_cut).union(set(text1_cut))
    _word_dict = dict()
    i = 0
    for word in word_set:
        _word_dict[word] = i
        i += 1
    return _word_dict


def word_cut(text):
    return [i for i in jieba.cut(text, cut_all=True) if i != '']


# Define two texts
text1 = "This is text one."
text2 = "This is text two."

# Convert texts into vector representation
text1_cut = word_cut(text1)
text2_cut = word_cut(text2)

word_dict = text_to_word_dict(text1_cut, text2_cut)
vector1 = text_to_vector(word_dict, text1_cut)
vector2 = text_to_vector(word_dict, text2_cut)

# Calculate cosine similarity
similarity = cosine_similarity(vector1, vector2)
print("Cosine Similarity:", similarity)
