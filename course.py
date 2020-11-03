

def create_outline():
    """
    TODO: implement your code here
    """
    topics = (["Introduction to Python" , "Tools of the Trade" , "How to make decisions" , "How to repeat code" , "How to structure data", "Functions", "Modules"])
    problems = "Problem 1, Problem 2, Problem 3"
    print("Course Topics:")
    topics.sort()
    for i in topics:
        print("*", i)
    
    p = {}
    for x in topics:
        p[x] = problems 
    print("Problems:")
    for i, j in p.items():
        print("*", i, ":", j)

    print("Student Progress:")
    a = "1", "Felicia", "Introduction to Python", "Problem 1 [STARTED]"
    b = "2", "John", "How to make decisions", "Problem 3 [GRADED]"
    c = "3", "Adam", "How to repeat code", "Problem 2[COMPLETED]"

    (number, name, topic, problem)=a
    print(number+ ".", name, "-", topic, "-", problem)
    (number, name, topic, problem)=b
    print(number+".", name, "-", topic, "-", problem)
    (number, name, topic, problem)=c
    print(number+".", name, "-", topic, "-", problem)

    pass


if __name__ == "__main__":
    create_outline()
