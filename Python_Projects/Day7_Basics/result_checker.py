def result_checker(marks):
    if marks >= 40:
        print ("Pass")

    else:
        print("Fail")

mark = int(input("Tell me your marks: "))
result_checker(mark)