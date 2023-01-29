import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_description = docx2txt.process('C:\\Users\\hp\\Desktop\\moKer\\jobdescription.docx')
resume = docx2txt.process('C:\\Users\\hp\\Desktop\\moKer\\Resume3.docx')
# print(resume)

content = [job_description, resume]
cv = CountVectorizer()
matrix = cv.fit_transform(content)
similarity_matrix = cosine_similarity(matrix)
# print(similarity_matrix)

print(' The % is : '+ str(similarity_matrix[1][0]*100)+ '%')