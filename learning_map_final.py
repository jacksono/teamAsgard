dict_skills = {}
def run():
    x = True
    
    while True:
        ui()
def ui():
    n = input('What do you want to do? Select "a" to add or "b" to view: ')
    if n == "a":
        k = input('Do You want to add a new skill or add a studied skill?Select "a" to add new or "b" to add studied skill: ')
        if k == "a":
            new_skill = input('Add your new skill:')
            dict_skills[new_skill] = 0
            ui()
                
        elif k == "b":
            studied_skill = input("Add a studied skill:")
            dict_skills[studied_skill]=1
            ui()
        
        else:
            print("Invalid Selection")
    elif n == "b":
        l = input('Select "a" to view all skills, "b" to view studied skills, "c" to view unstudied skills or "d" to view progress: ')
        if l == "a":
            print("View All Skills: ")
            skill_list=[]
            for skill in dict_skills.keys():
                skill_list.append(skill)
            print(skill_list)
            
        elif l == "b":
            print("View Studied Skills: ")
            skills_list2 = []
            for skill, value in dict_skills.items():
                if value == 1:
                    skills_list2.append(skill)
            print(skills_list2)
            
        elif l == "c":
            print("View Unstudied Skills: ")

            skills_list3 = []
            for skill, value in dict_skills.items():
                if value == 0:
                    skills_list3.append(skill)
            print(skills_list3)
        elif l == "d":
            print("View Progress: ")
            total = len(dict_skills)
            studied_no = 0
            for val in dict_skills.values():
                if val == 1:
                    studied_no += 1
            if total > 0: 
                progress = (studied_no / total) * 100
                print("Your current progress is {} %".format(progress))
            else:
                print("No skills set")
        
        else:
            print("Invalid Selection")
    else:
        print("Invalid Selection")
if __name__ == "__main__":
    run()

