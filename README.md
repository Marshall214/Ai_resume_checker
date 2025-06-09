Resume Matcher
Resume Matcher is a powerful tool that matches your resume or CV with the job description you're applying for, increasing your chances of getting noticed by Applicant Tracking Systems (ATS) used by most companies. This project uses TF-IDF and Cosine Similarity to intelligently compare your resume and the job description, helping you tailor your resume for a better match.

Features
Resume Parsing: Extracts text from PDF resumes to compare them with job descriptions.

Job Description Matching: Matches the key terms and context between your resume and the job description.

TF-IDF Vectorization: Weighs the importance of words in both the resume and job description.

Cosine Similarity: Measures the similarity between the resume and the job description based on their context.

How It Works
TF-IDF: The resume text and job description are converted into numerical vectors using TF-IDF. This method evaluates the importance of each word in the context of the entire document.

Cosine Similarity: After the vectors are generated, Cosine Similarity is used to calculate how similar the resume is to the job description. This similarity score helps determine how well your resume matches the job requirements.

Result: The tool provides a similarity score, which indicates how closely the resume aligns with the job description.

Technologies Used
Python: The core programming language used for the project.

Streamlit: A web framework to create interactive UIs for the tool.

pdfplumber: Used to extract text from PDF resumes.

scikit-learn: Provides the tools for TF-IDF vectorization and cosine similarity calculation.
