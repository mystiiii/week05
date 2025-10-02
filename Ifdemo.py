subj1Grade = int(input("Enter Grade for Subject 1: "))
subj2Grade = int(input("Enter Grade for Subject 2: "))
subj3Grade = int(input("Enter Grade for Subject 3: "))
subj4Grade = int(input("Enter Grade for Subject 4: "))
subj5Grade = int(input("Enter Grade for Subject 5: "))

averageGrade = (subj1Grade + subj2Grade + subj3Grade + subj4Grade + subj5Grade) / 5

print(f"Your Average is {averageGrade}")

if averageGrade > 70:
    print("You Passed")
else:
    print("You Failed")