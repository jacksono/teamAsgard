#class LearningMap():
import sys
dict_skills = {}
#print dict_skills
#print dict_skills.keys()
	
def addSkill(skill):
	n = raw_input('Do you want to add another skill?')
	if n == "Yes":
		while True:
			key = raw_input('Enter Your Skill Number')
			value = raw_input('Enter New Skill Learnt')
			dict_skills[key] = value
			print dict_skills
		
if __name__ == "__main__":
	addSkill(sys.argv[1])
	