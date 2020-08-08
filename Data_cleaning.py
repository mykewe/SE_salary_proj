import pandas as pd
#Read data
df = pd.read_csv('glassdoor_jobs.csv')

#Salary Parsing
#Remove '-1'
df = df[df['Salary Estimate']!='-1']

#Split
salary  = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#Remove pounds sign and K
minus_kp = salary.apply(lambda x: x.replace('£','').replace('K',''))

df['min_salary'] = minus_kp.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kp.apply(lambda x: int(x.split('-')[1]))
df['mean_salary']= (df.min_salary + df.max_salary)/2

#Company name
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis=1)
df['company_txt'] = df.company_txt.apply(lambda x: str(x).replace('\n',''))

#City
df['job_city']= df['Location'].apply(lambda x: x.split(',')[0] if ',' in x  else x)
df.job_city.value_counts()

#Country
df['job_country']= df['Location'].apply(lambda x: x.split(',')[1] if ',' in x  else x)

df.job_country.value_counts()

df['isjobinHQ']= df.apply(lambda x: 1 if x['Location'].split(',')[0]==x['Headquarters'].split(',')[0] else 0, axis =1)

#Company age
df['age'] = df['Founded'].apply(lambda x: x if x <1 else 2020 -x)

#Type of ownership
df['ownership']=df['Type of ownership'].apply(lambda x: x.split('-')[1] if '-' in x else x)

#Job describtion
df['Job Description'][100]
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['html'] = df['Job Description'].apply(lambda x: 1 if 'html' in x.lower() else 0)
df['javascript'] = df['Job Description'].apply(lambda x: 1 if 'javascript' in x.lower() else 0)
df['java'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['cpp'] = df['Job Description'].apply(lambda x: 1 if 'c++' in x.lower() else 0)
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['C'] = df['Job Description'].apply(lambda x: 1 if 'c#' in x.lower() else 0)
df['css'] = df['Job Description'].apply(lambda x: 1 if 'css' in x.lower() else 0)  
df['scala'] = df['Job Description'].apply(lambda x: 1 if 'scala' in x.lower() else 0)  
df['matlab'] = df['Job Description'].apply(lambda x: 1 if 'matlab' in x.lower() else 0) 
df['ML'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0) 
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))

#Job title
def title_simplifier(title):
    if 'front' in title.lower():
        return 'frontend'
    elif 'back' in title.lower():
        return 'backend'
    elif 'full' in title.lower():
        return 'fullstack'
    elif 'data' in title.lower():
        return 'data'
    elif 'devops' in title.lower():
        return 'Devops'
    elif 'java' in title.lower():
        return 'java'
    elif 'python' in title.lower():
        return 'python'
    elif 'c++' in title.lower():
        return 'cpp'
    else:
        return 'na'
    
    
df['job_simp'] = df['Job Title'].apply(title_simplifier)    

#Competitors
df['comp_count'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x!='-1' else 0)


df.to_csv('salary_data_cleaned.csv',index = False)


