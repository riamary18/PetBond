from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchResults
import streamlit as st

api_key="AIzaSyDGPiQvM1bSoIJWcMHSfGKbvRpgm0IP8vA"
llm=GoogleGenerativeAI(model="models/text-bison-001",google_api_key=api_key)

with open('dog_breed.txt', 'r') as file:
    dog_breed = file.read()

st.title(f"Understanding {dog_breed}")

#TEMPLATES
#Basic Training Tips Template
training_template = PromptTemplate(
        input_variables=['dog_breed'],
        template='''Extract key training tips specific to {dog_breed}. Present them as concise bullet points for easy reference.''',
)
#Nutrition and Feeding Template
nutrition_template = PromptTemplate(
        input_variables=['dog_breed'],
        template='''Deliver tailored nutrition and feeding recommendations for {dog_breed} in the following format:
                    1. Ideal weight and physical attributes of {dog_breed}
                    2. Nutritional Requirements (presented in concise points)
                    3. Feeding Guidelines (outlined in concise points)
                    4. Special Considerations, if any (in concise points)'''
)
#Healthcare and Vaccinations Template
healthcare_template = PromptTemplate(
        input_variables=['dog_breed'],
        template='''Provide comprehensive information on healthcare and vaccination recommendations specific to {dog_breed}, including essential vaccinations, preventive care measures, 
                    and common health concerns to ensure optimal well-being.''',
)
#Bonding Activities Template
bonding_template = PromptTemplate(
        input_variables=['dog_breed'],
        template='''Retrieve a list of bonding activities tailored to {dog_breed} to strengthen the connection between dog owners and their pets.''',
)
#Enriching Environments Template
environment_template = PromptTemplate(
        input_variables=['dog_breed'],
        template='''Generate ideas for creating enriching environments specifically tailored to {dog_breed} to ensure optimal mental stimulation and overall well-being.''',
)

option=st.selectbox('Select a category',[' ','Basic Training Tips','Nutrition and Feeding','Healthcare and Vaccinations','Bonding Activities','Creating Enriching Environments'])

if option=='Basic Training Tips':
        try:
                chain=LLMChain(llm=llm,prompt=training_template,verbose=True,output_key='training')
                training=chain.run(dog_breed=dog_breed)
                st.write("### Training Tips:")
                st.write(training)
        except Exception as e:
                st.error(f"An error occurred: {e}")
elif option=='Nutrition and Feeding':
        try:
                chain=LLMChain(llm=llm,prompt=nutrition_template,verbose=True,output_key='nutrition')
                nutrition=chain.run(dog_breed=dog_breed)
                st.write("### Nutrition and Feeding:")
                st.write(nutrition)
        except Exception as e:
                st.error(f"An error occurred: {e}")
elif option=='Healthcare and Vaccinations':
        try:
                chain=LLMChain(llm=llm,prompt=healthcare_template,verbose=True,output_key='healthcare')
                healthcare=chain.run(dog_breed=dog_breed)
                st.write("### Healthcare:")
                st.write(healthcare)
        except Exception as e:
                st.error(f"An error occurred: {e}")
elif option=='Bonding Activities':
        try:
                chain=LLMChain(llm=llm,prompt=bonding_template,verbose=True,output_key='bonding')
                bonding=chain.run(dog_breed=dog_breed)
                st.write("### Bonding Activities:")
                st.write(bonding)
        except Exception as e:
                st.error(f"An error occurred: {e}")
elif option=='Creating Enriching Environments':
        try:
                chain=LLMChain(llm=llm,prompt=environment_template,verbose=True,output_key='environment')
                environment=chain.run(dog_breed=dog_breed)
                st.write("### Enriching Environment:")
                st.write(environment)
        except Exception as e:
                st.error(f"An error occurred: {e}")