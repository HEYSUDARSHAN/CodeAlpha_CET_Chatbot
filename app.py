import nltk
from nltk.tokenize import word_tokenize

# Uncomment if running for the first time:
nltk.download('punkt')

def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()
    tokens = word_tokenize(user_input_lower)
    
    # Match queries based on keywords in the user's input
    if "what" in tokens and "mht-cet" in tokens:
        return ("MHT-CET is a state-level entrance exam conducted by the State Common Entrance Test Cell, "
                "Maharashtra, for admission to undergraduate engineering, pharmacy, and agriculture courses in "
                "institutions across Maharashtra.")
    
    elif "eligibility" in user_input_lower:
        return ("Candidates must have passed or be appearing for their class 12 (HSC) exam with Physics, "
                "Chemistry, and Mathematics (for engineering) or Biology (for pharmacy). Candidates must be Indian "
                "citizens and meet specific domicile requirements for admission to state quota seats.")
    
    elif "mode" in user_input_lower:
        return ("MHT-CET is a computer-based test (CBT). It consists of multiple-choice questions (MCQs) in Physics, "
                "Chemistry, and Mathematics (for engineering aspirants) or Biology (for pharmacy aspirants).")
    
    elif "syllabus" in user_input_lower:
        return ("The syllabus includes Physics, Chemistry, and Mathematics/Biology topics from the Maharashtra State "
                "Board curriculum of class 11 and 12. Approximately 20% of the questions are based on class 11 topics, "
                "and 80% on class 12 topics.")
    
    elif "structure" in user_input_lower or "exam structured" in user_input_lower:
        return ("The exam has two papers:\n\n"
                "• Paper 1: Physics and Chemistry (100 marks each)\n\n"
                "• Paper 2: Mathematics (for engineering, 100 marks) or Biology (for pharmacy, 100 marks for both Botany and Zoology).\n\n"
                "Each correct answer earns 1 mark in Physics, Chemistry, and Biology, and 2 marks in Mathematics. There is no negative marking.")
    
    elif "appear" in user_input_lower or "attempt" in user_input_lower:
        return ("There is no limit on the number of attempts for MHT-CET, as long as the candidate meets the eligibility "
                "criteria regarding age and educational qualifications.")
    
    elif "when" in user_input_lower or "held" in user_input_lower:
        return ("MHT-CET is typically conducted in the months of April to May each year. The exact dates are announced by "
                "the State CET Cell on their official website.")
    
    elif "reservation" in user_input_lower and "female" not in user_input_lower:
        return ("Yes, there are reservations for various categories such as SC, ST, OBC, and others as per Maharashtra state "
                "government norms. Candidates must provide valid category certificates at the time of admission.")
    
    elif "different" in user_input_lower or ("jee" in user_input_lower and "mht-cet" in user_input_lower):
        return ("MHT-CET is a state-level exam specifically for institutions in Maharashtra, while JEE Main is a national-level exam "
                "for NITs, IIITs, and centrally funded institutions across India. The syllabus for both exams is somewhat similar, but "
                "MHT-CET focuses more on the Maharashtra state board syllabus.")
    
    elif "application" in user_input_lower:
        return ("The application process is online. Candidates must fill in personal, academic, and communication details, upload "
                "necessary documents, and pay the application fee via the official MHT-CET website.")
    
    elif "cut-off" in user_input_lower or "cutoff" in user_input_lower:
        return ("The cut-off varies every year based on factors like the difficulty level of the exam, number of candidates, and "
                "availability of seats. Generally, higher-ranking institutions have higher cut-offs, especially for competitive branches "
                "like Computer Science and Mechanical Engineering.")
    
    elif "rank" in user_input_lower:
        return ("The rank is based on the marks scored in the exam, with no negative marking. Normalization techniques are used "
                "in case of multiple shifts to ensure fairness.")
    
    elif "outside" in user_input_lower:
        return ("Yes, but only candidates with a valid domicile of Maharashtra are eligible for state quota seats. Non-domicile "
                "candidates can apply for private and management quota seats.")
    
    elif "validity" in user_input_lower or "score valid" in user_input_lower:
        return ("The MHT-CET score is valid for one year, meaning it is applicable only for the academic year in which the candidate "
                "has appeared.")
    
    elif "female" in user_input_lower:
        return ("Yes, there is a reservation for female candidates in various courses, as per Maharashtra government policies.")
    
    else:
        return ("I'm sorry, I didn't understand that. Could you please rephrase your question regarding MHT-CET?")

def main():
    print("Welcome to the MHT-CET FAQ Chatbot! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Thank you for using the MHT-CET FAQ Chatbot. Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
