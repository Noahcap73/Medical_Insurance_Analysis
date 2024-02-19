import csv

rows = []
ages = []
sexs = []
bmis = []
children = []
smokers = []
regions = []
insurance_costs = []

#Converting CSV file data into list data
with open("insurance.csv", "r" ) as csvFile:
    csvData = csv.reader(csvFile)

    fields = next(csvData)
    for row in csvData:
        rows.append(row)
        ages.append(row[0])
        sexs.append(row[1])
        bmis.append(row[2])
        children.append(row[3])
        smokers.append(row[4])
        regions.append(row[5])
        insurance_costs.append(row[6])

    


#printing the fields of the data
print("The fields of this data are: " + ", ".join(field for field in fields) + ".")
print(" ")


from matplotlib import pyplot as plt

#Creating an average function
def getAvgInsurance(insuranceList):
   return sum(insuranceList) / len(insuranceList)
 
#ANALYZING AGES
#Finding the Average Price of Insurance for young, middle, and old age groups
youngerGroup = []
middleGroup = []
olderGroup = []
for person in rows:
   if int(person[0]) < 26:
    youngerGroup.append(float(person[6]))
   elif int(person[0]) >= 26 and int(person[0]) < 43:
      middleGroup.append(float(person[6])) 
   elif int(person[0]) >= 43:
      olderGroup.append(float(person[6]))

avgYoungInsurance = getAvgInsurance(youngerGroup) 
print(f"The average younger age group insurance cost = ${avgYoungInsurance}")

avgMiddleInsurance = getAvgInsurance(middleGroup) 
print(f"The average middle age group insurance cost = ${avgMiddleInsurance}")

avgOlderInsurance = getAvgInsurance(olderGroup) 
print(f"The average older age group insurance cost = ${avgOlderInsurance}") 
print(" ")


groups = ["18 - 25", "26 - 42", "43+"]
insurance_group_costs = [avgYoungInsurance, avgMiddleInsurance, avgOlderInsurance]


bars_age_insurance = plt.bar(groups, insurance_group_costs)
bars_age_insurance[0].set_color("#ED93BB")
bars_age_insurance[1].set_color("#6741FF")
bars_age_insurance[2].set_color("#4B2840")
plt.xlabel("Age Groups")
plt.ylabel("Average Insurance Costs $")
plt.show()



#ANALYZING SEX OR GENDER
#Finding the average price of insurance for males and females
males = []
females = []
for sex in rows:
   if sex[1] == "male":
      males.append(float(sex[6]))
   elif sex[1] == "female":
      females.append(float(sex[6]))
   
avgMaleInsurance = getAvgInsurance(males)
print(f"The average male insurance = ${avgMaleInsurance}")

avgFemaleInsurance = getAvgInsurance(females)
print(f"The average female insurance = ${avgFemaleInsurance}")
print(" ")

genders = ["Males", "Females"]
insurance_sex_costs = [avgMaleInsurance, avgFemaleInsurance]

'''bars_sex_insurance = plt.bar(genders, insurance_sex_costs)
bars_sex_insurance[0].set_color("#3F88C5")
bars_sex_insurance[1].set_color("#E867D0")
plt.xlabel("Gender")
plt.ylabel("Insurance Cost $")
plt.show()
'''


#ANALYZING BMIS
#Finding the average price of insurance for healthy, overweight, and obese bmis
healthyBmis = []
overweightBmis = []
obeseBmis = []
for bmi in rows:
   if float(bmi[2]) >= 18 and float(bmi[2]) <= 25:
      healthyBmis.append(float(bmi[6]))
   elif float(bmi[2]) >= 26 and float(bmi[2]) <= 30:
      overweightBmis.append(float(bmi[6])) 
   elif float(bmi[2]) > 30:
      obeseBmis.append(float(bmi[6]))

avgHealthyInsurance = getAvgInsurance(healthyBmis)
print(f"The average healthy insurance = ${avgHealthyInsurance}")

avgOverweightInsurance = getAvgInsurance(overweightBmis) 
print(f"The average overwiehgt insurance = ${avgOverweightInsurance}")

avgObeseInsurance = getAvgInsurance(obeseBmis) 
print(f"The average obese insurance = ${avgObeseInsurance}")
print("")

bmi_groups = ["Healthy", "Overweight", "Obese"]
insurance_bmi_costs = [avgHealthyInsurance, avgOverweightInsurance, avgObeseInsurance]

'''
bars_bmi_insurance = plt.bar(bmi_groups, insurance_bmi_costs)
bars_bmi_insurance[0].set_color("#4EF19F")
bars_bmi_insurance[1].set_color("#E2854F")
bars_bmi_insurance[2].set_color("#E93030")
plt.xlabel("BMI Groups")
plt.ylabel("Insurance Costs $")
plt.show()
'''



