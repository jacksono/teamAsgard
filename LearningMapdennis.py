class LearningMap():
    dict_skills = {}
    print dict_skills
    #print dict_skills.keys()

    def addSkill(self, skill):
        key = raw_input('Enter Your Skill Number')
        value = raw_input('Enter New Skill Learnt')
        dict_skills[key] = value

    def view_skills(self):
        skill_list=[]
        for skill in dict_skills.keys():
            skill_list.append(skill)
        return skill_list