#ANALYING CHILDREN
#Finding the average price of insurance for the different amounts of children
zeroChildren = []
oneChild = []
twoChildren = []
threeChildren = []
fourChildren = []
fiveChildren = []

for children in rows:
   if int(children[3]) == 0:
      zeroChildren.append(float(children[6]))
   elif int(children[3]) == 1:
      oneChild.append(float(children[6]))
   elif int(children[3]) == 2:
      twoChildren.append(float(children[6])) 
   elif int(children[3]) == 3:
      threeChildren.append(float(children[6]))
   elif int(children[3]) == 4:
      fourChildren.append(float(children[6]))
   elif int(children[3]) == 5:
      fiveChildren.append(float(children[6]))


avgZeroChildrenInsurance = getAvgInsurance(zeroChildren)
avgOneChildInsurance = getAvgInsurance(oneChild)
avgTwoChildrenInsurance = getAvgInsurance(twoChildren)
avgThreeChildrenInsurance = getAvgInsurance(threeChildren)
avgFourChildrenInsurance = getAvgInsurance(fourChildren)
avgFiveChildrenInsurance = getAvgInsurance(fiveChildren)

print(f"The average zero children insurance =  {avgZeroChildrenInsurance}")
print(f"The average one child insurance =  {avgOneChildInsurance}")
print(f"The average two children insurance = {avgTwoChildrenInsurance}")
print(f"The average three children insurance = {avgThreeChildrenInsurance}")
print(f"The average four children insurance = {avgFourChildrenInsurance}")
print(f"The average five children insurance = {avgFiveChildrenInsurance}")
print("")

children_groups = ["Zero Children", "One Child", "Two Children", "Three Children", "Four Children", "Five Children"]
insurance_children_cost = [avgZeroChildrenInsurance, avgOneChildInsurance, avgTwoChildrenInsurance, avgThreeChildrenInsurance, avgFourChildrenInsurance, avgFiveChildrenInsurance]


'''
bars_children_insurance = plt.bar(children_groups, insurance_children_cost)
bars_children_insurance[0].set_color("#B96890")
bars_children_insurance[1].set_color("#54B787")
bars_children_insurance[2].set_color("#4486C8")
bars_children_insurance[3].set_color("#CD5757")
bars_children_insurance[4].set_color("#F29A3B")
plt.xlabel("Amount of Children")
plt.ylabel("Average Insurance Cost $")
plt.show()
'''


#ANALYZING SMOKER
#Finding the average insurance for smokers and non-smokers
smoker = []
nonSmoker = []

for person in rows:
   if person[4] == "yes":
      smoker.append(float(person[6]))
   elif person[4] == "no":
      nonSmoker.append(float(person[6]))

avgSmokerInsurance = getAvgInsurance(smoker)
avgNonSmokerInsurance = getAvgInsurance(nonSmoker)
print(f"The average smoker insurance = {avgSmokerInsurance}")
print(f"The average non-smoker insurance = {avgNonSmokerInsurance}")
print("")

smoker_groups = ["Smoker", "Non-Smoker"]
insurance_smoker_cost = [avgSmokerInsurance, avgNonSmokerInsurance]

'''
bars_smoker_insurance = plt.bar(smoker_groups, insurance_smoker_cost)
bars_smoker_insurance[0].set_color("#E93030")
bars_smoker_insurance[1].set_color("#4EF19F")
plt.xlabel("Smoker or Non-Smoker")
plt.ylabel("Average Insurance Cost $")
plt.show()
'''


#ANALYZING REGION
#Finding the average insurance for different regions
northeast = []
northwest = []
southeast = []
southwest = []

for region in rows:
   if region[5] == "northeast":
      northeast.append(float(region[6]))
   elif region[5] == "northwest":
      northwest.append(float(region[6]))
   elif region[5] == "southeast":
      southeast.append(float(region[6]))
   elif region[5] == "southwest":
      southwest.append(float(region[6]))
   
avgNortheastInsurance = getAvgInsurance(northeast)
avgNorthwestInsurance = getAvgInsurance(northwest)
avgSoutheastInsurance = getAvgInsurance(southeast)
avgSouthwestInsurance = getAvgInsurance(southwest)

print(f"The average Northeast insurance = {avgNortheastInsurance}")
print(f"The average Northwest insurance = {avgNorthwestInsurance}")
print(f"The average Southeast insurance = {avgSoutheastInsurance}")
print(f"The average Southwest insurance = {avgSouthwestInsurance}")

















